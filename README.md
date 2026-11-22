# Kling 4.0 API — Python wrapper

Call **Kling 4.0 and Kling 4.0 Flash** from Python with one function per endpoint: text-to-video, image-to-video, reference-to-video, video editing, video extension. Built on the official [`wavespeed`](https://github.com/WaveSpeedAI/wavespeed-python) SDK and the [WaveSpeedAI](https://wavespeed.ai/?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) hosted API — no GPU, pay per generation.

<p>
  <a href="https://wavespeed.ai/kling-4-api?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api"><img src="https://img.shields.io/badge/Kling_4.0_API-Get_API_key-00E5FF?style=for-the-badge&labelColor=0B0B0F" alt="Kling 4.0 API"></a>
  <a href="https://wavespeed.ai/video-generator?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api"><img src="https://img.shields.io/badge/No_code-Try_in_browser-7C3AED?style=for-the-badge&labelColor=0B0B0F" alt="Try in browser"></a>
</p>

- **Kling 4.0 API guide, live pricing and playground:** [wavespeed.ai/kling-4-api](https://wavespeed.ai/kling-4-api?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api)
- **No code:** generate in the browser with the [AI Video Generator](https://wavespeed.ai/video-generator?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) on WaveSpeedAI

## Quick start

```bash
pip install git+https://github.com/WaveSpeedAI/kling-4.0-api.git
export WAVESPEED_API_KEY="your-api-key"   # https://wavespeed.ai/accesskey
```

```python
import kling_api

urls = kling_api.text_to_video(
    prompt="A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement",
)
print(urls[0])
```

Every function waits for the generation to finish and returns a list of output URLs. Optional arguments you leave out are not sent, so the API defaults apply. Inputs such as images, videos and audio are passed as URLs; use `kling_api.upload("local-file")` to get a URL for a local file.

## Endpoints

| Function | Model | Type |
| - | - | - |
| [`text_to_video()`](#text_to_video) | [kwaivgi/kling-v4.0/text-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0/text-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | text-to-video |
| [`image_to_video()`](#image_to_video) | [kwaivgi/kling-v4.0/image-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0/image-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | image-to-video |
| [`reference_to_video()`](#reference_to_video) | [kwaivgi/kling-v4.0/reference-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0/reference-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | reference-to-video |
| [`video_edit()`](#video_edit) | [kwaivgi/kling-v4.0/video-edit](https://wavespeed.ai/models/kwaivgi/kling-v4.0/video-edit?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | video-to-video |
| [`video_extend()`](#video_extend) | [kwaivgi/kling-v4.0/video-extend](https://wavespeed.ai/models/kwaivgi/kling-v4.0/video-extend?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | video-extend |
| [`flash_text_to_video()`](#flash_text_to_video) | [kwaivgi/kling-v4.0-flash/text-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0-flash/text-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | text-to-video |
| [`flash_image_to_video()`](#flash_image_to_video) | [kwaivgi/kling-v4.0-flash/image-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0-flash/image-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | image-to-video |
| [`flash_reference_to_video()`](#flash_reference_to_video) | [kwaivgi/kling-v4.0-flash/reference-to-video](https://wavespeed.ai/models/kwaivgi/kling-v4.0-flash/reference-to-video?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | reference-to-video |
| [`flash_video_edit()`](#flash_video_edit) | [kwaivgi/kling-v4.0-flash/video-edit](https://wavespeed.ai/models/kwaivgi/kling-v4.0-flash/video-edit?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api) | video-to-video |

Each model page has a playground, live pricing and copy-paste API snippets. Prices are per generation and depend on the settings you choose; check a request before running it with `wavespeed price <model>` from the [CLI](https://github.com/WaveSpeedAI/wavespeed-cli).

## Parameters

### text_to_video

`kwaivgi/kling-v4.0/text-to-video` — Kling V4.0 Text-to-Video generates cinematic clips of 3 to 30 seconds from a text prompt, with 720p, 1080p and 4K output, four aspect ratios including 21:9 ultrawide, and synchronized stereo audio.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. |
| `resolution` | str |  | `"720p"` | `720p`, `1080p`, `4k` | Output resolution: 720p, 1080p or 4k (native 3840x2160). |
| `dynamic_range` | str |  | `"sdr"` | `sdr`, `hdr` | Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | The duration of the generated video in seconds (3-30). |
| `aspect_ratio` | str |  | `"16:9"` | `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video. |

### image_to_video

`kwaivgi/kling-v4.0/image-to-video` — Kling V4.0 Image-to-Video animates a first frame into a clip of 3 to 30 seconds, with an optional last frame and up to 8 in-between keyframes to direct the story, 720p, 1080p and 4K output and synchronized stereo audio.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `image` | str | yes |  |  | First frame image URL. Supported formats: .jpg/.jpeg/.png. |
| `prompt` | str |  |  |  | Text prompt describing the motion (may be empty). |
| `last_image` | str |  |  |  | Last frame image URL. Requires image. |
| `keyframes` | List[str] |  |  | up to 9 items | Middle frames in order (image, last_image and keyframes together are at most 10). Requires image. |
| `resolution` | str |  | `"720p"` | `720p`, `1080p`, `4k` | Output resolution: 720p, 1080p or 4k (native 3840x2160). |
| `dynamic_range` | str |  | `"sdr"` | `sdr`, `hdr` | Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | The duration of the generated video in seconds (3-30). |
| `aspect_ratio` | str |  |  | `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video. Leave it out to follow the first frame. |

### reference_to_video

`kwaivgi/kling-v4.0/reference-to-video` — Kling V4.0 Reference-to-Video builds a new clip of 3 to 30 seconds from up to 10 reference images, 5 reference videos and 3 reference audios, following the subjects, motion and camera you point to in the prompt, with 720p, 1080p and 4K output and synchronized stereo audio.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. Refer to reference images as @Image1, @Image2, ... (in array order), to reference videos as @Video1, @Video2, ... and to reference audios as @Audio1, @Audio2, ... |
| `images` | List[str] |  |  | up to 10 items | Reference images (up to 10). |
| `videos` | List[str] |  |  | up to 5 items | Reference videos (up to 5). They guide motion, camera and pacing; together they are used for up to 30 seconds. |
| `audios` | List[str] |  |  | up to 3 items | Reference audios (up to 3), 5-30 seconds each. They guide the voice and sound of the video. |
| `keep_original_sound` | bool |  | `false` |  | Keep the reference video's own sound instead of generating new audio. Requires videos. |
| `resolution` | str |  | `"720p"` | `720p`, `1080p`, `4k` | Output resolution: 720p, 1080p or 4k (native 3840x2160). |
| `dynamic_range` | str |  | `"sdr"` | `sdr`, `hdr` | Dynamic range. hdr is 10-bit HLG and needs resolution 1080p or 4k; it adds a per-second charge. sdr is standard. |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | The duration of the generated video in seconds (3-30). |
| `aspect_ratio` | str |  | `"auto"` | `auto`, `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video; auto follows the reference images or video. |

### video_edit

`kwaivgi/kling-v4.0/video-edit` — Kling V4.0 Video Edit rewrites a 3 to 30 second video from a text instruction: it keeps the scene, subject and motion and changes what you describe, with optional reference images and audios, 720p, 1080p and 4K output and new synchronized audio generated by default (the original sound can be kept instead).

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Describe the edit you want applied to the video - change a subject, the setting, the weather or the style. Refer to the video as @Video1, to reference images as @Image1, @Image2, ... and to reference audios as @Audio1, @Audio2, ... in array order. |
| `video` | str | yes |  |  | URL of the video to edit. The edit keeps its scene, subject and motion; 3-30 seconds, longer videos are trimmed to 30 seconds. |
| `images` | List[str] |  |  | up to 10 items | Optional reference images (up to 10) for a subject, object or style to bring into the edit. |
| `audios` | List[str] |  |  | up to 3 items | Reference audios (up to 3), 5-30 seconds each. They guide the voice and sound of the video. |
| `keep_original_sound` | bool |  | `false` |  | Keep the input video's own sound instead of generating new synchronized audio. |
| `resolution` | str |  | `"720p"` | `720p`, `1080p`, `4k` | Output resolution: 720p, 1080p or 4k (native 3840x2160). |
| `duration` | int |  |  | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | Output duration in seconds (3-30). Follows the input video's length if not specified. |
| `aspect_ratio` | str |  |  | `16:9`, `9:16`, `1:1`, `21:9` | Aspect ratio of the output video. Follows the input video if not specified. |

### video_extend

`kwaivgi/kling-v4.0/video-extend` — Kling V4.0 Video Extend continues a video from its last frame with a new 3 to 30 second segment guided by your prompt, at 720p, 1080p or 4K with synchronized stereo audio, and returns the original and the new segment joined.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Describe the continuation - action, camera movement, lighting and sound. Audio is generated together with the picture. |
| `video` | str | yes |  |  | URL of the video to extend. The new segment is generated from its last frame and appended to the original. |
| `last_image` | str |  |  |  | Optional target last-frame image URL. When provided, the new segment interpolates from the input video's last frame to this image. |
| `resolution` | str |  | `"720p"` | `720p`, `1080p`, `4k` | Output resolution: 720p, 1080p or 4k (native 3840x2160). |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30` | Length in seconds of the new segment to append (3-30). |

### flash_text_to_video

`kwaivgi/kling-v4.0-flash/text-to-video` — Kling V4.0 Flash Text-to-Video generates 3 to 20 second 720p clips from a text prompt with synchronized audio, in four aspect ratios including 21:9 ultrawide; Flash is the fast, lower-cost tier of Kling 4.0 for quick iteration.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20` | The duration of the generated video in seconds (3-20). |
| `aspect_ratio` | str |  | `"16:9"` | `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video. |

### flash_image_to_video

`kwaivgi/kling-v4.0-flash/image-to-video` — Kling V4.0 Flash Image-to-Video animates a first-frame image into a 3 to 20 second 720p clip with synchronized audio; Flash is the fast, lower-cost tier of Kling 4.0 for quick iteration.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `image` | str | yes |  |  | First frame image URL. Supported formats: .jpg/.jpeg/.png. |
| `prompt` | str |  |  |  | Text prompt describing the motion (may be empty). |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20` | The duration of the generated video in seconds (3-20). |
| `aspect_ratio` | str |  |  | `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video. Leave it out to follow the first frame. |

### flash_reference_to_video

`kwaivgi/kling-v4.0-flash/reference-to-video` — Kling V4.0 Flash Reference-to-Video generates a 3 to 20 second 720p clip guided by up to 10 reference images and 5 reference videos, with synchronized audio; Flash is the fast, lower-cost tier of Kling 4.0.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | The positive prompt for the generation. Refer to reference images as @Image1, @Image2, ... (in array order) and to reference videos as @Video1, @Video2, ... |
| `images` | List[str] |  |  | up to 10 items | Reference images (up to 10). |
| `videos` | List[str] |  |  | up to 5 items | Reference videos (up to 5). They guide motion, camera and pacing; together they are used for up to 20 seconds. |
| `keep_original_sound` | bool |  | `false` |  | Keep the reference video's own sound instead of generating new audio. Requires videos. |
| `duration` | int |  | `5` | `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20` | The duration of the generated video in seconds (3-20). |
| `aspect_ratio` | str |  | `"auto"` | `auto`, `16:9`, `9:16`, `1:1`, `21:9` | The aspect ratio of the generated video; auto follows the reference images or video. |

### flash_video_edit

`kwaivgi/kling-v4.0-flash/video-edit` — Kling V4.0 Flash Video Edit rewrites a 3 to 20 second video from a text instruction at 720p: it keeps the scene, subject and motion and changes what you describe, with optional reference images and new synchronized audio by default.

| Parameter | Type | Required | Default | Allowed | Description |
| - | - | - | - | - | - |
| `prompt` | str | yes |  |  | Describe the edit you want applied to the video - change a subject, the setting, the weather or the style. Refer to reference images as @Image1, @Image2, ... in array order. |
| `video` | str | yes |  |  | URL of the video to edit. The edit keeps its scene, subject and motion; 3-20 seconds, longer videos are trimmed to 20 seconds. |
| `images` | List[str] |  |  | up to 10 items | Optional reference images (up to 10) for a subject, object or style to bring into the edit. |
| `keep_original_sound` | bool |  | `false` |  | Keep the input video's own sound instead of generating new synchronized audio. |
| `aspect_ratio` | str |  |  | `16:9`, `9:16`, `1:1`, `21:9` | Aspect ratio of the output video. Follows the input video if not specified. |

## REST and CLI

The wrapper is a thin layer over the REST API: submit, then poll for the result.

```bash
curl -s -X POST "https://api.wavespeed.ai/api/v3/kwaivgi/kling-v4.0/text-to-video" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY" -H "Content-Type: application/json" \
  -d '{"prompt": "A slow cinematic dolly shot through a rain-soaked neon night market, reflections on the pavement"}'
# -> {"data": {"id": "<prediction_id>"}}

curl -s "https://api.wavespeed.ai/api/v3/predictions/<prediction_id>/result" \
  -H "Authorization: Bearer $WAVESPEED_API_KEY"
# -> status: completed, outputs: ["<url>"]
```

```bash
npm i -g @wavespeed/cli && wavespeed login
wavespeed run kwaivgi/kling-v4.0/text-to-video -p "your prompt"
```

## Related

- [awesome-kling-api](https://github.com/WaveSpeedAI/awesome-kling-api) — prompt library and variant guide
- More model wrappers: [Seedance 2.5](https://github.com/WaveSpeedAI/seedance-2.5-api) · [Wan 3.0](https://github.com/WaveSpeedAI/wan-3.0-api) · [Veo 3.1](https://github.com/WaveSpeedAI/veo-3.1-api) · [MiniMax H3](https://github.com/WaveSpeedAI/minimax-h3-api) · [HappyHorse 1.1](https://github.com/WaveSpeedAI/happyhorse-1.1-api) · [FLUX 3](https://github.com/WaveSpeedAI/flux-3-api) · [Seedream 5.5](https://github.com/WaveSpeedAI/seedream-5.5-api) · [GPT Image 2.6](https://github.com/WaveSpeedAI/gpt-image-2.6-api) · [Nano Banana 2.1](https://github.com/WaveSpeedAI/nano-banana-2.1-api)
- SDKs and tools: [Python](https://github.com/WaveSpeedAI/wavespeed-python) · [JavaScript](https://github.com/WaveSpeedAI/wavespeed-javascript) · [CLI](https://github.com/WaveSpeedAI/wavespeed-cli) · [MCP server](https://github.com/WaveSpeedAI/mcp-server) · [ComfyUI nodes](https://github.com/WaveSpeedAI/wavespeed-comfyui)
- [Full model catalog](https://wavespeed.ai/models?utm_source=github&utm_medium=readme&utm_campaign=kling-4.0-api)

## Notes

- Kling 4.0 is a model by Kuaishou. This repository is maintained by WaveSpeedAI and wraps the WaveSpeedAI hosted API for it.
- Function signatures and the tables above are generated from the live model schemas (last generated 2026-11-22). The model pages are the source of truth if an endpoint changes.
- Issues and pull requests are welcome. License: MIT.
