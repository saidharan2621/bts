import os
import sys
import streamlit as st
from PIL import Image
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "model")))
from pages._pages import home, about, github, try_it

routes = {
    #"Home": home.main,
    "Try it out": try_it.main
    #"About": about.main,
    #"GitHub": github.main,
}

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon=":brain:",
    layout="wide",
    menu_items={
        "Get Help": "https://github.com/Oct4Pie/brain-tumor-detection",
        "Report a bug": "https://github.com/Oct4Pie/brain-tumor-detection/issues",
        "About": "Detecting brain tumors using *deep Convolutional Neural Networks*",
    },
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
   [data-testid="stSelectbox"] .st-emotion-cache-13bfgw8 p {
        font-size: 24px;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

def format_func(page):
    return page[0]

# Sidebar for image upload
st.sidebar.header("Upload MRI Image")
uploaded_file = st.sidebar.file_uploader("Choose an MRI image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded MRI Image", use_column_width=True)
    image = np.array(image)
    
    # Pass the uploaded image to try_it module for processing
    try_it.main(image)

page = st.selectbox(
    "Menu",
    list(routes.items()),
    index=0,
    format_func=format_func,
)

if uploaded_file is None:
    page[1]()
