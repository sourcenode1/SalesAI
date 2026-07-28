"""
Products module — analysis components.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#E65100"


def _placeholder_notice():
    st.info("Data source not yet connected. Wire `data/db_utils.py` to populate this view.", icon="🔌")


# ── Analysis: Growth Pattern ────────────────────────────────────────────────

def render_growth_pattern_analysis(year: int, month: str):
    st.markdown("#### Growth Pattern")
    render_kpi_row([
        {"label": "YoY Growth %",      "value": None, "unit": "%"},
        {"label": "MoM Growth %",      "value": None, "unit": "%"},
        {"label": "Top Growing SKU",   "value": None, "unit": ""},
        {"label": "Growth Rate",       "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Products", year)
    values = [row.get("yoy_growth") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Growth (%)", COLOR)
    _placeholder_notice()


# ── Analysis: Inventory Status ─────────────────────────────────────────────

def render_inventory_analysis(year: int, month: str):
    st.markdown("#### Inventory Status")
    render_kpi_row([
        {"label": "Stock Days",        "value": None, "unit": "days"},
        {"label": "Stockout Incidents","value": None, "unit": ""},
        {"label": "Inventory Turnover","value": None, "unit": "x"},
        {"label": "Carrying Cost",     "value": None, "unit": "$"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Products", year)
    values = [row.get("stock_days") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Stock Days", COLOR)
    _placeholder_notice()


# ── Analysis: Manufacturing Cost ────────────────────────────────────────────

def render_manufacturing_cost_analysis(year: int, month: str):
    st.markdown("#### Manufacturing Cost")
    render_kpi_row([
        {"label": "Cost Per Unit",     "value": None, "unit": "$"},
        {"label": "Raw Material %",    "value": None, "unit": "%"},
        {"label": "Packaging %",       "value": None, "unit": "%"},
        {"label": "Labour %",          "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Products", year)
    values = [row.get("cost_per_unit") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Cost Per Unit ($)", COLOR)
    _placeholder_notice()


# ── Analysis: Seasonality ──────────────────────────────────────────────────

def render_seasonality_analysis(year: int, month: str):
    st.markdown("#### Seasonality")
    render_kpi_row([
        {"label": "Peak Month Sales",  "value": None, "unit": "$"},
        {"label": "Off-Peak Sales",    "value": None, "unit": "$"},
        {"label": "Seasonal Index",    "value": None, "unit": ""},
        {"label": "Seasonality Range", "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Products", year)
    values = [row.get("seasonal_index") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Seasonal Index", COLOR)
    _placeholder_notice()


# ── Dispatch map ────────────────────────────────────────────────────────────

PRODUCTS_RENDERERS = {
    "products_growth":      render_growth_pattern_analysis,
    "products_inventory":   render_inventory_analysis,
    "products_manufacturing": render_manufacturing_cost_analysis,
    "products_seasonality": render_seasonality_analysis,
}
