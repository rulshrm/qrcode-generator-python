# QR Code Generator in Python

QR Code Generator adalah sebuah program Python interaktif yang digunakan untuk membuat QR Code dengan input teks atau URL. Program ini mendukung konfigurasi dasar, seperti ukuran kotak, tingkat koreksi kesalahan, dan penyimpanan hasil di folder khusus (assets).

## Features

- Generate QR codes for text or URLs.
- Customizable QR code size and error correction levels.
- Save generated QR codes as image files.
- User-friendly and lightweight.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/rulshrm/qrcode-generator-python.git
   cd qrcode-generator-python
   ```

2. Install the required library:
   ```bash
   pip install qrcode
   ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```
2. Enter the text or URL you want to generate a QR code for when prompted.

3. The generated QR code will be saved as an image file in the project directory (default: Qrcode1.png).

## Example

After running the script and providing input, the terminal will display:
  ```bash
  Masukan input: Hello, World!
  QR Code berhasil dibuat dan disimpan sebagai Qrcode1.png
  Nilai input: Hello, World!
  ```
  Generated QR Code

## Structure
project/
├── main.py               # File utama program
├── assets/               # Folder penyimpanan QR Code
│   ├── Qrcode1.png       # QR Code hasil yang dihasilkan
└── README.md             # Dokumentasi program
