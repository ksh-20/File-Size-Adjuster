ALLOWED_TYPES = {
    'image/jpeg',
    'image/png',
    'image/webp',
    'application/pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
}

MAX_SIZE = 100 * 1024 * 1024


def validate_type(content_type):
    return content_type in ALLOWED_TYPES


def validate_size(size):
    return size <= MAX_SIZE