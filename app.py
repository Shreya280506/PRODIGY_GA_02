import gradio as gr

from generator import ImageGenerator
from utils import save_image
from history import save_history
from styles import STYLE_PRESETS

generator = ImageGenerator()


def generate_image(
    prompt,
    style,
    negative_prompt,
    guidance,
    steps,
):

    final_prompt = f"{prompt}, {STYLE_PRESETS[style]}"

    image = generator.generate(
        prompt=final_prompt,
        negative_prompt=negative_prompt,
        guidance_scale=guidance,
        steps=steps,
    )

    save_image(image, prompt)
    save_history(prompt)

    return image


with gr.Blocks(title="VisionCraft AI") as demo:

    gr.Markdown("# 🎨 VisionCraft AI")
    gr.Markdown("Generate stunning AI images using Stable Diffusion")

    with gr.Row():

        with gr.Column():

            prompt = gr.Textbox(
                label="Prompt",
                placeholder="A futuristic city at sunset"
            )

            style = gr.Dropdown(
                choices=list(STYLE_PRESETS.keys()),
                value="Realistic",
                label="Style"
            )

            negative_prompt = gr.Textbox(
                label="Negative Prompt",
                placeholder="blurry, low quality"
            )

            guidance = gr.Slider(
                1,
                20,
                value=7.5,
                label="Guidance Scale"
            )

            steps = gr.Slider(
                10,
                50,
                value=30,
                step=1,
                label="Inference Steps"
            )

            generate = gr.Button("🚀 Generate")

        with gr.Column():

            output = gr.Image(label="Generated Image")

    generate.click(
        fn=generate_image,
        inputs=[
            prompt,
            style,
            negative_prompt,
            guidance,
            steps
        ],
        outputs=output
    )

demo.launch()