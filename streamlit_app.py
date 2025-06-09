
import streamlit as st
from broll_stitcher_core import make_video

st.set_page_config(page_title="101VideoGenerator App 1.0", layout="centered")
st.markdown("""
<style>
body {
    background-color: #0d1b2a;
    color: #ffffff;
}
h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 36px;
    color: #fca311;
    text-align: center;
}
.stTextInput>div>div>input {
    background-color: #1b263b;
    color: white;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
}
.stSlider {
    background-color: #1b263b;
    padding: 10px;
    border-radius: 10px;
}
.stSelectbox>div>div {
    background-color: #1b263b;
    color: white;
    border-radius: 10px;
    padding: 10px;
}
.stButton>button {
    background-color: #fca311;
    color: #14213d;
    border: none;
    padding: 10px 24px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
}
.stButton>button:hover {
    background-color: #ffba08;
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 101VideoGenerator App 1.0")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Total duration (seconds)", 10, 120, 30)
clips = st.slider("Number of clips", 1, 10, 5)
aspect = st.selectbox("Aspect Ratio", ["16:9", "1:1", "9:16"])

if st.button("🎬 Generate Video"):
    with st.spinner("Generating your masterpiece..."):
        output = make_video(topic, duration, clips, aspect)
    if output:
        st.success("✅ Video created successfully!")
        st.video(output)
        with open(output, "rb") as f:
            st.download_button("📥 Download Video", f, file_name="highlight.mp4", mime="video/mp4")
    else:
        st.error("❌ Failed to create video. Try a different topic.")
