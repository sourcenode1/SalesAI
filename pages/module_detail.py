"""
Module detail page — renders the drill-down for the selected module.
Dispatches to the correct analysis component based on analysis type.
"""
import streamlit as st
from config.modules_config import MODULES_DATA
from utils.session_state import clear_module_selection

from components.sales_analysis import SALES_RENDERERS
from components.salesforce_analysis import SALESFORCE_RENDERERS
from components.customers_analysis import CUSTOMERS_RENDERERS
from components.products_analysis import PRODUCTS_RENDERERS
from components.supplychain_analysis import SUPPLYCHAIN_RENDERERS
from components.finance_analysis import FINANCE_RENDERERS

# Map module name → renderer dispatch dict
_MODULE_DISPATCH = {
    "sales":        SALES_RENDERERS,
    "salesforce":   SALESFORCE_RENDERERS,
    "customers":    CUSTOMERS_RENDERERS,
    "products":     PRODUCTS_RENDERERS,
    "supplychain":  SUPPLYCHAIN_RENDERERS,
    "finance":      FINANCE_RENDERERS,
}


def render_module_detail(module: str, selected_year: int, selected_month: str):
    data = MODULES_DATA.get(module)
    if not data:
        st.error(f"Unknown module: {module}")
        return

    color    = data["color"]
    gradient = data["gradient"]
    icon     = data.get("icon", "")
    desc     = data.get("description", "")

    # ── Header ──────────────────────────────────────────────────────────────
    col_back, col_title = st.columns([1, 9])
    with col_back:
        if st.button("← Back", key="back_btn"):
            clear_module_selection()
            st.rerun()

    with col_title:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
            <span style="font-size:2rem;">{icon}</span>
            <div>
                <div style="font-family:'Outfit',sans-serif;font-size:1.6rem;font-weight:800;
                            color:#ffffff;letter-spacing:-0.03em;">{module.title()}</div>
                <div style="font-size:0.85rem;color:#c0c8d4;font-weight:500;">{desc}</div>
            </div>
        </div>
        <div style="height:4px;background:{gradient};border-radius:4px;width:160px;margin-bottom:8px;"></div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Analysis tabs ────────────────────────────────────────────────────────
    analyses = data.get("analyses", [])
    if not analyses:
        st.info("No analyses configured for this module yet.")
        return

    tab_names  = [a["name"] for a in analyses]
    tabs       = st.tabs(tab_names)
    dispatch   = _MODULE_DISPATCH.get(module, {})

    for tab, analysis in zip(tabs, analyses):
        with tab:
            st.markdown(
                f"<div style='font-size:0.82rem;color:#c0c8d4;margin-bottom:12px;'>"
                f"{analysis['description']}</div>",
                unsafe_allow_html=True,
            )
            renderer = dispatch.get(analysis["type"])
            if renderer:
                renderer(selected_year, selected_month)
            else:
                st.warning(
                    f"Renderer for `{analysis['type']}` not registered. "
                    "Add it to the module's analysis file and update the dispatch map.",
                    icon="⚠️",
                )
