import qrcode

data = input ("Enter the text or Url: ").strip()
filename = input("Enter the file name: ").strip()
qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)
image = qr.make_image(fill_color="black", black_color="white")
image.save(filename)
print(f"QRCode saved as {filename}")