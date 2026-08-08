import torch
from diffusers import StableDiffusionPipeline
from config import MODEL_ID


class ImageGenerator:

    def __init__(self):
        print("Loading Stable Diffusion...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        if self.device == "cuda":
            dtype = torch.float16
        else:
            dtype = torch.float32

        print(f"Device: {self.device}")

        self.pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=dtype,
            safety_checker=None,
            requires_safety_checker=False
        )

        self.pipe = self.pipe.to(self.device)

        if self.device == "cpu":
            self.pipe.enable_attention_slicing()

        print("Stable Diffusion loaded successfully.")

    def generate(
        self,
        prompt,
        negative_prompt="",
        guidance_scale=7.5,
        steps=20,
        width=512,
        height=512,
    ):

        result = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=steps,
            width=width,
            height=height,
        )

        return result.images[0]