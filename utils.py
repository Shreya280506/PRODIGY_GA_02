import os
from datetime import datetime

from config import OUTPUT_DIR


os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_image(image, prompt):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{timestamp}_{prompt[:30].replace(' ','_')}.png"

    path = os.path.join(OUTPUT_DIR, filename)

    image.save(path)

    return path