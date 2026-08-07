import torch
from diffusers import StableDiffusionPipeline
from config import MODEL_ID, DEVICE, DTYPE

class ImageGenerator:

    def __init__(self):

        print("Loading Stable Diffusion...")

        self.pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=DTYPE,
            safety_checker=None
        )

        self.pipe.to(DEVICE)

        print(f"Running on {DEVICE}")

    def generate(
        self,
        prompt,
        negative_prompt="",
        guidance_scale=7.5,
        steps=30,
        width=512,
        height=512,
    ):

        image = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=steps,
            width=width,
            height=height,
        ).images[0]

        return image

        