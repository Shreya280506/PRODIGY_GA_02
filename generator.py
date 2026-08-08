import io
import os

import fal_client
import requests
import streamlit as st
from PIL import Image


class ImageGenerator:

    def __init__(self):
        try:
            self.api_key = st.secrets["FAL_KEY"]
        except KeyError:
            raise RuntimeError(
                "FAL_KEY is not configured. "
                "Add FAL_KEY to Streamlit Secrets."
            )

        os.environ["FAL_KEY"] = self.api_key

    def generate(
        self,
        prompt,
        negative_prompt="",
        guidance_scale=3.5,
        steps=4,
        width=512,
        height=512,
    ):

        result = fal_client.subscribe(
            "fal-ai/flux/schnell",
            arguments={
                "prompt": prompt,
                "num_inference_steps": min(max(steps, 1), 4),
                "guidance_scale": guidance_scale,
                "image_size": {
                    "width": width,
                    "height": height,
                },
                "num_images": 1,
                "output_format": "png",
            },
        )

        image_url = result["images"][0]["url"]

        response = requests.get(image_url, timeout=120)
        response.raise_for_status()

        return Image.open(
            io.BytesIO(response.content)
        ).convert("RGB")