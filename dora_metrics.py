import streamlit as st
from PIL import Image

st.markdown("# DORA Metrics")
st.sidebar.markdown("#  DORA Metrics")

image = Image.open('DORA_model.png')
st.image(image, caption='DORA Metrics')