import qrcode
import qrcode.constants

def generate_qrcode():
    # Konfigurasi QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Input data dengan validasi
    while True:
        input_data = input("Masukan input: ").strip()
        if input_data:
            break
        else:
            print("Data tidak boleh kosong, silakan masukkan lagi.")

    # Menambahkan data ke QR Code
    qr.add_data(input_data)
    qr.make(fit=True)

    # Membuat gambar QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    try:
        # Menyimpan gambar QR Code
        filename = "assets/Qrcode1.png"
        img.save(filename)
        print(f"QR Code berhasil dibuat dan disimpan sebagai {filename}")
        print(f"Nilai input: {input_data}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan QR Code: {e}")

if __name__ == "__main__":
    generate_qrcode()