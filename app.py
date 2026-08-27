"""
SalesAI — Main Application
Data Pulse | Modelling Zone | Events & Market | Intelligence Briefing | Advisor
"""
import streamlit as st

from config.app_config import PAGE_CONFIG, YEAR_RANGE, MONTHS
from assets.styles import CUSTOM_CSS
from utils.session_state import (
    initialize_session_state,
    update_date_selection,
    clear_module_selection,
)
from pages.dashboard import render_dashboard
from pages.module_detail import render_module_detail


def render_view_toggle():
    """Top-level navigation pills."""
    active_section = st.session_state.active_section

    top_labels = {
        "data_pulse":    "Data Pulse",
        "modelling":     "Modelling Zone",
        "events_market": "Events & Market",
        "briefing":      "Intelligence Briefing",
        "advisor":       "Advisor",
    }
    cols = st.columns(len(top_labels))
    for col, key in zip(cols, top_labels.keys()):
        with col:
            is_active = active_section == key
            if st.button(top_labels[key], key=f"nav_top_{key}", use_container_width=True,
                         type="primary" if is_active else "secondary"):
                st.session_state.active_section = key
                clear_module_selection()
                st.rerun()


def _render_date_selector(key_suffix: str = ""):
    """Shared date selector. Returns (selected_year, selected_month)."""
    years = list(range(YEAR_RANGE[0], YEAR_RANGE[1]))
    c1, c2 = st.columns(2)
    with c1:
        selected_year = st.selectbox(
            "Select Year", years,
            index=years.index(st.session_state.selected_year),
            key=f"year_sel{key_suffix}",
        )
    with c2:
        selected_month = st.selectbox(
            "Select Month", MONTHS,
            index=MONTHS.index(st.session_state.selected_month),
            key=f"month_sel{key_suffix}",
        )
    if update_date_selection(selected_year, selected_month):
        st.rerun()
    return selected_year, selected_month


def render_advisor():
    """Advisor section with chat-like placeholder and example questions."""
    st.divider()
    st.header("Advisor")
    
    st.markdown(
        "<p style='text-align:center;color:#c8d6e5;margin-bottom:2rem;'>"
        "Ask me anything about your sales strategy and performance.</p>",
        unsafe_allow_html=True,
    )
    
    # Example questions
    st.subheader("Example Questions")
    example_questions = [
        "How do I increase revenue by 10%?",
        "Where should I recruit 50 new sales reps?",
        "If I reduce price of product by 5% what will be the impact on my EBITDA?",
    ]
    
    for question in example_questions:
        st.markdown(f"• *{question}*")
    
    st.divider()
    st.info("Chat interface coming soon — ask your questions above!")


def main():
    st.set_page_config(**PAGE_CONFIG)
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    initialize_session_state()

    st.markdown(
        "<h1 style='text-align:center;font-size:3.5rem;margin-bottom:0.5rem;color:#ffffff;text-shadow:0 2px 20px rgba(100,150,255,0.4);'>MITRA SalesAI</h1>",
        unsafe_allow_html=True,
    )
    render_view_toggle()

    active_section = st.session_state.active_section

    # ── Non-Data-Pulse sections (placeholder pages) ───────────────────────────
    if active_section == "modelling":
        st.divider()
        st.header("Modelling Zone")
        st.info("Modelling Zone content coming soon.")
        return

    if active_section == "events_market":
        st.divider()
        st.header("Events & Market")
        st.info("Events & Market content coming soon.")
        return

    if active_section == "briefing":
        st.divider()
        st.header("Intelligence Briefing")
        st.info("Intelligence Briefing content coming soon.")
        return

    if active_section == "advisor":
        render_advisor()
        return

    # ── Data Pulse: Dashboard (default home) ──────────────────────────────────
    selected_year, selected_month = _render_date_selector()
    st.markdown(
        f"<p style='text-align:center;font-size:16px;color:#c8d6e5;'>"
        f"Showing data for: <b>{selected_month} {selected_year}</b></p>",
        unsafe_allow_html=True,
    )
    st.divider()

    if st.session_state.selected_module:
        render_module_detail(st.session_state.selected_module, selected_year, selected_month)
    else:
        render_dashboard(selected_year, selected_month)


if __name__ == "__main__":
    main()
