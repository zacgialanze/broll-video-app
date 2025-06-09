import streamlit as st
from broll_stitcher_core import make_video
import base64
import time

st.set_page_config(page_title="101VideoGenerator App 1.0", layout="centered")

# --- Load and encode images & sound ---
with open("static/background.png", "rb") as bg:
    bg_encoded = base64.b64encode(bg.read()).decode()

with open("static/bike_rider.png", "rb") as bike:
    bike_encoded = base64.b64encode(bike.read()).decode()

with open("static/spark_trail.png", "rb") as spark:
    spark_encoded = base64.b64encode(spark.read()).decode()

with open("static/bike_loop.mp3", "rb") as audio:
    audio_encoded = base64.b64encode(audio.read()).decode()

# --- Inject CSS + JS for animation ---
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
        bottom: 40px;
        left: -300px;
        z-index: 9999;
        animation: ride 5s linear infinite;
    }}

    .spark-trail {{
        position: fixed;
        bottom: 35px;
        left: -320px;
        z-index: 9998;
        animation: ride 5s linear infinite;
    }}

    .spark-trail img {{
        height: 40px;
        opacity: 0.85;
        animation: flicker 0.15s infinite alternate;
    }}

    @keyframes ride {{
        0% {{ left: -320px; }}
        100% {{ left: 110%; }}
    }}

    @keyframes flicker {{
        0% {{ transform: scale(1); opacity: 0.6; }}
        100% {{ transform: scale(1.2); opacity: 1; }}
    }}

    .generating-text {{
        position: fixed;
        bottom: 10px;
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
    </style>
""", unsafe_allow_html=True)

# --- UI ---
st.title("🎬 101VideoGenerator App 1.0")

topic = st.text_input("Enter topic", "fish")
duration = st.slider("Total duration (seconds)", 10, 1000, 30)
clips = st.slider("Number of clips", 1, 100, 5)
aspect = st.selectbox("Aspect ratio", ["16:9", "1:1", "9:16"])

if st.button("Generate Video"):
    # Inject animation, spark, and sound
    st.markdown(f"""
        <div class="bike-animation">
            <img src="data:image/png;base64,{bike_encoded}" height="110">
        </div>
        <div class="spark-trail">
            <img src="data:image/png;base64,{spark_encoded}">
        </div>
        <div class="generating-text">Generating...</div>
        <audio id="bike-audio" autoplay loop>
            <source src="data:audio/mp3;base64,{audio_encoded}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

    with st.spinner("Generating..."):
        time.sleep(1.5)
        output = make_video(topic, duration, clips, aspect)

    # Kill audio + visuals
    st.markdown("""
        <script>
            const audio = document.getElementById('bike-audio');
            if (audio) audio.pause();
        </script>
        <style>
            .bike-animation, .spark-trail, .generating-text { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

    if output:
        st.success("✅ Video created successfully!")
        st.video(output)
        with open(output, "rb") as f:
            st.download_button("📥 Download Video", f, file_name="highlight.mp4", mime="video/mp4")
    else:
        st.error("❌ Failed to create video. Try a different topic.")
