import qrcode
import random
from PIL import Image  # Eklediğimiz satır

def generate_random_data():
    # Generate random data for QR code (you can customize this based on your requirements)
    return ''.join(str(random.randint(0, 9)) for _ in range(12))

def generate_qr_code(data, filename='qrcode'):
    # Generate QR code image using qrcode library
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filename_with_extension = f"{filename}.png"
    img.save(filename_with_extension)
    return filename_with_extension
