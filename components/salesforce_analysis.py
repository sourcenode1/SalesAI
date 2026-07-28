"""
Sales Force module — analysis components.
Wire real data into each render function when the schema is ready.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_module_data, fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#6A1B9A"


def _placeholder_notice():
    st.info("Data source not yet connected. Wire `data/db_utils.py` to populate this view.", icon="🔌")


# ── Analysis: Visits ────────────────────────────────────────────────────────

def render_visits_analysis(year: int, month: str):
    st.markdown("#### Field Force Visits")
    render_kpi_row([
        {"label": "Total Visits",     "value": "2,850", "unit": ""},
        {"label": "Productive Visits","value": "2,445", "unit": ""},
        {"label": "Visit Frequency",  "value": "12.8", "unit": "/rep"},
        {"label": "Conversion Rate",  "value": "85.8%", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("SalesForce", year)
    if trend:
        plot_trend_line(trend, "month", "total_visits", "Total Visits", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Total Visits", COLOR)
    _placeholder_notice()


# ── Analysis: Trainings ────────────────────────────────────────────────────

def render_trainings_analysis(year: int, month: str):
    st.markdown("#### Training Programs")
    render_kpi_row([
        {"label": "Sessions Conducted", "value": "85", "unit": ""},
        {"label": "Attendance Rate",    "value": "91.3%", "unit": ""},
        {"label": "Completion Rate",    "value": "87.5%", "unit": ""},
        {"label": "Avg Session Size",   "value": "22", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("SalesForce", year)
    if trend:
        plot_trend_line(trend, "month", "sessions_conducted", "Sessions Conducted", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Sessions Conducted", COLOR)
    _placeholder_notice()


# ── Analysis: Travels & Expenses ────────────────────────────────────────────

def render_travels_analysis(year: int, month: str):
    st.markdown("#### Travel & Expenses")
    render_kpi_row([
        {"label": "Total Travel Expense", "value": "₹45.2L", "unit": ""},
        {"label": "Avg Per Rep",          "value": "₹2,145", "unit": ""},
        {"label": "Claims Pending",       "value": "₹8.5L", "unit": ""},
        {"label": "Expense/Visit",        "value": "₹1,585", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("SalesForce", year)
    if trend:
        plot_trend_line(trend, "month", "travel_expense", "Travel Expense (₹L)", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Travel Expense (₹L)", COLOR)
    _placeholder_notice()


# ── Analysis: Tour Plan Optimization ────────────────────────────────────────

def render_tourplan_analysis(year: int, month: str):
    st.markdown("#### Tour Plan Optimization")
    render_kpi_row([
        {"label": "Plan Adherence",  "value": "92.3%", "unit": ""},
        {"label": "Routes Optimized","value": "78", "unit": ""},
        {"label": "Coverage %",      "value": "87.6%", "unit": ""},
        {"label": "Efficiency Score","value": "8.7", "unit": "/10"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("SalesForce", year)
    if trend:
        plot_trend_line(trend, "month", "plan_adherence", "Plan Adherence %", COLOR)
    else:
        plot_trend_line([{"month": m, "value": None} for m in MONTHS], "month", "value", "Plan Adherence %", COLOR)
    _placeholder_notice()


# ── Dispatch map ────────────────────────────────────────────────────────────

SALESFORCE_RENDERERS = {
    "salesforce_visits":     render_visits_analysis,
    "salesforce_trainings":  render_trainings_analysis,
    "salesforce_travels":    render_travels_analysis,
    "salesforce_tour_plan":  render_tourplan_analysis,
}
