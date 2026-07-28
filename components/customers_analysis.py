"""
Customers module — analysis components.
Wire real data into each render function when the schema is ready.
"""
import streamlit as st
from components.kpi_cards import render_kpi_row
from components.charts import plot_trend_line
from data.db_utils import fetch_module_data, fetch_yearly_trend
from config.app_config import MONTHS

COLOR = "#2E7D32"


def _placeholder_notice():
    st.info("Data source not yet connected. Wire `data/db_utils.py` to populate this view.", icon="🔌")


# ── Analysis: Distributor ───────────────────────────────────────────────────

def render_distributor_analysis(year: int, month: str):
    st.markdown("#### Distributor Analysis")
    render_kpi_row([
        {"label": "Active Distributors", "value": "485", "unit": ""},
        {"label": "New Additions",       "value": "32", "unit": ""},
        {"label": "Avg Billing",         "value": "₹8.5L", "unit": ""},
        {"label": "YoY Growth",          "value": "+12.4%", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("Customers", year)
    values = [row.get("active_distributors") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Active Distributors", COLOR)
    _placeholder_notice()


# ── Analysis: Retailer ──────────────────────────────────────────────────────

def render_retailer_analysis(year: int, month: str):
    st.markdown("#### Retailer Analysis")
    render_kpi_row([
        {"label": "Active Retailers", "value": "1,850", "unit": ""},
        {"label": "New Additions",    "value": "145", "unit": ""},
        {"label": "Avg Order Value",  "value": "₹45.3K", "unit": ""},
        {"label": "YoY Growth",       "value": "+18.7%", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("Customers", year)
    values = [row.get("active_retailers") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Active Retailers", COLOR)
    _placeholder_notice()


# ── Analysis: Vet ──────────────────────────────────────────────────────────

def render_vet_analysis(year: int, month: str):
    st.markdown("#### Veterinary Channel")
    render_kpi_row([
        {"label": "Vet Contacts",          "value": "650", "unit": ""},
        {"label": "Prescriptions Influenced", "value": "2,340", "unit": ""},
        {"label": "Coverage %",            "value": "78.5%", "unit": ""},
        {"label": "Engagement Score",      "value": "8.2", "unit": "/10"},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("Customers", year)
    values = [row.get("vet_contacts") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Vet Contacts", COLOR)
    _placeholder_notice()


# ── Analysis: Doctor ────────────────────────────────────────────────────────

def render_doctor_analysis(year: int, month: str):
    st.markdown("#### Doctor/Medical Channel")
    render_kpi_row([
        {"label": "Doctor Contacts", "value": "520", "unit": ""},
        {"label": "Recommendations", "value": "1,850", "unit": ""},
        {"label": "Engagement Rate", "value": "82.3%", "unit": ""},
        {"label": "Avg Interaction", "value": "3.6", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("Customers", year)
    values = [row.get("doctor_contacts") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Doctor Contacts", COLOR)
    _placeholder_notice()


# ── Analysis: Farmer ────────────────────────────────────────────────────────

def render_farmer_analysis(year: int, month: str):
    st.markdown("#### Farmer Segment")
    render_kpi_row([
        {"label": "Farmer Reach",    "value": "3,250", "unit": ""},
        {"label": "Adoption Rate",   "value": "71.4%", "unit": ""},
        {"label": "Satisfaction Score", "value": "8.5", "unit": "/10"},
        {"label": "YoY Growth",      "value": "+22.3%", "unit": ""},
    ], color=COLOR)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    trend = fetch_yearly_trend("Customers", year)
    values = [row.get("farmer_reach") for row in trend] if trend else []
    plot_trend_line(MONTHS, values + [None] * (12 - len(values)), "Farmer Reach", COLOR)
    _placeholder_notice()


# ── Dispatch map ────────────────────────────────────────────────────────────

CUSTOMERS_RENDERERS = {
    "customers_distributor": render_distributor_analysis,
    "customers_retailer":    render_retailer_analysis,
    "customers_vet":         render_vet_analysis,
    "customers_doctor":      render_doctor_analysis,
    "customers_farmer":      render_farmer_analysis,
}
