import streamlit as st
from broll_stitcher_core import make_video
import base64

st.set_page_config(
    page_title="101VideoGenerator App 1.0",
    page_icon="🎬",
    layout="centered"
)

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        color: #fff;
        font-weight: bold;
    }}
    h1 {{
        text-align: center;
        font-size: 2.8rem;
        color: white;
        background-color: rgba(0,0,0,0.5);
        padding: 0.5rem;
        border-radius: 10px;
    }}
    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stSlider > div {{
        background-color: rgba(255, 255, 255, 0.85) !important;
        color: #000 !important;
        border-radius: 10px;
        padding: 6px 10px;
    }}
    button[kind="primary"] {{
        background-color: #3366ff !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 1rem;
    }}
    .stDownloadButton > button {{
        background-color: #22bb33;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        margin-top: 10px;
        padding: 8px 16px;
    }}
    .stSlider .css-1y4p8pa-efpxz3 {{
        background-color: red !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background
set_background("assets/background.png")

# UI
st.title("🎬 101VideoGenerator App 1.0")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Duration (seconds)", 10, 120, 30)
clips = st.slider("Number of clips", 1, 10, 5)
aspect = st.selectbox("Aspect Ratio", ["16:9", "1:1", "9:16"])

if st.button("Generate Video"):
    with st.spinner("Generating..."):
        output = make_video(topic, duration, clips, aspect)
    if output:
        st.success("Video created successfully!")
        st.video(output)
        with open(output, "rb") as f:
            st.download_button("📥 Download Video", f, file_name="highlight.mp4", mime="video/mp4")
    else:
        st.error("Failed to create video. Try a different topic.")
