"""Kling 4.0 API — Python wrapper for the WaveSpeedAI hosted endpoints.

Each function calls one endpoint through the official `wavespeed` SDK, waits for
the result and returns the list of output URLs. Arguments left as None are not
sent, so the server-side defaults apply.

Set WAVESPEED_API_KEY first: https://wavespeed.ai/accesskey

Generated from the live model schemas; do not edit by hand.
"""
from typing import Any, Dict, List, Optional

import wavespeed

__version__ = "0.1.0"

__all__ = ["MODELS", "upload", "text_to_video", "image_to_video", "reference_to_video", "video_edit", "video_extend", "flash_text_to_video", "flash_image_to_video", "flash_reference_to_video", "flash_video_edit"]

#: function name -> WaveSpeedAI model id
MODELS: Dict[str, str] = {
    "text_to_video": "kwaivgi/kling-v4.0/text-to-video",
    "image_to_video": "kwaivgi/kling-v4.0/image-to-video",
    "reference_to_video": "kwaivgi/kling-v4.0/reference-to-video",
    "video_edit": "kwaivgi/kling-v4.0/video-edit",
    "video_extend": "kwaivgi/kling-v4.0/video-extend",
    "flash_text_to_video": "kwaivgi/kling-v4.0-flash/text-to-video",
    "flash_image_to_video": "kwaivgi/kling-v4.0-flash/image-to-video",
    "flash_reference_to_video": "kwaivgi/kling-v4.0-flash/reference-to-video",
    "flash_video_edit": "kwaivgi/kling-v4.0-flash/video-edit",
}


def upload(file: Any) -> str:
    """Upload a local file (path or binary file object) and return its URL."""
    return wavespeed.upload(file)


def _run(name: str, params: Dict[str, Any], timeout: Optional[float], poll_interval: float) -> List[str]:
    payload = {k: v for k, v in params.items() if v is not None}
    result = wavespeed.run(MODELS[name], payload, timeout=timeout, poll_interval=poll_interval)
    return list(result["outputs"])


