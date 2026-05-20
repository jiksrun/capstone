from PIL import Image
from torchvision import transforms

from src.config import IMAGE_SIZE


def get_transforms(img_size: int = IMAGE_SIZE):
    imagenet_mean = [0.485, 0.456, 0.406]
    imagenet_std = [0.229, 0.224, 0.225]

    train_transform = transforms.Compose(
        [
            transforms.Resize((img_size, img_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=imagenet_mean, std=imagenet_std),
        ]
    )

    eval_transform = transforms.Compose(
        [
            transforms.Resize((img_size, img_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=imagenet_mean, std=imagenet_std),
        ]
    )

    return train_transform, eval_transform


def prepare_image(image: Image.Image):
    _, eval_transform = get_transforms()
    return eval_transform(image.convert("RGB")).unsqueeze(0)
