import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, color

# Create a simple binary test image with shapes (if you want to generate)
def create_test_image():
    img = np.zeros((200, 200), dtype="uint8")
    cv2.rectangle(img, (20, 20), (80, 80), 255, -1)
    cv2.circle(img, (150, 50), 30, 255, -1)
    cv2.rectangle(img, (120, 120), (170, 180), 255, -1)
    return img

# Uncomment below if you have an existing image to load
# img = cv2.imread('shapes.png', cv2.IMREAD_GRAYSCALE)
# _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Create binary image here
binary = create_test_image()

# Label connected components
labels = measure.label(binary, connectivity=2)

# Count objects (exclude background=0)
num_objects = labels.max()

print(f"Number of objects detected: {num_objects}")

# Create a color image to visualize the labels
label_overlay = color.label2rgb(labels, image=binary, bg_label=0)

# Plot original and labeled images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(binary, cmap='gray')
axes[0].set_title('Binary Image')
axes[0].axis('off')

axes[1].imshow(label_overlay)
axes[1].set_title('Labeled Objects')
axes[1].axis('off')

plt.show()
