import streamlit as st
import torch
from torchvision import transforms, models
from PIL import Image
import os

# Path to your saved model
MODEL_PATH = r"D:\ml_lern\model\flower_classifier.pth"

# Device configuration (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource(show_spinner=False)
def load_model():
    # Load the saved checkpoint
    checkpoint = torch.load(MODEL_PATH, map_location=device)
    class_names = checkpoint['class_names']

    # Initialize model architecture
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))

    # Load weights
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    model.to(device)

    return model, class_names

def preprocess_image(image: Image.Image):
    # Define image transformations matching training
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    return transform(image).unsqueeze(0).to(device)

def predict(image: Image.Image, model, class_names):
    input_tensor = preprocess_image(image)
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted_idx = torch.max(probabilities, 0)
        predicted_class = class_names[predicted_idx]
    return predicted_class, confidence.item()

def main():
    st.title("🌸 Flower Image Classifier")
    st.write("Upload a flower image and the model will predict its class.")

    # Load model and class names once (cached)
    model, class_names = load_model()

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            predicted_class, confidence = predict(image, model, class_names)
            st.success(f"Prediction: **{predicted_class}** (Confidence: {confidence * 100:.2f}%)")

if __name__ == "__main__":
    main()
