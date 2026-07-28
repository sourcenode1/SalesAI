"""
Session state management utilities for SalesAI
"""
import streamlit as st
from datetime import datetime

# Valid active_section values:
# "data_pulse" | "modelling" | "events_market" | "briefing" | "advisor"
#
# Valid active_view values (when active_section == "data_pulse"):
# "dashboard" | "sales" | "salesforce" | "customers" | "products" | "supplychain" | "finance"
# When active_section is NOT "data_pulse", active_view mirrors the section key.


def initialize_session_state():
    """Initialize all session state variables with sensible defaults."""
    if "selected_year" not in st.session_state:
        st.session_state.selected_year = datetime.now().year

    if "selected_month" not in st.session_state:
        st.session_state.selected_month = datetime.now().strftime("%B")

    if "selected_module" not in st.session_state:
        st.session_state.selected_module = None  # None means no drill-down active

    if "active_section" not in st.session_state:
        st.session_state.active_section = "data_pulse"

    if "active_view" not in st.session_state:
        st.session_state.active_view = "dashboard"


def update_date_selection(year, month):
    """Update year/month in session state. Returns True if changed (triggers rerun)."""
    if year != st.session_state.selected_year or month != st.session_state.selected_month:
        st.session_state.selected_year = year
        st.session_state.selected_month = month
        return True
    return False


def select_module(module_key: str):
    """Open the drill-down for a specific module."""
    st.session_state.selected_module = module_key


def clear_module_selection():
    """Return to dashboard overview."""
    st.session_state.selected_module = None