def text_to_video(
    prompt: str,
    *,
    resolution: Optional[str] = None,
    dynamic_range: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Text-to-Video generates cinematic clips of 3 to 30 seconds from a text prompt, with 720p, 1080p and 4K output, four aspect ratios including 21:9 ultrawide, and synchronized stereo audio.

    Model: ``kwaivgi/kling-v4.0/text-to-video``

    Args:
        prompt: The positive prompt for the generation.
        resolution: Output resolution: 720p, 1080p or 4k (native 3840x2160). Allowed: 720p, 1080p, 4k. Server default: "720p".
        dynamic_range: Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. Allowed: sdr, hdr. Server default: "sdr".
        duration: The duration of the generated video in seconds (3-30). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video. Allowed: 16:9, 9:16, 1:1, 21:9. Server default: "16:9".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "text_to_video",
        {"prompt": prompt, "resolution": resolution, "dynamic_range": dynamic_range, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def image_to_video(
    image: str,
    *,
    prompt: Optional[str] = None,
    last_image: Optional[str] = None,
    keyframes: Optional[List[str]] = None,
    resolution: Optional[str] = None,
    dynamic_range: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Image-to-Video animates a first frame into a clip of 3 to 30 seconds, with an optional last frame and up to 8 in-between keyframes to direct the story, 720p, 1080p and 4K output and synchronized stereo audio.

    Model: ``kwaivgi/kling-v4.0/image-to-video``

    Args:
        image: First frame image URL. Supported formats: .jpg/.jpeg/.png.
        prompt: Text prompt describing the motion (may be empty).
        last_image: Last frame image URL. Requires image.
        keyframes: Middle frames in order (image, last_image and keyframes together are at most 10). Requires image. Allowed: up to 9 items.
        resolution: Output resolution: 720p, 1080p or 4k (native 3840x2160). Allowed: 720p, 1080p, 4k. Server default: "720p".
        dynamic_range: Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. Allowed: sdr, hdr. Server default: "sdr".
        duration: The duration of the generated video in seconds (3-30). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video. Leave it out to follow the first frame. Allowed: 16:9, 9:16, 1:1, 21:9.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "image_to_video",
        {"image": image, "prompt": prompt, "last_image": last_image, "keyframes": keyframes, "resolution": resolution, "dynamic_range": dynamic_range, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def reference_to_video(
    prompt: str,
    *,
    images: Optional[List[str]] = None,
    videos: Optional[List[str]] = None,
    audios: Optional[List[str]] = None,
    keep_original_sound: Optional[bool] = None,
    resolution: Optional[str] = None,
    dynamic_range: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Reference-to-Video builds a new clip of 3 to 30 seconds from up to 10 reference images, 5 reference videos and 3 reference audios, following the subjects, motion and camera you point to in the prompt, with 720p, 1080p and 4K output and synchronized stereo audio.

    Model: ``kwaivgi/kling-v4.0/reference-to-video``

    Args:
        prompt: The positive prompt for the generation. Refer to reference images as @Image1, @Image2, ... (in array order), to reference videos as @Video1, @Video2, ... and to reference audios as @Audio1, @Audio2, ...
        images: Reference images (up to 10). Allowed: up to 10 items.
        videos: Reference videos (up to 5). They guide motion, camera and pacing; together they are used for up to 30 seconds. Allowed: up to 5 items.
        audios: Reference audios (up to 3), 5-30 seconds each. They guide the voice and sound of the video. Allowed: up to 3 items.
        keep_original_sound: Keep the reference video's own sound instead of generating new audio. Requires videos. Server default: false.
        resolution: Output resolution: 720p, 1080p or 4k (native 3840x2160). Allowed: 720p, 1080p, 4k. Server default: "720p".
        dynamic_range: Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. Allowed: sdr, hdr. Server default: "sdr".
        duration: The duration of the generated video in seconds (3-30). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video; auto follows the reference images or video. Allowed: auto, 16:9, 9:16, 1:1, 21:9. Server default: "auto".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "reference_to_video",
        {"prompt": prompt, "images": images, "videos": videos, "audios": audios, "keep_original_sound": keep_original_sound, "resolution": resolution, "dynamic_range": dynamic_range, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def video_edit(
    prompt: str,
    video: str,
    *,
    images: Optional[List[str]] = None,
    audios: Optional[List[str]] = None,
    keep_original_sound: Optional[bool] = None,
    resolution: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Video Edit rewrites a 3 to 30 second video from a text instruction: it keeps the scene, subject and motion and changes what you describe, with optional reference images and audios, 720p, 1080p and 4K output and new synchronized audio generated by default (the original sound can be kept instead).

    Model: ``kwaivgi/kling-v4.0/video-edit``

    Args:
        prompt: Describe the edit you want applied to the video - change a subject, the setting, the weather or the style. Refer to the video as @Video1, to reference images as @Image1, @Image2, ... and to reference audios as @Audio1, @Audio2, ... in array order.
        video: URL of the video to edit. The edit keeps its scene, subject and motion; 3-30 seconds, longer videos are trimmed to 30 seconds.
        images: Optional reference images (up to 10) for a subject, object or style to bring into the edit. Allowed: up to 10 items.
        audios: Reference audios (up to 3), 5-30 seconds each. They guide the voice and sound of the video. Allowed: up to 3 items.
        keep_original_sound: Keep the input video's own sound instead of generating new synchronized audio. Server default: false.
        resolution: Output resolution: 720p, 1080p or 4k (native 3840x2160). Allowed: 720p, 1080p, 4k. Server default: "720p".
        duration: Output duration in seconds (3-30). Follows the input video's length if not specified. Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.
        aspect_ratio: Aspect ratio of the output video. Follows the input video if not specified. Allowed: 16:9, 9:16, 1:1, 21:9.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "video_edit",
        {"prompt": prompt, "video": video, "images": images, "audios": audios, "keep_original_sound": keep_original_sound, "resolution": resolution, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def video_extend(
    prompt: str,
    video: str,
    *,
    last_image: Optional[str] = None,
    resolution: Optional[str] = None,
    duration: Optional[int] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Video Extend continues a video from its last frame with a new 3 to 30 second segment guided by your prompt, at 720p, 1080p or 4K with synchronized stereo audio, and returns the original and the new segment joined.

    Model: ``kwaivgi/kling-v4.0/video-extend``

    Args:
        prompt: Describe the continuation - action, camera movement, lighting and sound. Audio is generated together with the picture.
        video: URL of the video to extend. The new segment is generated from its last frame and appended to the original.
        last_image: Optional target last-frame image URL. When provided, the new segment interpolates from the input video's last frame to this image.
        resolution: Output resolution: 720p, 1080p or 4k (native 3840x2160). Allowed: 720p, 1080p, 4k. Server default: "720p".
        duration: Length in seconds of the new segment to append (3-30). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30. Server default: 5.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "video_extend",
        {"prompt": prompt, "video": video, "last_image": last_image, "resolution": resolution, "duration": duration},
        timeout,
        poll_interval,
    )


def flash_text_to_video(
    prompt: str,
    *,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Flash Text-to-Video generates 3 to 20 second 720p clips from a text prompt with synchronized audio, in four aspect ratios including 21:9 ultrawide; Flash is the fast, lower-cost tier of Kling 4.0 for quick iteration.

    Model: ``kwaivgi/kling-v4.0-flash/text-to-video``

    Args:
        prompt: The positive prompt for the generation.
        duration: The duration of the generated video in seconds (3-20). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video. Allowed: 16:9, 9:16, 1:1, 21:9. Server default: "16:9".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "flash_text_to_video",
        {"prompt": prompt, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def flash_image_to_video(
    image: str,
    *,
    prompt: Optional[str] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Flash Image-to-Video animates a first-frame image into a 3 to 20 second 720p clip with synchronized audio; Flash is the fast, lower-cost tier of Kling 4.0 for quick iteration.

    Model: ``kwaivgi/kling-v4.0-flash/image-to-video``

    Args:
        image: First frame image URL. Supported formats: .jpg/.jpeg/.png.
        prompt: Text prompt describing the motion (may be empty).
        duration: The duration of the generated video in seconds (3-20). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video. Leave it out to follow the first frame. Allowed: 16:9, 9:16, 1:1, 21:9.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "flash_image_to_video",
        {"image": image, "prompt": prompt, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def flash_reference_to_video(
    prompt: str,
    *,
    images: Optional[List[str]] = None,
    videos: Optional[List[str]] = None,
    keep_original_sound: Optional[bool] = None,
    duration: Optional[int] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Flash Reference-to-Video generates a 3 to 20 second 720p clip guided by up to 10 reference images and 5 reference videos, with synchronized audio; Flash is the fast, lower-cost tier of Kling 4.0.

    Model: ``kwaivgi/kling-v4.0-flash/reference-to-video``

    Args:
        prompt: The positive prompt for the generation. Refer to reference images as @Image1, @Image2, ... (in array order) and to reference videos as @Video1, @Video2, ...
        images: Reference images (up to 10). Allowed: up to 10 items.
        videos: Reference videos (up to 5). They guide motion, camera and pacing; together they are used for up to 20 seconds. Allowed: up to 5 items.
        keep_original_sound: Keep the reference video's own sound instead of generating new audio. Requires videos. Server default: false.
        duration: The duration of the generated video in seconds (3-20). Allowed: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. Server default: 5.
        aspect_ratio: The aspect ratio of the generated video; auto follows the reference images or video. Allowed: auto, 16:9, 9:16, 1:1, 21:9. Server default: "auto".
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "flash_reference_to_video",
        {"prompt": prompt, "images": images, "videos": videos, "keep_original_sound": keep_original_sound, "duration": duration, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )


def flash_video_edit(
    prompt: str,
    video: str,
    *,
    images: Optional[List[str]] = None,
    keep_original_sound: Optional[bool] = None,
    aspect_ratio: Optional[str] = None,
    timeout: Optional[float] = None,
    poll_interval: float = 1.0,
) -> List[str]:
    """Kling V4.0 Flash Video Edit rewrites a 3 to 20 second video from a text instruction at 720p: it keeps the scene, subject and motion and changes what you describe, with optional reference images and new synchronized audio by default.

    Model: ``kwaivgi/kling-v4.0-flash/video-edit``

    Args:
        prompt: Describe the edit you want applied to the video - change a subject, the setting, the weather or the style. Refer to reference images as @Image1, @Image2, ... in array order.
        video: URL of the video to edit. The edit keeps its scene, subject and motion; 3-20 seconds, longer videos are trimmed to 20 seconds.
        images: Optional reference images (up to 10) for a subject, object or style to bring into the edit. Allowed: up to 10 items.
        keep_original_sound: Keep the input video's own sound instead of generating new synchronized audio. Server default: false.
        aspect_ratio: Aspect ratio of the output video. Follows the input video if not specified. Allowed: 16:9, 9:16, 1:1, 21:9.
        timeout: Maximum seconds to wait for the result (None = no limit).
        poll_interval: Seconds between status checks.

    Returns:
        List of output URLs.
    """
    return _run(
        "flash_video_edit",
        {"prompt": prompt, "video": video, "images": images, "keep_original_sound": keep_original_sound, "aspect_ratio": aspect_ratio},
        timeout,
        poll_interval,
    )
