from flask import Flask, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def generate_qr():
    ssid = "Home Wifi"
    password = "2173d82h1"

    wifi_data = 'WIFI:S:{};T:WPA;P:{};;'.format(ssid, password)

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(wifi_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    byteIO = BytesIO()
    img.save(byteIO, 'PNG')
    byteIO.seek(0)
    return send_file(byteIO, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5000,debug=True)