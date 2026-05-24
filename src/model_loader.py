import torch
from torch import nn
from torchvision import models
from torchvision.models import MobileNet_V2_Weights
from src.config import CLASS_NAMES, MODEL_PATH


def build_model(num_classes: int = len(CLASS_NAMES)) -> nn.Module:
    # model = models.resnet18(weights=None)
    # in_features = model.fc.in_features
    # model.fc = nn.Linear(in_features, num_classes)
    model = models.mobilenet_v2(weights=None)

    in_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(in_features, num_classes)
    return model


def get_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model(model_path=MODEL_PATH, device=None) -> nn.Module:
    if device is None:
        device = get_device()

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = build_model()
    state_dict = torch.load(model_path, map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model
