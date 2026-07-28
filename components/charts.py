"""
Generic Plotly chart helpers used across multiple modules.
"""
import plotly.graph_objects as go
import streamlit as st


def plot_module_comparison(data: dict):
    """
    Horizontal bar chart comparing modules.
    
    `data` dict with keys:
        modules : list  — module names
        values : list  — corresponding values
        colors : list  — corresponding colors
        title : str  — chart title (optional)
    """
    modules = data.get("modules", [])
    values = data.get("values", [])
    colors = data.get("colors", [])
    title = data.get("title", "Module Overview")
    
    display_values = values if any(v and v != 0 for v in values) else [1] * len(modules)

    fig = go.Figure(go.Bar(
        x=display_values,
        y=modules,
        orientation="h",
        marker_color=colors,
        text=[f"{v:,.1f}" if v else "—" for v in values],
        textposition="inside",
        insidetextfont=dict(color="white", size=12, family="Plus Jakarta Sans"),
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit", size=16, color="#ffffff")),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=300,
        margin=dict(l=0, r=20, t=40, b=20),
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, tickfont=dict(family="Plus Jakarta Sans", size=12, color="#c0c8d4")),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_trend_line(data_or_x, x_col_or_y=None, y_col=None, title: str = "", color: str = "#2563eb"):
    """
    Line chart with markers for monthly trends.
    
    Supports two call patterns:
    1. plot_trend_line(data: list[dict], x_col, y_col, title, color)
    2. plot_trend_line(x_list, y_list, title, color)  [legacy]
    """
    # Detect call pattern
    if isinstance(data_or_x, list) and data_or_x and isinstance(data_or_x[0], dict):
        # Pattern 1: list of dicts
        x_values = [d.get(x_col_or_y) for d in data_or_x]
        y_values = [d.get(y_col) for d in data_or_x]
    elif isinstance(data_or_x, list):
        # Pattern 2: legacy (x_list, y_list, title, color)
        x_values = data_or_x
        y_values = x_col_or_y if isinstance(x_col_or_y, list) else []
        title = y_col if isinstance(y_col, str) else title
        color = title if title and title.startswith("#") else color
        if isinstance(y_col, str) and y_col.startswith("#"):
            color = y_col
            title = x_col_or_y if isinstance(x_col_or_y, str) else ""
    else:
        x_values = []
        y_values = []

    fig = go.Figure(go.Scatter(
        x=x_values,
        y=y_values if y_values else [0] * len(x_values),
        mode="lines+markers",
        line=dict(color=color, width=2.5),
        marker=dict(size=7, color=color),
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit", size=16, color="#ffffff")) if title else {},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=280,
        margin=dict(l=10, r=10, t=30 if title else 10, b=20),
        xaxis=dict(showgrid=False, tickfont=dict(family="Plus Jakarta Sans", size=11, color="#c0c8d4")),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)",
                   tickfont=dict(family="Plus Jakarta Sans", size=11, color="#c0c8d4")),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_donut(data: dict, title: str = ""):
    """
    Donut / pie chart for breakdowns.
    
    `data` dict with keys:
        labels : list  — category labels
        values : list  — corresponding values
        colors : list  — corresponding colors
    """
    labels = data.get("labels", [])
    values = data.get("values", [])
    colors = data.get("colors", [])
    
    if not any(values):
        values = [1] * len(labels)

    fig = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.55,
        marker_colors=colors,
        textinfo="label+percent",
        textfont=dict(family="Plus Jakarta Sans", size=12, color="#ffffff"),
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(family="Outfit", size=15, color="#ffffff")) if title else {},
        paper_bgcolor="rgba(0,0,0,0)",
        height=280,
        margin=dict(l=0, r=0, t=40 if title else 0, b=0),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)
