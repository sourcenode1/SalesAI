"""
Generic KPI card tiles rendered at the top of drill-down pages.
"""
import streamlit as st


def render_kpi_row(metrics: list[dict], color: str = "#1e293b"):
    """
    Render a horizontal row of KPI tiles.

    `metrics` is a list of dicts with keys:
        label  : str  — display label
        value  : any  — the metric value (formatted automatically)
        unit   : str  — optional unit suffix (e.g. "%", "$", "units")
        delta  : str  — optional delta string (e.g. "+3.2%")
        delta_up : bool — True = green, False = red, None = neutral

    Example:
        render_kpi_row([
            {"label": "Total Revenue", "value": 125000, "unit": "$", "delta": "+12.5%", "delta_up": True},
            {"label": "Avg Order", "value": 450, "unit": "$"},
        ], color="#2563eb")
    """
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        with col:
            _render_single_kpi(metric, color)


def _render_single_kpi(metric: dict, accent_color: str):
    label     = metric.get("label", "")
    raw_value = metric.get("value", None)
    unit      = metric.get("unit", "")
    delta     = metric.get("delta", "")
    delta_up  = metric.get("delta_up", None)

    if raw_value is None:
        value_str = "—"
    elif isinstance(raw_value, float):
        value_str = f"{raw_value:,.1f}"
    elif isinstance(raw_value, int):
        value_str = f"{raw_value:,}"
    else:
        value_str = str(raw_value)

    if unit:
        value_str = f"{value_str} {unit}"

    if delta:
        if delta_up is True:
            delta_color = "#16a34a"
            delta_arrow = "&#8593;"
        elif delta_up is False:
            delta_color = "#dc2626"
            delta_arrow = "&#8595;"
        else:
            delta_color = "#64748b"
            delta_arrow = "&#8594;"
        delta_html = (
            f'<div style="font-size:0.78rem;font-weight:700;color:{delta_color};margin-top:4px;">'
            f'{delta_arrow} {delta}</div>'
        )
    else:
        delta_html = ""

    st.markdown(f"""
    <div class="kpi-tile" style="border-top: 3px solid {accent_color};">
        <div style="font-size:0.72rem;font-weight:700;letter-spacing:0.1em;
                    text-transform:uppercase;color:#c0c8d4;margin-bottom:4px;">{label}</div>
        <div style="font-family:'Outfit',sans-serif;font-size:1.7rem;
                    font-weight:800;color:#ffffff;letter-spacing:-0.03em;">{value_str}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)
