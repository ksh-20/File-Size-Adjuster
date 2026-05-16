from PIL import Image
import os

def adjust_image_size(input_path, output_path, target_size, operation):
    quality = 95

    img = Image.open(input_path)

    width, height = img.size

    while True:
        img.save(output_path, optimize=True, quality=quality)

        current_size = os.path.getsize(output_path)

        if operation == "decrease":
            if current_size <= target_size or quality <= 10:
                break

            quality -= 5

            width = int(width * 0.95)
            height = int(height * 0.95)

            img = img.resize((width, height))

        else:
            if current_size >= target_size:
                break

            with open(output_path, "ab") as f:
                f.write(b"0" * 1024)

    return output_path