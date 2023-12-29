import qrcode

# img = qrcode.make('https://www.youtube.com/@AzadChaiwala')
# img.save('qrcode.png')

from PIL import Image

qr=qrcode.QRCode(version=1,
 error_correction= qrcode.constants.ERROR_CORRECT_H,
 box_size=10,border=4)

qr.add_data('https://www.youtube.com/@AzadChaiwala')

qr.make(fit=True)

img= qr.make_image(fill_color='green',back_color='blue')

img.save('azad.png')