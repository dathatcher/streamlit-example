import streamlit as st
from PIL import Image

st.markdown("# DevOps Metrics Model")
st.sidebar.markdown("#  DORA Metrics Model")

image = Image.open('DORA_model.png')
st.image(image, caption='DORA ')