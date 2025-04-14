import matplotlib.pyplot as plt

def copy_image(source, destination):
    try:
        with open(source, "rb") as img_file:
            img_data = img_file.read()
        with open(destination, "wb") as copy_file:
            copy_file.write(img_data)
        print("✅ Image copied successfully!")
    except FileNotFoundError:
        print("❌ Image file not found!")

def show_images(original, copied):
    try:
        img1 = plt.imread(original)
        img2 = plt.imread(copied)
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))
        axes[0].imshow(img1)
        axes[0].set_title("Original Image")
        axes[1].imshow(img2)
        axes[1].set_title("Copied Image")
        plt.show()
    except FileNotFoundError:
        print("❌ Cannot display images, files not found!")

# Example Usage
copy_image("original.jpg", "copy.jpg")
show_images("original.jpg", "copy.jpg")
