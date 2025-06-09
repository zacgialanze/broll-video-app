import streamlit as st
from broll_stitcher_core import make_video
import base64

st.set_page_config(
    page_title="101VideoGenerator App 1.0",
    page_icon="🎬",
    layout="centered"
)

# Inject custom CSS to set the background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div,
    .stSlider > div {{
        background-color: rgba(255,255,255,0.8);
        border-radius: 5px;
        padding: 5px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("assets/background.png")

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
