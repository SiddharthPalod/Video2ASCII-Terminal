import cv2
from PIL import Image
import os
import time
import yt_dlp

def frame_to_ascii(image, output_width=100):
    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))    # Convert to grayscale
    
    # Calculate new height maintaining aspect ratio and reduce height further to match terminal proportions
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio * 0.55)  # Adjust the scaling factor as needed
    
    img = img.resize((output_width, new_height))    
    chars = " &@#%$*o!;:,. "
    num_chars = len(chars)
    
    pixels = img.getdata()
    ascii_str = ''.join(chars[pixel * (num_chars - 1) // 255] for pixel in pixels)  # Properly map pixel values to chars
    ascii_str = [ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)]  # Format the ASCII string into lines of width output_width
    return "\n".join(ascii_str)

def download_youtube_video(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'downloaded_video.mp4',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'downloaded_video.mp4'

def video_to_ascii(video_url):
    if os.path.exists('downloaded_video.mp4'):
        os.remove('downloaded_video.mp4')

    if video_url.startswith('http://') or video_url.startswith('https://'):    # Download the video if it's a URL
        video_path = download_youtube_video(video_url)
    else:
        video_path = video_url

    cap = cv2.VideoCapture(video_path) # Open video file    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)    # Get frame rate
    frame_time = 1 / fps

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            ascii_frame = frame_to_ascii(frame)
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal and print ASCII frame
            print(ascii_frame)            
            time.sleep(frame_time)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("Video playback stopped.")

if __name__ == "__main__":
    while True:
        user_input = input("Enter the video URL or path to the video file (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        video_to_ascii(user_input)
