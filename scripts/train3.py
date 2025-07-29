import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torchvision.datasets import ImageFolder
import random

# -------- CONFIGURATION -------- #
NUM_CLASSES_PER_EPISODE = 5  # N-way
NUM_SUPPORT = 5              # K-shot
NUM_QUERY = 5                # Query samples per class
EMBEDDING_DIM = 64
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------- BACKBONE NETWORK -------- #
class ConvBackbone(nn.Module):
    def __init__(self, output_dim=EMBEDDING_DIM):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),  # RGB images
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        # Input 84x84 => after 2 maxpool(2) => 21x21
        self.fc = nn.Linear(64 * 21 * 21, output_dim)

    def forward(self, x):
        x = self.encoder(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

# -------- EPISODE SAMPLER -------- #
def create_episode(dataset, n_classes, k_shot, q_query):
    class_indices = {}
    for idx, (_, label) in enumerate(dataset.samples):
        class_indices.setdefault(label, []).append(idx)

    selected_classes = random.sample(list(class_indices.keys()), n_classes)

    support_x, support_y, query_x, query_y = [], [], [], []
    label_map = {cls: i for i, cls in enumerate(selected_classes)}

    for cls in selected_classes:
        indices = random.sample(class_indices[cls], k_shot + q_query)
        support_idxs = indices[:k_shot]
        query_idxs = indices[k_shot:]

        support_x += [dataset[i][0] for i in support_idxs]
        support_y += [label_map[cls]] * k_shot
        query_x += [dataset[i][0] for i in query_idxs]
        query_y += [label_map[cls]] * q_query

    support_x = torch.stack(support_x).to(DEVICE)
    query_x = torch.stack(query_x).to(DEVICE)
    support_y = torch.tensor(support_y).to(DEVICE)
    query_y = torch.tensor(query_y).to(DEVICE)

    return support_x, support_y, query_x, query_y

# -------- PROTOTYPES -------- #
def compute_prototypes(support_x, support_y, model):
    embeddings = model(support_x)
    prototypes = []

    for cls in torch.unique(support_y):
        class_embeddings = embeddings[support_y == cls]
        prototype = class_embeddings.mean(dim=0)
        prototypes.append(prototype)

    return torch.stack(prototypes)

# -------- EVALUATE ONE EPISODE -------- #
def evaluate_episode(model, support_x, support_y, query_x, query_y):
    model.eval()
    with torch.no_grad():
        prototypes = compute_prototypes(support_x, support_y, model)
        query_embeddings = model(query_x)

        dists = torch.cdist(query_embeddings, prototypes)
        preds = torch.argmin(dists, dim=1)
        acc = (preds == query_y).float().mean().item()
    return acc

# -------- TRAINING LOOP -------- #
def train_few_shot(model, dataset, num_episodes=1000):
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    model.train()

    for episode in range(1, num_episodes + 1):
        support_x, support_y, query_x, query_y = create_episode(
            dataset, NUM_CLASSES_PER_EPISODE, NUM_SUPPORT, NUM_QUERY
        )
        optimizer.zero_grad()

        prototypes = compute_prototypes(support_x, support_y, model)
        query_embeddings = model(query_x)
        dists = torch.cdist(query_embeddings, prototypes)
        loss = F.cross_entropy(-dists, query_y)

        loss.backward()
        optimizer.step()

        if episode % 100 == 0:
            acc = (torch.argmin(dists, dim=1) == query_y).float().mean().item()
            print(f"Episode {episode} - Loss: {loss.item():.4f}, Acc: {acc:.4f}")

# -------- MAIN -------- #
if __name__ == "__main__":
    dataset_root = r"D:\ml_lern\dataset"  # Your dataset folder here

    transform = transforms.Compose([
        transforms.Resize((84, 84)),
        transforms.ToTensor(),
    ])

    dataset = ImageFolder(root=dataset_root, transform=transform)

    model = ConvBackbone().to(DEVICE)
    train_few_shot(model, dataset)
