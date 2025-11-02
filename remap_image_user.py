from PIL import Image

def remap_gif_pixels(input_path, output_path):
    """
    Remaps pixel values of a GIF image from a 0-255 range to a 0-100 range.

    Args:
        input_path (str): The path to the input GIF image (0-255 range).
        output_path (str): The path where the remapped GIF image will be saved (0-100 range).
    """
    try:
        img = Image.open(input_path)
        img = img.convert("L")  # Convert to grayscale if not already

        # Create a new image for the remapped pixels
        remapped_img = Image.new('L', img.size)

        pixels = img.load()
        remapped_pixels = remapped_img.load()

        for y in range(img.height):
            for x in range(img.width):
                original_value = pixels[x, y]
                # Remap from 0-255 to 0-100
                remapped_value = int((original_value / 255.0) * 100.0)
                remapped_pixels[x, y] = remapped_value

        remapped_img.save(output_path, "GIF")
        print(f"Successfully remapped '{input_path}' to '{output_path}' with pixel values from 0-100.")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_gif_path = "/workspaces/SLEUTH3.0beta_p01_linux/Input/taipei_coarse_base/taipei_coarse_base.slope.gif"
    output_gif_path = "/workspaces/SLEUTH3.0beta_p01_linux/Input/taipei_coarse_base/taipei_coarse_base.slope_remapped.gif"
    remap_gif_pixels(input_gif_path, output_gif_path)
