import qrcode

qr_data = '이형구'
qr_img = qrcode.make(qr_data)

save_path = 'ab.png'
qr_img.save(save_path)