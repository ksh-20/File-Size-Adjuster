import shutil
import os

def adjust_docx_size(input_path, output_path, target_size, operation):
    shutil.copy(input_path, output_path)

    current = os.path.getsize(output_path)

    if operation == "increase":
        while current < target_size:
            with open(output_path, "ab") as f:
                f.write(b"0" * 1024)

            current = os.path.getsize(output_path)

    return output_path