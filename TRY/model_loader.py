import torch
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

def load_model_and_data(data_path="./data", batch_size=32, image_size=224):
    transform = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor()
    ])

    dataset = datasets.FakeData(transform=transform, size=200, image_size=(3, image_size, image_size), num_classes=10)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = models.resnet18(pretrained=True)
    model.eval()

    class_names = [f"Class {i}" for i in range(10)]

    return model, dataloader, class_names
