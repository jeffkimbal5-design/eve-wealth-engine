import os
import glob
from moviepy.editor import *

print(">>> EVE_PRIME: SCANNING ASSETS...")

# 1. Grab all video and image files in the assets folder
video_files = sorted(glob.glob("assets/*.mp4"))
image_files = sorted(glob.glob("assets/*.jpg") + glob.glob("assets/*.png"))

print(f">>> FOUND {len(video_files)} VIDEOS and {len(image_files)} IMAGES.")

if not video_files:
    print("!!! ERROR: NO VIDEOS FOUND IN 'assets' FOLDER !!!")
    exit()

# 2. Create a looping generator to avoid running out of files
def get_video(index):
    return video_files[index % len(video_files)]

def get_image(index):
    if not image_files:
        return video_files[0] # Fallback
    return image_files[index % len(image_files)]

# 3. Construct the Timeline
print(">>> ASSEMBLING TIMELINE...")

clips = []

# ACT 1: THE LOOP
clips.append(VideoFileClip(get_video(0)).subclip(0, 8).resize(height=1080))
clips.append(VideoFileClip(get_video(1)).subclip(0, 9).resize(height=1080))
clips.append(VideoFileClip(get_video(2)).subclip(0, 8).resize(height=1080))
clips.append(VideoFileClip(get_video(0)).subclip(10, 15).resize(height=1080))

# ACT 2: AWAKENING
clips.append(ImageClip(get_image(0)).set_duration(8).resize(height=1080))
clips.append(ImageClip(get_image(1)).set_duration(7).resize(height=1080))

# ACT 3: BROKEN ACCESS
clips.append(VideoFileClip(get_video(3)).subclip(0, 10).resize(height=1080))
clips.append(VideoFileClip(get_video(4)).subclip(0, 10).resize(height=1080))
clips.append(ImageClip(get_image(2)).set_duration(5).resize(height=1080))

# ACT 4: NEW REALITY
clips.append(VideoFileClip(get_video(5)).subclip(0, 15).resize(height=1080))
clips.append(VideoFileClip(get_video(6)).subclip(0, 20).resize(height=1080))
clips.append(VideoFileClip(get_video(7)).subclip(0, 7).resize(height=1080))
clips.append(VideoFileClip(get_video(8)).subclip(0, 8).resize(height=1080))

# ACT 5: LEGACY
clips.append(VideoFileClip(video_files[-1]).subclip(0, 10).resize(height=1080))
clips.append(VideoFileClip(get_video(3)).subclip(5, 20).resize(height=1080).fx(vfx.speedx, 2))
clips.append(ImageClip(image_files[-1]).set_duration(5).resize(height=1080))

# 4. Render
final_video = concatenate_videoclips(clips, method="compose")

print(">>> RENDER INITIATED. PLEASE WAIT...")
final_video.write_videofile("EVE_PRIME_FINAL.mp4", fps=24)
