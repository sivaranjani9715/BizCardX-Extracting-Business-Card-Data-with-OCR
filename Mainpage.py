import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Bizcard app",
    page_icon="📇",
)

st.title("BizcardX: Extracting Business Card Data with OCR")
st.sidebar.success("Select a page above")

