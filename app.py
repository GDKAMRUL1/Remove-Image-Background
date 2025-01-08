from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    """
    Removes the background from an image and saves the result.

    :param input_path: Path to the input image.
    :param output_path: Path to save the output image.
    """
    try:
        with open(input_path, 'rb') as file:
            input_image = file.read()
            output_image = remove(input_image)

        # Save the output
        output = Image.open(io.BytesIO(output_image))
        output.save(output_path, format='PNG')  # Always save as PNG for transparency
        print(f"Background removed and saved to: {output_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "img.jpg"  # Replace with your image path
    output_image_path = "output.png"
    remove_background(input_image_path, output_image_path)
