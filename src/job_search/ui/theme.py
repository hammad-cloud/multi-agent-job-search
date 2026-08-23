"""Shared dashboard theme: colors, CSS injection, and chart layout defaults."""

from __future__ import annotations

import streamlit as st

from job_search.models.schemas import TrackerStatus

# Metric accent colors (match dashboard screenshot)
COLORS = {
    "total": "#e5e7eb",
    "in_process": "#22d3ee",
    "active": "#3b82f6",
    "interview": "#fbbf24",
    "offer": "#a78bfa",
    "hired": "#22c55e",
    "rejected": "#ef4444",
    "sector_bar": "#3b82f6",
    "channel_bar": "#a78bfa",
    "funnel_bar": "#3b82f6",
}

STATUS_CHART_COLORS = {
    "Applied / Active": COLORS["active"],
    "In process": COLORS["in_process"],
    "Interview": COLORS["interview"],
    "Offer": COLORS["offer"],
    "Hired": COLORS["hired"],
    "Rejected/Closed": COLORS["rejected"],
}

# Legend order matching the dashboard screenshot (colored dots)
STATUS_LEGEND: list[tuple[TrackerStatus, str, str]] = [
    (TrackerStatus.ACTIVE, COLORS["active"], "Active"),
    (TrackerStatus.INTERVIEW, COLORS["interview"], "Interview"),
    (TrackerStatus.OFFER, COLORS["offer"], "Offer"),
    (TrackerStatus.HIRED, COLORS["hired"], "Hired"),
    (TrackerStatus.REJECTED, COLORS["rejected"], "Rejected/Closed"),
]

DASHBOARD_CSS = """
<style>
  .block-container {
    padding-top: 1.2rem;
    max-width: 1400px;
  }

  /* Pill-style tabs */
  .stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: transparent;
    border-bottom: none;
  }
  .stTabs [data-baseweb="tab"] {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 999px;
    color: #9ca3af;
    padding: 8px 20px;
    font-weight: 600;
  }
  .stTabs [aria-selected="true"] {
    background: #2563eb !important;
    border-color: #2563eb !important;
    color: #ffffff !important;
  }

  /* Upload button styling */
  [data-testid="stFileUploader"] section {
    padding: 0;
  }
  [data-testid="stFileUploader"] button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
  }
  [data-testid="stFileUploader"] button:hover {
    background: #1d4ed8;
    color: white;
    border: none;
  }

  /* Bordered chart containers */
  [data-testid="stVerticalBlockBorderWrapper"] {
    background: #161b22;
    border-color: #30363d !important;
    border-radius: 12px;
    padding: 8px 12px 4px;
  }
  [data-testid="stVerticalBlockBorderWrapper"] p {
    color: #f3f4f6;
    font-weight: 600;
    margin-bottom: 0;
  }

  /* Hide plotly mode bar for cleaner cards */
  .js-plotly-plot .plotly .modebar { display: none !important; }

  /* Find jobs */
  .jobs-found {
    color: #9ca3af;
    font-size: 14px;
    margin: 12px 0 10px;
  }
  div[data-testid="stMarkdownContainer"] a {
    color: #60a5fa;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }
</style>
"""


def inject_dashboard_theme() -> None:
    st.markdown(DASHBOARD_CSS, unsafe_allow_html=True)


def plotly_layout(**overrides) -> dict:
    base = {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"color": "#9ca3af", "size": 12},
        "margin": {"l": 12, "r": 12, "t": 12, "b": 12},
        "showlegend": False,
        "xaxis": {"gridcolor": "#30363d", "zerolinecolor": "#30363d"},
        "yaxis": {"gridcolor": "#30363d", "zerolinecolor": "#30363d"},
    }
    base.update(overrides)
    return base
