# imghdr.py
# Minimal implementation to support basic image types
# Based on common replacements suggested in the community [citation:3][citation:9]

def what(filepath):
    # Read the first few bytes to determine image type
    with open(filepath, 'rb') as f:
        header = f.read(12)

    if header.startswith(b'\xff\xd8\xff'):
        return 'jpeg'
    elif header.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
        return 'gif'
    elif header.startswith(b'BM'):
        return 'bmp'
    # Add more formats if needed
    else:
        return None