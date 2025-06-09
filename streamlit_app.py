import streamlit as st
from broll_stitcher_core import make_video
import base64
import time

st.set_page_config(page_title="101VideoGenerator App 1.0", layout="centered")

# --- Load and encode background and rider image ---
with open("static/background.png", "rb") as bg:
    bg_encoded = base64.b64encode(bg.read()).decode()

with open("static/bike_rider.png", "rb") as bike:
    bike_encoded = base64.b64encode(bike.read()).decode()

# --- Inject custom CSS ---
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{bg_encoded}");
        background-size: cover;
        background-position: center 35%;
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

    .bike-animation {{
        position: fixed;
        bottom: 100px;
        left: -200px;
        z-index: 9999;
        animation: ride 4s linear infinite;
    }}

    @keyframes ride {{
        0% {{ left: -200px; }}
        100% {{ left: 110%; }}
    }}

    .generating-text {{
        position: fixed;
        bottom: 60px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
        z-index: 9999;
        animation: pulse 1.5s ease-in-out infinite;
    }}

    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.3; }}
    }}

    .stSpinner {{
        visibility: hidden;
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
    # Show the animated biker + text manually before running the spinner
    st.markdown(f"""
        <div class="bike-animation">
            <img src="data:image/png;base64,{bike_encoded}" height="80">
        </div>
        <div class="generating-text">Generating...</div>
    """, unsafe_allow_html=True)

    with st.spinner("Generating..."):
        time.sleep(1.5)  # short delay to let animation appear
        output = make_video(topic, duration, clips, aspect)

    st.markdown(
        """<style>.bike-animation, .generating-text { display: none !important; }</style>""",
        unsafe_allow_html=True
    )

    if output:
        st.success("✅ Video created successfully!")
        st.video(output)
        with open(output, "rb") as f:
            st.download_button("📥 Download Video", f, file_name="highlight.mp4", mime="video/mp4")
    else:
        st.error("❌ Failed to create video. Try a different topic.")
