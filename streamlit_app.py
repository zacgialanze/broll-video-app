import streamlit as st
from broll_stitcher_core import make_video

st.set_page_config(page_title="101VideoGenerator App 1.0", layout="centered")

# Custom background CSS
st.markdown("""
    <style>
    body {
        background-image: url("assets/background.png");
        background-size: cover;
        background-position: center;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
        max-width: 700px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    label, .stTextInput label, .stSelectbox label {
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 101VideoGenerator App 1.0")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Total duration (seconds)", 10, 120, 30)
clips = st.slider("Number of clips", 1, 10, 5)
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
