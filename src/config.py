from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "best_mobilenet_v2_food_freshness_model.pth"

IMAGE_SIZE = 224
# MODEL_NAME = "resnet18"
MODEL_NAME = "mobilenet_v2"

CLASS_NAMES = [
    "FreshApple",
    "FreshBanana",
    "FreshStrawberry",
    "RottenApple",
    "RottenBanana",
    "RottenStrawberry",
]

DISPLAY_NAMES = {
    "FreshApple": "Fresh Apple",
    "FreshBanana": "Fresh Banana",
    "FreshStrawberry": "Fresh Strawberry",
    "RottenApple": "Rotten Apple",
    "RottenBanana": "Rotten Banana",
    "RottenStrawberry": "Rotten Strawberry",
}
