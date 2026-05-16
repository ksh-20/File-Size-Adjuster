def convert_to_bytes(size, unit):
    if unit == "MB":
        return int(size * 1024 * 1024)
    return int(size * 1024)

def get_file_size(path):
    import os
    return os.path.getsize(path)