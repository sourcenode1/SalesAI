"""
Dashboard — 6-module overview grid with gradient cards.
"""
import streamlit as st
from config.modules_config import MODULES_DATA
from components.module_card import render_module_card
from components.charts import plot_module_comparison
from utils.session_state import select_module
from data.db_utils import fetch_module_data


def _get_headlines(year: int, month: str) -> dict:
    """Get headline KPI for each module."""
    headlines = {}

    sales_data = fetch_module_data("sales", year, month)
    if sales_data:
        headlines["sales"] = f"₹{sales_data['net_sales']/100000:.1f}L"
    else:
        headlines["sales"] = "—"

    sf_data = fetch_module_data("salesforce", year, month)
    if sf_data:
        headlines["salesforce"] = f"{sf_data['total_visits']:,} visits"
    else:
        headlines["salesforce"] = "—"

    # These modules don't have data wired yet
    headlines["customers"] = "—"
    headlines["products"] = "—"
    headlines["supplychain"] = "—"
    headlines["finance"] = "—"

    return headlines


def render_dashboard(selected_year: int, selected_month: str):
    st.markdown("""
    <div style="margin-bottom:1.2rem;">
        <div style="font-family:'Outfit',sans-serif;font-size:1.5rem;font-weight:700;
                    color:#ffffff;letter-spacing:-0.02em;">Module Overview</div>
        <div style="font-size:0.85rem;color:#c0c8d4;margin-top:3px;font-weight:500;">
            Click any module to drill down
        </div>
    </div>
    """, unsafe_allow_html=True)

    headlines = _get_headlines(selected_year, selected_month)

    # Render cards in a 3-column grid (2 rows for 6 modules)
    module_names = list(MODULES_DATA.keys())
    rows = [module_names[:3], module_names[3:]]

    for row_modules in rows:
        cols = st.columns(3, gap="medium")
        for col, module in zip(cols, row_modules):
            data = MODULES_DATA[module]
            with col:
                render_module_card(module, data, headline=headlines.get(module, "—"))
                btn_key = f"btn_{module.replace(' ', '_')}"
                if st.button("Open Details", key=btn_key, use_container_width=True):
                    select_module(module)
                    st.rerun()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.divider()

    # Global comparison chart
    st.markdown("""
    <div style="margin-bottom:1rem;">
        <div style="font-family:'Outfit',sans-serif;font-size:1.3rem;font-weight:700;
                    color:#ffffff;letter-spacing:-0.02em;">Global Snapshot</div>
        <div style="font-size:0.82rem;color:#c0c8d4;margin-top:3px;font-weight:500;">
            Net Sales (₹L) by module where data is available
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Use real sales value for the chart
    sales_data = fetch_module_data("sales", selected_year, selected_month)
    sf_data = fetch_module_data("salesforce", selected_year, selected_month)
    values = [
        sales_data.get("net_sales", 0) / 100000 if sales_data else 0,
        sf_data.get("total_visits", 0) if sf_data else 0,
        0, 0, 0, 0,
    ]
    plot_module_comparison({
        "modules": module_names,
        "values": values,
        "colors": [MODULES_DATA[m]["color"] for m in module_names],
        "title": "Headline Metrics",
    })
