import cv2
from matplotlib import pyplot as plt

# Load the image
image_path = '/Users/dominiquebuob/Documents/Projects/Embroider-Image-Transformation/data/Husky-Golden-Red.png'
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Display the image
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()
