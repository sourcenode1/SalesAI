"""
Finance module — analysis components.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#AD1457"


def _placeholder_notice():
    st.info("Data source not yet connected. Wire `data/db_utils.py` to populate this view.", icon="🔌")


# ── Analysis: Outstanding ──────────────────────────────────────────────────

def render_outstanding_analysis(year: int, month: str):
    st.markdown("#### Outstanding")
    render_kpi_row([
        {"label": "Total Outstanding",  "value": None, "unit": "$"},
        {"label": "0-30 Days",          "value": None, "unit": "$"},
        {"label": "30-60 Days",         "value": None, "unit": "$"},
        {"label": "60+ Days",           "value": None, "unit": "$"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Finance", year)
    values = [row.get("total_outstanding") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Outstanding ($)", COLOR)
    _placeholder_notice()


# ── Analysis: Collections ──────────────────────────────────────────────────

def render_collections_analysis(year: int, month: str):
    st.markdown("#### Collections")
    render_kpi_row([
        {"label": "Collection %",       "value": None, "unit": "%"},
        {"label": "Collection Amount",  "value": None, "unit": "$"},
        {"label": "Target Achievement", "value": None, "unit": "%"},
        {"label": "Days to Collect",    "value": None, "unit": "days"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Finance", year)
    values = [row.get("collection_percent") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Collection %", COLOR)
    _placeholder_notice()


# ── Analysis: Credit Days ──────────────────────────────────────────────────

def render_creditdays_analysis(year: int, month: str):
    st.markdown("#### Credit Days")
    render_kpi_row([
        {"label": "Avg Credit Days",    "value": None, "unit": "days"},
        {"label": "Overdue Accounts",   "value": None, "unit": ""},
        {"label": "Credit Limit Breaches","value": None, "unit": ""},
        {"label": "DSO",                "value": None, "unit": "days"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Finance", year)
    values = [row.get("avg_credit_days") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Avg Credit Days", COLOR)
    _placeholder_notice()


# ── Analysis: Bad Debt ─────────────────────────────────────────────────────

def render_baddebt_analysis(year: int, month: str):
    st.markdown("#### Bad Debt")
    render_kpi_row([
        {"label": "Bad Debt Amount",    "value": None, "unit": "$"},
        {"label": "Bad Debt %",         "value": None, "unit": "%"},
        {"label": "Provision Amount",   "value": None, "unit": "$"},
        {"label": "Write-off Rate",     "value": None, "unit": "%"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Finance", year)
    values = [row.get("bad_debt_amount") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Bad Debt ($)", COLOR)
    _placeholder_notice()


# ── Analysis: EBITDA ────────────────────────────────────────────────────────

def render_ebitda_analysis(year: int, month: str):
    st.markdown("#### EBITDA")
    render_kpi_row([
        {"label": "EBITDA",             "value": None, "unit": "$"},
        {"label": "EBITDA Margin %",    "value": None, "unit": "%"},
        {"label": "YoY Change",         "value": None, "unit": "%"},
        {"label": "YoY Change Amount",  "value": None, "unit": "$"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend  = fetch_yearly_trend("Finance", year)
    values = [row.get("ebitda") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "EBITDA ($)", COLOR)
    _placeholder_notice()


# ── Dispatch map ────────────────────────────────────────────────────────────

FINANCE_RENDERERS = {
    "finance_outstanding":  render_outstanding_analysis,
    "finance_collections":  render_collections_analysis,
    "finance_credit_days":  render_creditdays_analysis,
    "finance_bad_debt":     render_baddebt_analysis,
    "finance_ebitda":       render_ebitda_analysis,
}
