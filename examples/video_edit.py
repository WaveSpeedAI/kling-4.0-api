"""Kling 4.0 — video-to-video with `kwaivgi/kling-v4.0/video-edit`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import kling_api

urls = kling_api.video_edit(
    prompt="Describe the result you want",
    video="https://example.com/your-video.mp4",
)
print(urls[0])
