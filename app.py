"""Titik masuk Streamlit untuk sistem penelitian Sumiati."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Percepatan Masa Studi · Sumiati", layout="wide")
application = Path(__file__).with_name("sistem.html").read_text(encoding="utf-8")
components.html(application, height=940, scrolling=True)
