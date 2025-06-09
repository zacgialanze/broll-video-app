import streamlit as st
from broll_stitcher_core import make_video
import base64

st.set_page_config(page_title="101VideoGenerator App 1.0", layout="centered")

# --- Load and encode background image from static folder ---
with open("static/background.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

# --- Inject CSS with left-positioned, zoomed-out image ---
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: 80%;
        background-position: left center;
        background-repeat: no-repeat;
    }}

    .stApp {{
        background: transparent;
    }}

    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem 3rem;
        border-radius: 1rem;
        max-width: 650px;
        margin: 6vh auto;
        color: white;
    }}

    h1 {{
        font-size: 2.7rem;
        text-align: center;
        color: white;
        margin-bottom: 1.5rem;
    }}

    label, .stTextInput label, .stSelectbox label {{
        font-weight: bold;
        color: white !important;
        opacity: 1 !important;
    }}

    .stSlider label, .stSlider span {{
        color: white !important;
        opacity: 1 !important;
        font-weight: bold;
    }}

    .stButton>button {{
        background-color: #ff8000;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
    }}

    .stButton>button:hover {{
        background-color: #ffa733;
    }}

    .stDownloadButton>button {{
        margin-top: 1rem;
        background-color: #00b7ff;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
    }}
    </style>
""", unsafe_allow_html=True)

# --- UI ---
st.title("🎬 101VideoGenerator App 1.0")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Total duration (seconds)", 10, 1000, 30)
clips = st.slider("Number of clips", 1, 100, 5)
aspect = st.selectbox("Aspect ratio", ["16:9", "1:1", "9:16"])

if st.button("Generate Video"):
    with st.spinner("Generating..."):
        output = make_video(topic, duration, clips, aspect)
    if output:
        st.success("✅ Video created successfully!")
        st.video(output)
        with open(output, "rb") as f:
            st.download_button("📥 Download Video", f, file_name="highlight.mp4", mime="video/mp4")
    else:
        st.error("❌ Failed to create video. Try a different topic.")
