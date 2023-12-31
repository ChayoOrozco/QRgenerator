import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    logo = Image.open(logo_path)
    qr_width, qr_height = qr_img.size
    logo_size = int(qr_width / 4) 
    logo = logo.resize((logo_size, logo_size))
    logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, logo_pos, mask=logo) 

    qr_img.save(output_path)

data_to_encode = "https://medicalhealthinstitute.com/tracking" 
logo_path = "circuloblanco.png" 
output_path = "Tracking&InvoiceDepartmentMHI.png"

generate_qr_with_logo(data_to_encode, logo_path, output_path)
