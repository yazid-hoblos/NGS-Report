from PIL import Image
import matplotlib.pyplot as plt
import os

# Create a list of image filenames
image_files = [f"lod_plot2_{i}.png" for i in range(1, 13)]

# Load all the images into a list
images = [Image.open(img) for img in image_files]

# Set the desired layout (e.g., 3 rows and 5 columns)
rows = 3
cols = 4

# Determine the maximum width and height of the individual images
widths, heights = zip(*(img.size for img in images))
max_width = max(widths)
max_height = max(heights)

# Create a new image with the total size (rows * max_height, cols * max_width)
total_width = cols * max_width
total_height = rows * max_height

# Create a blank canvas to concatenate images
concatenated_image = Image.new('RGB', (total_width, total_height))

# Place each image in its respective position on the canvas
for i, img in enumerate(images):
    row = i // cols
    col = i % cols
    concatenated_image.paste(img, (col * max_width, row * max_height))

# Save the concatenated image
concatenated_image.save("concatenated_lod_plots.png")

# Optionally, display the concatenated image
plt.imshow(concatenated_image)
plt.axis('off')  # Hide axes
plt.show()
