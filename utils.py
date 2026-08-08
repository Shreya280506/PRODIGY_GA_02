import os
from datetime import datetime

from config import OUTPUT_DIR


def save_image(image, prompt):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"image_{timestamp}.png"

    filepath = os.path.join(
        OUTPUT_DIR,
        filename
    )

    image.save(filepath)

    return filepath