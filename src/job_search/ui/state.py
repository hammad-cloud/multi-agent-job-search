"""Session-state helpers for cross-tab UI actions."""

from __future__ import annotations

import streamlit as st

from job_search.models.schemas import JobPosting


def prefill_design_resume(job: JobPosting) -> None:
    """Load a job listing into the Design resume tab fields."""
    st.session_state.design_company = job.company
    st.session_state.design_role = job.title
    st.session_state.design_job_description = job.description
    st.session_state.design_job_url = str(job.url) if job.url else ""
    st.session_state.design_prefill_notice = (
        f"Loaded **{job.title}** at **{job.company}**. "
        "Open the **Design resume** tab to continue."
    )


def consume_design_prefill_notice() -> str | None:
    return st.session_state.pop("design_prefill_notice", None)


def peek_design_prefill_notice() -> str | None:
    return st.session_state.get("design_prefill_notice")
