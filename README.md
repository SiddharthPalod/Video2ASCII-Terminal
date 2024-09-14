# Video2ASCII Terminal

This Python script converts video frames into ASCII art and plays them directly in the terminal. It supports both local video files and YouTube videos, offering a unique way to experience video content.

## Features

- Converts video frames to ASCII art for terminal playback.
- Supports downloading and playing YouTube videos.
- Works with local video files as well.
- Simple terminal-based playback interface.
- Compatible with both Windows and Linux systems.

## Requirements

The following Python packages are required to run this script:

- `opencv-python`: For handling video files and extracting frames.
- `Pillow`: For image processing and resizing.
- `yt-dlp`: For downloading YouTube videos.

You can install these dependencies by running:

```bash
pip install opencv-python Pillow yt-dlp
    ```
## How It Works

1. **Download YouTube Videos (optional)**: If a YouTube URL is provided, the video is downloaded using `yt-dlp`.
2. **Frame Extraction**: Video frames are extracted using OpenCV and converted to grayscale.
3. **ASCII Conversion**: Each grayscale frame is converted into ASCII art using a set of characters.
4. **Playback**: The frames are displayed in sequence in the terminal, simulating video playback.

## Usage

1. Clone this repository or download the script file.

2. Install the required dependencies:

    ```bash
    pip install opencv-python Pillow yt-dlp
    ```

3. Run the script:

    ```bash
    python video_to_ascii.py
    ```

4. Enter the YouTube video URL or the local file path when prompted.

    Example:

    ```css
    Enter the video URL or path to the video file (or type 'exit' to quit): https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```

5. The video will start playing as ASCII art in your terminal. To stop the playback, press `Ctrl+C`.

## Customization

- **Output Width**: The default output width for ASCII frames is set to 100 characters. You can modify the `output_width` argument in the `frame_to_ascii` function to adjust this.
- **Character Set**: The ASCII characters used for the conversion can be customized by modifying the `chars` string.

## Acknowledgements

- [OpenCV](https://opencv.org/) for video frame handling.
- [Pillow](https://python-pillow.org/) for image manipulation.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube video downloads.
