import qrcode
from datetime import datetime

def generate_qr():
    data = input("Enter text or URL to generate QR code: ").strip()

    if not data:
        print("Error: Input cannot be empty.")
        return

    filename = input("Enter file name (without extension): ").strip()

    if not filename:
        filename = "qrcode"

    fill_color = input("Enter QR color (default: black): ").strip()
    back_color = input("Enter background color (default: white): ").strip()

    if not fill_color:
        fill_color = "black"

    if not back_color:
        back_color = "white"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{filename}_{timestamp}.png"

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        img.save(output_file)

        print("QR Code generated successfully.")
        print("Saved as:", output_file)

    except Exception as e:
        print("Failed to generate QR code.")
        print("Error:", e)

if __name__ == "__main__":
    generate_qr()