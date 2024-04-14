from image_processing.image_extractor import ImageExtractor
from utils.helper_functions import *

def main():
    # Load input image
    input_image_path = "input_images/input_image.jpg"
    input_image = load_image(input_image_path)

    # Initialize image extractor
    image_extractor = ImageExtractor()

    # Extract abstract images
    abstract_images = image_extractor.extract_images(input_image)

    # Save extracted images
    for i, abstract_image in enumerate(abstract_images):
        save_image(abstract_image, f"extracted_images/abstract_image_{i}.jpg")

if __name__ == "__main__":
    main()