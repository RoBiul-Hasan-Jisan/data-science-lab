import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# === CONFIG ===
data_dir = r"D:\ml_lern\sample_fewShot_processed"
batch_size = 16
image_size = 128
epochs = 10
learning_rate = 0.001
model_save_path = "models/cnn_baseline.pth"

# === TRANSFORM ===
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
])

# === LOAD DATA ===
dataset = datasets.ImageFolder(root=data_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
class_names = dataset.classes
num_classes = len(class_names)

# === SIMPLE CNN MODEL ===
class FlowerCNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * (image_size // 4) * (image_size // 4), 256)
        self.fc2 = nn.Linear(256, num_classes)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # (B, 32, H/2, W/2)
        x = self.pool(torch.relu(self.conv2(x)))  # (B, 64, H/4, W/4)
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

# === DEVICE ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = FlowerCNN(num_classes).to(device)

# === TRAINING SETUP ===
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# === TRAIN LOOP ===
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct, total = 0, 0

    for images, labels in dataloader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

    accuracy = 100 * correct / total
    print(f"Epoch {epoch+1}/{epochs} | Loss: {running_loss:.4f} | Accuracy: {accuracy:.2f}%")

# === SAVE MODEL ===
os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), model_save_path)
print(f"✅ Model saved at: {model_save_path}")
