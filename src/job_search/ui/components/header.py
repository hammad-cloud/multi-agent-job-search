"""Dashboard header with title and CV upload."""

from __future__ import annotations

from datetime import date

import streamlit as st

from job_search.tools.resume_parser import ResumeParser


def render_header() -> object | None:
    """Render title row and CV uploader. Returns the uploaded file, if any."""
    top_left, top_right = st.columns([2, 1])
    with top_left:
        st.title("Job Search Dashboard")
        st.caption(f"Generated: {date.today().isoformat()}")
    with top_right:
        resume_file = st.file_uploader(
            "Upload CV",
            type=["txt", "md", "pdf"],
            label_visibility="visible",
        )
        if resume_file:
            char_count = _resume_char_count(resume_file)
            st.caption(f"Using {resume_file.name} ({char_count} characters)")
        else:
            st.caption("No CV uploaded yet · PDF, TXT, or MD")
    return resume_file


def _resume_char_count(uploaded_file) -> int:
    try:
        suffix = uploaded_file.name.rsplit(".", 1)[-1].lower()
        if suffix == "pdf":
            import tempfile
            from pathlib import Path

            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = Path(tmp.name)
            try:
                text = ResumeParser().parse(tmp_path)
            finally:
                tmp_path.unlink(missing_ok=True)
        else:
            text = uploaded_file.getvalue().decode("utf-8", errors="ignore")
        return len(text.strip())
    except Exception:
        return len(uploaded_file.getvalue())
