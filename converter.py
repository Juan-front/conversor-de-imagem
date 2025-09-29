from PIL import Image
import os

def convert_to_grayscale(input_path, output_path=None):
    image = Image.open(input_path).convert("L")
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_gray{ext}"
    image.save(output_path)
    return output_path
