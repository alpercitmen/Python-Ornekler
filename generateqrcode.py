#Python Script for generate QRCode

import pyqrcode
from pyqrcode import QRCode

# String for QRCode
s = "https://github.com/alpercitmen/"

# Generate QR Code
url = pyqrcode.create(s)

# Create and save the svg file naming myqr.svg
url.svg("myqr.svg", scale=8)
