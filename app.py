
import streamlit as st
import pandas as pd
from job_matcher import calculate_match

st.set_page_config(
    page_title="JobPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 JobPilot AI")
st.subheader("Your AI-powered job search assistant")

st.write(
    "Find entry-level AI and Software Engineering jobs "
    "and compare them with your skills."
)
