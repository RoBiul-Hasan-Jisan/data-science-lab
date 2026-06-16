import torch
import torch.nn.functional as F

def get_gradcam_features(model, images, target_layer):
    # Hook to capture gradients & activations
    activations = []
    gradients = []

    def forward_hook(module, input, output):
        activations.append(output)

    def backward_hook(module, grad_in, grad_out):
        gradients.append(grad_out[0])

    handle_forward = target_layer.register_forward_hook(forward_hook)
    handle_backward = target_layer.register_backward_hook(backward_hook)

    model.eval()
    images.requires_grad = True
    output = model(images)
    class_idx = output.argmax(dim=1)
    one_hot = F.one_hot(class_idx, num_classes=output.shape[1]).float()
    model.zero_grad()
    output.backward(gradient=one_hot)

    # Compute Grad-CAM
    grads = gradients[0]  # [B, C, H, W]
    acts = activations[0]  # [B, C, H, W]
    weights = grads.mean(dim=(2, 3), keepdim=True)
    cam = (weights * acts).sum(dim=1, keepdim=True)
    cam = F.relu(cam)
    cam = F.interpolate(cam, size=images.shape[2:], mode='bilinear', align_corners=False)
    cam = cam - cam.min()
    cam = cam / cam.max()

    handle_forward.remove()
    handle_backward.remove()

    return cam.squeeze(1)  # Shape: [B, H, W]
