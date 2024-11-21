'''
  Documentation:
  https://pypi.org/project/qrcode/
'''

import qrcode
import os
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
    
    # Membuat folder 'assets' jika belum ada
    if not os.path.exists('assets'):
      os.makedirs('assets')

    # Menyimpan gambar QR Code dengan nama kustom
    filename = input("\nMasukkan nama file (default: Qrcode1.png): ").strip() or "Qrcode1.png"
    if not filename.endswith(".png"):
      filename += ".png"
    
    # Menyimpan gambar ke dalam folder 'assets'
    filename = os.path.join('assets', filename)
        
    try:
        # Menyimpan gambar QR Code
        img.save(filename)
        print(f"QR Code berhasil dibuat dan disimpan sebagai {os.path.basename(filename)}")
        print(f"Nilai input: {input_data}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan QR Code: {e}")

def main_menu():
  while True:
    print("QR code generator")
    print("1. Buat QR code baru.")
    print("2. Keluar.")
    
    choice = input("Pilih opsi(1/2): ").strip()
    
    if choice=="1":
      generate_qrcode()
    elif choice=="2":
      print("Terima kasih telah menggunakan QR Code Generator. Sampai jumpa!")
      break
    else:
      print("pilihan adna tidak valid")

if __name__ == "__main__":
    main_menu()