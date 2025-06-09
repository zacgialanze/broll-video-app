import streamlit as st
from broll_stitcher_core import make_video

st.title("🎬 B-Roll Video Generator")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Total duration (seconds)", 10, 120, 30)
clips = st.slider("Number of clips", 1, 10, 5)
aspect = st.selectbox("Aspect ratio", ["16:9", "1:1", "9:16"])

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

