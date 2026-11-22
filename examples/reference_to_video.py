"""Kling 4.0 — reference-to-video with `kwaivgi/kling-v4.0/reference-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import kling_api

urls = kling_api.reference_to_video(
    prompt="Describe the result you want",
)
print(urls[0])
