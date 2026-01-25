import qrcode

QR = qrcode.make("i love u....")
QR.save("QR.png")