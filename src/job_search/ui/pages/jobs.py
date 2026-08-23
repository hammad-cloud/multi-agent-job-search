"""Find jobs tab — search the job board and open roles in Design resume."""

from __future__ import annotations

import streamlit as st

from job_search.config import Settings
from job_search.models.schemas import JobBoardQuery
from job_search.tools.job_search import JobSearchTool
from job_search.ui.components.jobs.results_list import render_job_results
from job_search.ui.components.jobs.search_form import render_job_search_form
from job_search.ui.state import peek_design_prefill_notice


def render_jobs_page(settings: Settings, resume_file) -> None:
    notice = peek_design_prefill_notice()
    if notice:
        st.success(notice)

    keywords, location, source, submitted = render_job_search_form(settings.default_location)

    if submitted or "job_results" not in st.session_state:
        query = JobBoardQuery(
            keywords=keywords,
            location=location,
            source=source,
            results_limit=settings.results_limit,
        )
        st.session_state.job_results = JobSearchTool(settings).search(query)

    if submitted and not resume_file:
        st.caption("Upload a CV above to design resumes for these jobs.")

    render_job_results(st.session_state.get("job_results", []))
