import streamlit as st

st.markdown("# DevOps Metrics Model")
st.sidebar.markdown("#  DORA Metrics Model")

from PIL import Image
image = Image.open('DORA_model.png')

st.image(image, caption='DORA ')