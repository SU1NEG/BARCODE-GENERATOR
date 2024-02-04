from barcodes import generate_qr_code, generate_random_data
from PIL import Image  # Eklediğimiz satır

if __name__ == "__main__":
    # Generate random data for QR code
    qr_data = generate_random_data()

    # Generate and save QR code image, get the filename
    filename = generate_qr_code(qr_data)

    if filename is not None:
        # Open and display the QR code image
        img = Image.open(filename)
        img.show()

        print(f"Generated QR Code Data: {qr_data}")
        print(f"QR Code Image saved as: {filename}")
    else:
        print("Error generating QR code image.")
