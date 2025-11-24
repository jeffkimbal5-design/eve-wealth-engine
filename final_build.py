import PIL.Image
# === MONKEY PATCH: Fix missing ANTIALIAS ===
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
# ===========================================

import os
import glob
import PIL.Image
# === MONKEY PATCH: Fix missing ANTIALIAS ===
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
# ===========================================

import os
import glob
from moviepy.editor import *

print(">>> EVE_PRIME: INITIALIZING SAFE MODE RENDER (720p)...")

# 1. Grab all video and image files
video_files = sorted(glob.glob("assets/*.mp4"))
image_files = sorted(glob.glob("assets/*.jpg") + glob.glob("assets/*.png"))

if not video_files:
    print("!!! ERROR: NO VIDEOS FOUND !!!")
    exit()

# 2. Helper to safely cut videos (Downgraded to 720p for stability)
def safe_subclip(video_path, start_time, duration, target_height=720):
    clip = VideoFileClip(video_path)
    
    if clip.duration < start_time:
        start_time = 0
        
    end_time = min(start_time + duration, clip.duration)
    
    if end_time - start_time < 1:
        start_time = 0
        end_time = clip.duration

    # Resize to 720p to save RAM
    return clip.subclip(start_time, end_time).resize(height=target_height)

# 3. Looping generators
def get_video(index):
    return video_files[index % len(video_files)]

def get_image(index):
    if not image_files:
        return video_files[0]
    return image_files[index % len(image_files)]

# 4. Construct the Timeline
print(">>> ASSEMBLING TIMELINE...")

clips = []
H = 720 # Target Height

# ACT 1
clips.append(safe_subclip(get_video(0), 0, 8))
clips.append(safe_subclip(get_video(1), 0, 9))
clips.append(safe_subclip(get_video(2), 0, 8))
clips.append(safe_subclip(get_video(0), 0, 5))

# ACT 2
clips.append(ImageClip(get_image(0)).set_duration(8).resize(height=H))
clips.append(ImageClip(get_image(1)).set_duration(7).resize(height=H))

# ACT 3
clips.append(safe_subclip(get_video(3), 0, 10))
clips.append(safe_subclip(get_video(4), 0, 10))
clips.append(ImageClip(get_image(2)).set_duration(5).resize(height=H))

# ACT 4
clips.append(safe_subclip(get_video(5), 0, 15))
clips.append(safe_subclip(get_video(6), 0, 20))
clips.append(safe_subclip(get_video(7), 0, 7))
clips.append(safe_subclip(get_video(8), 0, 8))

# ACT 5
clips.append(safe_subclip(video_files[-1], 0, 10))
try:
    # Speed effect can be heavy, simplified here
    tunnel_clip = safe_subclip(get_video(3), 0, 10).fx(vfx.speedx, 2)
    clips.append(tunnel_clip)
except:
    clips.append(safe_subclip(get_video(3), 0, 5))

clips.append(ImageClip(image_files[-1]).set_duration(5).resize(height=H))

# 5. Render with ULTRAFAST preset to prevent crashing
final_video = concatenate_videoclips(clips, method="compose")

print(">>> RENDER INITIATED. STAND BY...")
# 'preset' speeds up compression, 'threads' limits memory usage
final_video.write_videofile("EVE_PRIME_FINAL.mp4", fps=24, preset='ultrafast', threads=4)
