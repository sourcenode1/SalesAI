"""
Supply Chain module — analysis components.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#00695C"


def _placeholder_notice():
    st.info("Data source not yet connected. Wire `data/db_utils.py` to populate this view.", icon="🔌")


# ── Analysis: Fill Rate ─────────────────────────────────────────────────────

def render_fillrate_analysis(year: int, month: str):
    st.markdown("#### Fill Rate")
    render_kpi_row([
        {"label": "Fill Rate %",       "value": None, "unit": "%"},
        {"label": "Order Accuracy",    "value": None, "unit": "%"},
        {"label": "On-Time Delivery %","value": None, "unit": "%"},
        {"label": "Partial Orders",    "value": None, "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Supply Chain", year)
    values = [row.get("fill_rate") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Fill Rate (%)", COLOR)
    _placeholder_notice()


# ── Analysis: Stock ─────────────────────────────────────────────────────────

def render_stock_analysis(year: int, month: str):
    st.markdown("#### Stock")
    render_kpi_row([
        {"label": "Total Stock Value", "value": None, "unit": "$"},
        {"label": "Slow-Moving %",     "value": None, "unit": "%"},
        {"label": "Days of Inventory", "value": None, "unit": "days"},
        {"label": "Stock-Outs",        "value": None, "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Supply Chain", year)
    values = [row.get("stock_value") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Stock Value ($)", COLOR)
    _placeholder_notice()


# ── Analysis: Back Orders ──────────────────────────────────────────────────

def render_backorders_analysis(year: int, month: str):
    st.markdown("#### Back Orders")
    render_kpi_row([
        {"label": "Pending Backorders","value": None, "unit": ""},
        {"label": "Backorder Value",   "value": None, "unit": "$"},
        {"label": "Avg Resolution Days","value": None, "unit": "days"},
        {"label": "Backorder %",       "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Supply Chain", year)
    values = [row.get("backorders") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Backorders", COLOR)
    _placeholder_notice()


# ── Analysis: Production ────────────────────────────────────────────────────

def render_production_analysis(year: int, month: str):
    st.markdown("#### Production")
    render_kpi_row([
        {"label": "Production Volume", "value": None, "unit": "units"},
        {"label": "Capacity Utilization %","value": None, "unit": "%"},
        {"label": "Defect Rate",       "value": None, "unit": "%"},
        {"label": "On-Time Completion","value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Supply Chain", year)
    values = [row.get("production_volume") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Production Volume (units)", COLOR)
    _placeholder_notice()


# ── Analysis: Warehouse ─────────────────────────────────────────────────────

def render_warehouse_analysis(year: int, month: str):
    st.markdown("#### Warehouse")
    render_kpi_row([
        {"label": "Warehouse Utilization %","value": None, "unit": "%"},
        {"label": "Dispatch Accuracy",  "value": None, "unit": "%"},
        {"label": "Avg Dispatch Time",  "value": None, "unit": "hrs"},
        {"label": "Space Available",    "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Supply Chain", year)
    values = [row.get("warehouse_utilization") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Warehouse Utilization (%)", COLOR)
    _placeholder_notice()


# ── Dispatch map ────────────────────────────────────────────────────────────

SUPPLYCHAIN_RENDERERS = {
    "supplychain_fill_rate":   render_fillrate_analysis,
    "supplychain_stock":       render_stock_analysis,
    "supplychain_backorders":  render_backorders_analysis,
    "supplychain_production":  render_production_analysis,
    "supplychain_warehouse":   render_warehouse_analysis,
}
