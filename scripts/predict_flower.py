import torch
from torchvision import transforms, models
from PIL import Image

# Configs - update paths & settings accordingly
model_save_path = "models/flower_resnet18_best.pth"
image_size = 128
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load classes (hardcoded or load from your training script)
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# Define transform (must be same as validation)
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# Load model
def load_model():
    model = models.resnet18(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(torch.load(model_save_path, map_location=device))
    model.to(device)
    model.eval()
    return model

def predict_flower(image_path, model, class_names):
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]

if __name__ == "__main__":
    model = load_model()
    test_image_path = r"D:\ml_lern\dataset\daisy\image_001.jpg"  # update this path
    prediction = predict_flower(test_image_path, model, class_names)
    print(f"Predicted flower: {prediction}")
