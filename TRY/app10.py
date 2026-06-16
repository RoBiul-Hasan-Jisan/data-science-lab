import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import umap
import torch
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from model_loader import load_model_and_data
from gradcam_utils import get_gradcam_features

st.set_page_config(layout="wide")
st.title("CNN Feature Visualization Dashboard")

# ---- Sidebar controls ----
reduction = st.sidebar.selectbox("Dimensionality Reduction", ["UMAP", "t-SNE"])
max_samples = st.sidebar.slider("Number of Samples", 50, 1000, 300)
perplexity = st.sidebar.slider("t-SNE Perplexity", 5, 50, 30)
zoom = st.sidebar.slider("Thumbnail Zoom", 0.1, 1.0, 0.4)
use_gradcam = st.sidebar.checkbox("Use Grad-CAM Features")
target_layer_name = st.sidebar.selectbox("ResNet Layer", ["layer1", "layer2", "layer3", "layer4"])

# ---- Load model and data ----
device = "cuda" if torch.cuda.is_available() else "cpu"
model, dataloader, class_names = load_model_and_data()
model = model.to(device)

# ---- Get target layer ----
target_layer = getattr(model, target_layer_name)

# ---- Feature extraction ----
features = []
labels = []
thumbnails = []

with torch.no_grad():
    for images, label in dataloader:
        images = images.to(device)
        if use_gradcam:
            cams = get_gradcam_features(model, images, target_layer)
            feats = cams.view(cams.shape[0], -1).cpu().numpy()
        else:
            feats = torch.flatten(target_layer(images), 1).cpu().numpy()

        features.append(feats)
        labels.extend(label.numpy())
        for img in images:
            thumbnails.append(img.cpu())
        if len(labels) >= max_samples:
            break

features = np.vstack(features)[:max_samples]
labels = labels[:max_samples]
thumbnails = thumbnails[:max_samples]
features = StandardScaler().fit_transform(features)

# ---- Dimensionality reduction ----
if reduction == "t-SNE":
    reducer = TSNE(n_components=2, perplexity=perplexity, random_state=42)
else:
    reducer = umap.UMAP(n_components=2, random_state=42)

proj = reducer.fit_transform(features)

# ---- Visualization ----
fig, ax = plt.subplots(figsize=(10, 8))

def imscatter(x, y, images, ax=None, zoom=0.5):
    ax = ax or plt.gca()
    for i in range(len(images)):
        img = images[i].permute(1, 2, 0).numpy()
        im = OffsetImage(img, zoom=zoom)
        ab = AnnotationBbox(im, (x[i], y[i]), frameon=False)
        ax.add_artist(ab)

palette = sns.color_palette("hls", len(class_names))
for idx in range(len(class_names)):
    pts = proj[np.array(labels) == idx]
    ax.scatter(pts[:, 0], pts[:, 1], color=palette[idx], alpha=0.4, label=class_names[idx])

imscatter(proj[:, 0], proj[:, 1], thumbnails, ax=ax, zoom=zoom)
ax.set_title(f"{reduction} Projection (Grad-CAM: {use_gradcam})", fontsize=14)
ax.axis('off')
ax.legend()
st.pyplot(fig)
