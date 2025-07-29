import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from scripts.train import FlowerCNN  # Assuming model class is in train.py

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

data_dir = r"D:\ml_lern\sample_fewShot_test"
model_path = "models/cnn_baseline.pth"
image_size = 128
batch_size = 16

# Load test dataset
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
])

test_dataset = datasets.ImageFolder(root=data_dir, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
num_classes = len(test_dataset.classes)

# Load model
model = FlowerCNN(num_classes).to(device)
model.load_state_dict(torch.load(model_path))
model.eval()

# Evaluation
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")
