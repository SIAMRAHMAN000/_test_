from pytube import YouTube
import cv2
from moviepy.editor import *
from pyyoutube import Api

# Step 1: Download YouTube video
url = "https://www.youtube.com/watch?v=jzvOZm-Rs1A"
yt = YouTube(url)
yt.streams.filter(only_video=True, file_extension='mp4').first().download()
downloaded_video_path = yt.streams[0].default_filename

# Step 2: Edit and enhance the video
video = VideoFileClip(downloaded_video_path)
txt_clip = (TextClip("Hello, YouTube!", fontsize=50, color='white')
            .set_position('center')
            .set_duration(video.duration))
final_video = CompositeVideoClip([video, txt_clip])
edited_video_path = "edited_short.mp4"
final_video.write_videofile(edited_video_path, codec='libx264')

# Step 3: Upload the Short to YouTube
api_key = "AIzaSyBw2LFLOZmCRsZSYiKDOsE2kpU8hH0Vnqc"
api = Api(api_key=api_key)

# Set the video details
video_title = "My AI-generated YouTube Short"
video_description = "Check out this AI-generated YouTube Short!"
video_tags = ["AI", "YouTube Shorts", "Python"]
video_category_id = 22  # Short Movies category (adjust as needed)

# Upload the video
upload_response = api.upload_video(edited_video_path, video_title, video_description, tags=video_tags, category_id=video_category_id)

# Print the upload response
print("Video uploaded successfully!")
print("Video ID:", upload_response["id"])
print("Video URL:", f"https://www.youtube.com/watch?v={upload_response['id']}")
