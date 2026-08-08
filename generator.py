import io
import requests
from PIL import Image


class ImageGenerator:

    def __init__(self):
        print("Using Pollinations AI image generation")

    def generate(
        self,
        prompt,
        negative_prompt="",
        guidance_scale=7.5,
        steps=4,
        width=512,
        height=512,
    ):
        url = "https://image.pollinations.ai/prompt/" + requests.utils.quote(
            prompt
        )

        params = {
            "width": width,
            "height": height,
            "nologo": "true",
        }

        response = requests.get(
            url,
            params=params,
            timeout=180,
        )

        response.raise_for_status()

        return Image.open(
            io.BytesIO(response.content)
        ).convert("RGB")