import streamlit as st

# Page title
st.set_page_config(page_title="UV Packages Demo", page_icon="📦", layout="centered")

# Main title
st.title("📦 Welcome to my UV Packages Demo")

# Subtitle / Description
st.markdown("This app is built with **Streamlit** and managed using **UV** 🚀")

# Add some interactivity
name = st.text_input("👉 Enter your name:")

if name:
    st.success(f"Hello, {name}! 👋 Thanks for trying out UV + Streamlit!")

# Add a button
if st.button("Show Info"):
    st.info("UV helps you manage Python packages faster and cleaner than pip.")
