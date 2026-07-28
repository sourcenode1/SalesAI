"""
Module card — premium gradient card rendered on the dashboard for each module.
"""
import streamlit as st


def render_module_card(module_key: str, module_config: dict, headline: str = "—") -> None:
    """
    Render a gradient KPI card for the given module.

    `module_key` : module identifier
    `module_config` : dict with keys: gradient, color, icon, description
    `headline` : the headline metric value to display
    """
    headline_str = headline

    gradient = module_config.get("gradient", "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
    color    = module_config.get("color", "#667eea")
    icon     = module_config.get("icon", "📊")
    desc     = module_config.get("description", "")

    st.markdown(
        f'<div style="background:{gradient};border-radius:20px;padding:1.6rem 1.4rem 1.4rem;'
        f'color:white;box-shadow:0 8px 32px {color}55;position:relative;overflow:hidden;'
        f'min-height:200px;display:flex;flex-direction:column;justify-content:space-between;">'
        f'<div style="position:absolute;top:-28px;right:-28px;width:110px;height:110px;'
        f'background:rgba(255,255,255,0.12);border-radius:50%;"></div>'
        f'<div style="position:absolute;bottom:-20px;left:-20px;width:70px;height:70px;'
        f'background:rgba(255,255,255,0.07);border-radius:50%;"></div>'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:0.6rem;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'<span style="font-family:\'Plus Jakarta Sans\',sans-serif;font-size:0.75rem;'
        f'font-weight:700;letter-spacing:0.12em;text-transform:uppercase;opacity:0.9;">{module_key}</span>'
        f'</div>'
        f'<div style="font-family:\'Outfit\',sans-serif;font-size:2.4rem;font-weight:800;'
        f'letter-spacing:-0.04em;line-height:1;margin:0.3rem 0 0.6rem;">{headline_str}</div>'
        f'<div style="font-size:0.78rem;opacity:0.85;font-weight:500;line-height:1.4;">{desc}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
