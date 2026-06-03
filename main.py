import streamlit as st
from app.ui import init_session, render_sidebar, render_search

st.set_page_config(page_title="Note Search", page_icon="🔍")
st.title("🔍 Semantic Note Search")

init_session()
render_sidebar()
render_search()