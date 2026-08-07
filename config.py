import torch

MODEL_ID = "runwayml/stable-diffusion-v1-5"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

DEFAULT_WIDTH = 512
DEFAULT_HEIGHT = 512
DEFAULT_STEPS = 30
DEFAULT_GUIDANCE = 7.5

OUTPUT_DIR = "generated_images"

HISTORY_FILE = "history/prompts.json"