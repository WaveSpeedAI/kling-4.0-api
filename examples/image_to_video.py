"""Kling 4.0 — image-to-video with `kwaivgi/kling-v4.0/image-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import kling_api

urls = kling_api.image_to_video(
    image="https://example.com/your-image.jpg",
)
print(urls[0])
