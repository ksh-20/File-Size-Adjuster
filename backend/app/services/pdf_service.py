import fitz
import os

def adjust_pdf_size(input_path, output_path, target_size, operation):
    doc = fitz.open(input_path)

    if operation == "decrease":
        doc.save(
            output_path,
            garbage=4,
            deflate=True,
            clean=True
        )
    else:
        doc.save(output_path)

        current = os.path.getsize(output_path)

        while current < target_size:
            with open(output_path, "ab") as f:
                f.write(b"0" * 2048)

            current = os.path.getsize(output_path)

    doc.close()

    return output_path