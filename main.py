from broll_stitcher_core import make_video

topic = input("Enter video topic: ")
duration = int(input("Total video duration in seconds: "))
clips = int(input("Number of clips: "))
aspect = "16:9"

output = make_video(topic, duration, clips, aspect)
if output:
    print(f"\n✅ Done! Output saved at: {output}")
else:
    print("\n❌ Failed to create video.")
