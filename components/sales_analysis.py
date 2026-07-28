"""
Sales module — analysis components with real data from MainData.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_module_data, fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#1565C0"


# ── Analysis: Invoice Analysis ──────────────────────────────────────────────

def render_invoice_analysis(year: int, month: str):
    st.markdown("#### Invoice Analysis")
    data = fetch_module_data("sales", year, month)

    if data:
        render_kpi_row([
            {"label": "Invoice Count",    "value": f"{data['invoice_count']:,}", "unit": ""},
            {"label": "Net Sales",        "value": f"₹{data['net_sales']/100000:.1f}L", "unit": ""},
            {"label": "Avg Invoice Size", "value": f"₹{data['avg_invoice']:,.0f}", "unit": ""},
            {"label": "MoM Growth",       "value": f"{data['mom_growth']:+.1f}%", "unit": ""},
        ], color=COLOR)
    else:
        render_kpi_row([
            {"label": "Invoice Count", "value": "—", "unit": ""},
            {"label": "Net Sales", "value": "—", "unit": ""},
            {"label": "Avg Invoice Size", "value": "—", "unit": ""},
            {"label": "MoM Growth", "value": "—", "unit": ""},
        ], color=COLOR)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    trend = fetch_yearly_trend("Sales", year)
    if trend:
        plot_trend_line(trend, "month", "invoice_count", "Invoice Count", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Invoice Count", COLOR)


# ── Analysis: Orders Analysis ───────────────────────────────────────────────

def render_orders_analysis(year: int, month: str):
    st.markdown("#### Orders Analysis")
    data = fetch_module_data("sales", year, month)

    if data:
        render_kpi_row([
            {"label": "Total Qty Sold",    "value": f"{data['total_qty']:,.0f}", "unit": ""},
            {"label": "Active HQs",        "value": f"{data['active_hqs']}", "unit": ""},
            {"label": "Active Products",   "value": f"{data['active_products']}", "unit": ""},
            {"label": "MoM Growth",        "value": f"{data['mom_growth']:+.1f}%", "unit": ""},
        ], color=COLOR)
    else:
        render_kpi_row([
            {"label": "Total Qty Sold", "value": "—", "unit": ""},
            {"label": "Active HQs", "value": "—", "unit": ""},
            {"label": "Active Products", "value": "—", "unit": ""},
            {"label": "MoM Growth", "value": "—", "unit": ""},
        ], color=COLOR)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    trend = fetch_yearly_trend("Sales", year)
    if trend:
        plot_trend_line(trend, "month", "total_orders", "Total Qty Sold", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Total Qty Sold", COLOR)


# ── Analysis: Net Sales & Gross Sales ───────────────────────────────────────

def render_netsales_analysis(year: int, month: str):
    st.markdown("#### Net Sales & Gross Sales")
    data = fetch_module_data("sales", year, month)

    if data:
        render_kpi_row([
            {"label": "Net Sales",       "value": f"₹{data['net_sales']/100000:.1f}L", "unit": ""},
            {"label": "Invoice Count",   "value": f"{data['invoice_count']:,}", "unit": ""},
            {"label": "Active HQs",      "value": f"{data['active_hqs']}", "unit": ""},
            {"label": "MoM Growth",      "value": f"{data['mom_growth']:+.1f}%", "unit": ""},
        ], color=COLOR)
    else:
        render_kpi_row([
            {"label": "Net Sales", "value": "—", "unit": ""},
            {"label": "Invoice Count", "value": "—", "unit": ""},
            {"label": "Active HQs", "value": "—", "unit": ""},
            {"label": "MoM Growth", "value": "—", "unit": ""},
        ], color=COLOR)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    trend = fetch_yearly_trend("Sales", year)
    if trend:
        plot_trend_line(trend, "month", "net_sales", "Net Sales (₹L)", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Net Sales (₹L)", COLOR)


# ── Dispatch map ────────────────────────────────────────────────────────────

SALES_RENDERERS = {
    "sales_invoice":     render_invoice_analysis,
    "sales_orders":      render_orders_analysis,
    "sales_net_gross":   render_netsales_analysis,
}
