"""Kling 4.0 — text-to-video with `kwaivgi/kling-v4.0/text-to-video`.

export WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey
"""
import kling_api

urls = kling_api.text_to_video(
    prompt="A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement",
)
print(urls[0])
