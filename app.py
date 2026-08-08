import io

import streamlit as st

from generator import ImageGenerator
from utils import save_image
from history import save_history
from styles import STYLE_PRESETS


st.set_page_config(
    page_title="VisionCraft AI",
    page_icon="🎨",
    layout="wide"
)


@st.cache_resource
def load_generator():
    return ImageGenerator()


st.title("🎨 VisionCraft AI")
st.markdown(
    "Generate stunning AI images using **Stable Diffusion**."
)

st.divider()

left, right = st.columns([1, 1])

with left:

    st.subheader("Image Settings")

    prompt = st.text_area(
        "Prompt",
        placeholder="A futuristic city at sunset",
        height=120
    )

    style = st.selectbox(
        "Style",
        list(STYLE_PRESETS.keys())
    )

    negative_prompt = st.text_area(
        "Negative Prompt",
        value="blurry, low quality, distorted",
        height=80
    )

    guidance = st.slider(
        "Guidance Scale",
        min_value=1.0,
        max_value=20.0,
        value=7.5,
        step=0.5
    )

    steps = st.slider(
        "Inference Steps",
        min_value=5,
        max_value=20,
        value=10
    )

    generate = st.button(
        "🚀 Generate Image",
        use_container_width=True,
        type="primary"
    )


with right:

    st.subheader("Generated Image")

    image_placeholder = st.empty()


if generate:

    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    final_prompt = f"{prompt}, {STYLE_PRESETS[style]}"

    try:

        with st.spinner(
            "Loading Stable Diffusion and generating your image..."
        ):

            generator = load_generator()

            image = generator.generate(
                prompt=final_prompt,
                negative_prompt=negative_prompt,
                guidance_scale=guidance,
                steps=steps
            )

        save_image(image, prompt)
        save_history(prompt)

        image_placeholder.image(
            image,
            caption=prompt,
            use_container_width=True
        )

        st.success("Image generated successfully!")

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="PNG"
        )

        st.download_button(
            label="📥 Download Image",
            data=buffer.getvalue(),
            file_name="visioncraft_ai.png",
            mime="image/png"
        )

    except Exception as e:

        st.error(
            f"Image generation failed: {e}"
        )

        st.info(
            "The model may be unavailable on the current "
            "Streamlit Cloud hardware. Please check the app logs."
        )