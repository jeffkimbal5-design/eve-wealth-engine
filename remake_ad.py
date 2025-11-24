import PIL.Image
# === MONKEY PATCH: Fix missing ANTIALIAS ===
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
# ===========================================

import os
import glob
from moviepy.editor import *
from moviepy.config import change_settings

print(">>> EVE_PRIME: INITIALIZING REMASTERING SEQUENCE...")

# === 1. SMART ASSET LOADER ===
video_files = sorted(glob.glob("assets/*.mp4"))
image_files = sorted(glob.glob("assets/*.jpg") + glob.glob("assets/*.png"))

if not video_files:
    print("!!! ERROR: NO VIDEOS FOUND IN 'assets' FOLDER !!!")
    exit()

# Helpers to grab assets safely
def get_vid(i): return VideoFileClip(video_files[i % len(video_files)])
def get_img(i): return ImageClip(image_files[i % len(image_files)])

def safe_cut(clip, start, duration):
    # Cuts video without crashing if it's too short
    if clip.duration < start: start = 0
    end = min(start + duration, clip.duration)
    return clip.subclip(start, end).resize(height=720)

# Helper to add text
def add_text(clip, text, size=50, duration=None):
    if duration is None: duration = clip.duration
    # Generate text
    try:
        txt = TextClip(text, fontsize=size, color='white', font='Courier-Bold', 
                       stroke_color='black', stroke_width=2, method='caption', size=(1000, None))
        txt = txt.set_pos(('center', 'bottom')).set_duration(duration)
        return CompositeVideoClip([clip, txt])
    except Exception as e:
        print(f"!!! TEXT ERROR: {e}")
        return clip # Return video without text if font fails

# === 2. BUILD THE TIMELINE (TYPOS FIXED) ===
clips = []

print(">>> PROCESSING ACT 1: THE LOOP...")
# 0:00 Intro
v1 = safe_cut(get_vid(0), 0, 8)
t1 = "EVE-PRIME PROTOCOL\nUnlock Your Potential\nBio-Hacking Secrets Revealed"
clips.append(add_text(v1, t1))

# 0:08 Waking Up
v2 = safe_cut(get_vid(1), 0, 9)
t2 = "You didn't forget.\nYour system just failed you."
clips.append(add_text(v2, t2))

# 0:17 Desk
v3 = safe_cut(get_vid(2), 0, 8)
t3 = "This app was built for a full brain.\nFrom Chaos..."
clips.append(add_text(v3, t3))

# 0:25 App Store
v4 = safe_cut(get_vid(0), 10, 5) 
t4 = "App-Store   |   Google Play\nSTOP THE LOOP"
clips.append(add_text(v4, t4, size=60))

print(">>> PROCESSING ACT 2: THE AWAKENING...")
# 0:30 Book Image
img1 = get_img(0).set_duration(8).resize(height=720)
t5 = "They told you circumstances define destiny.\nThe truth is, they don't."
clips.append(add_text(img1, t5, size=40))

# 0:38 Jeffrey Image
img2 = get_img(1).set_duration(7).resize(height=720)
t6 = "What didn't break you...\nMade you unbreakable."
clips.append(add_text(img2, t6))

print(">>> PROCESSING ACT 3: BROKEN ACCESS...")
# 0:45 AI Tunnel
v7 = safe_cut(get_vid(3), 0, 10)
clips.append(add_text(v7, "BROKEN ACCESS CONTROL", size=70).set_pos('center'))

# 0:55 UI Interaction
v8 = safe_cut(get_vid(4), 0, 10)
clips.append(add_text(v8, "I learned its validity and plasticity."))

# 1:05 Logo
img3 = get_img(2).set_duration(5).resize(height=720)
clips.append(add_text(img3, "Designed for Modern Minds."))

print(">>> PROCESSING ACT 4: NEW REALITY...")
# 1:10 Voice Memo
v10 = safe_cut(get_vid(5), 0, 15)
clips.append(add_text(v10, "TRANSCRIPTION: Reschedule Investor Call..."))

# 1:25 EVE_1 Brain
v11 = safe_cut(get_vid(6), 0, 15)
clips.append(add_text(v11, "Introducing EVE_1\nYour AI-Powered Investment Partner"))

# 1:40 Yoga & Dance
clips.append(safe_cut(get_vid(7), 0, 7))
clips.append(safe_cut(get_vid(8), 0, 8))

print(">>> PROCESSING ACT 5: THE LEGACY...")
# 2:00 Drone
v14 = safe_cut(get_vid(-1), 0, 10)
clips.append(add_text(v14, "This is my GENESIS."))

# 2:10 The Code
v15 = safe_cut(get_vid(3), 5, 15).fx(vfx.speedx, 2)
clips.append(add_text(v15, "EVE IS THE CONSEQUENCE.\nSECURE YOUR SAFETY."))

# 2:25 Final QR Code
img_qr = get_img(-1).set_duration(6).resize(height=720)
clips.append(add_text(img_qr, "SCAN TO ACTIVATE", size=80))

# === 3. RENDER ===
print(">>> COMPILING REMASTERED VIDEO...")
final_video = concatenate_videoclips(clips, method="compose")
final_video.write_videofile("EVE_COMMERCIAL_CLEAN.mp4", fps=24, preset='ultrafast', threads=4)
