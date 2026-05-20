import torch
from PIL import Image

from src.config import CLASS_NAMES, DISPLAY_NAMES
from src.preprocessing import prepare_image


def predict_image(image: Image.Image, model, device):
    input_tensor = prepare_image(image).to(device)

    with torch.inference_mode():
        logits = model(input_tensor)
        probabilities = torch.softmax(logits, dim=1).squeeze(0)

    confidence, predicted_idx = torch.max(probabilities, dim=0)
    class_name = CLASS_NAMES[predicted_idx.item()]

    scores = [
        {
            "class": DISPLAY_NAMES[name],
            "probability": probabilities[idx].item(),
        }
        for idx, name in enumerate(CLASS_NAMES)
    ]
    scores.sort(key=lambda item: item["probability"], reverse=True)

    return {
        "class_name": class_name,
        "display_name": DISPLAY_NAMES[class_name],
        "confidence": confidence.item(),
        "scores": scores,
    }
