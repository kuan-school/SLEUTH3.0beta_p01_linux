
from PIL import Image
import os

def remap_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            if img.mode != 'P':
                img = img.convert('P')
            
            remapped_pixels = bytearray()
            palette = img.getpalette()
            new_palette = []

            if palette:
                # Remap the palette
                for i in range(0, len(palette), 3):
                    r, g, b = palette[i:i+3]
                    # Simple grayscale conversion, then remap.
                    # This is a simplification. For a true color image, this would be more complex.
                    # Assuming the original image is grayscale-like and uses the palette for that.
                    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                    remapped_gray = round(gray * 100 / 255)
                    new_palette.extend([remapped_gray, remapped_gray, remapped_gray])
            
            pixels = img.load()
            new_img = Image.new('P', img.size)
            
            # Create a mapping from old palette index to new palette index
            # This is complex because we need to map colors.
            # A simpler approach for paletted images is to convert to L, remap, and convert back to P.
            img_l = img.convert('L')
            
            new_img_l = img_l.point(lambda p: round(p * 100 / 255))

            new_img_l.save(output_path)

        print(f"Image remapped and saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = '/workspaces/SLEUTH3.0beta_p01_linux/Input/taipei_coarse_base/taipei_coarse_base.slope.gif'
    output_file = '/workspaces/SLEUTH3.0beta_p01_linux/Input/taipei_coarse_base/taipei_coarse_base.slope_remapped.gif'
    remap_image(input_file, output_file)
