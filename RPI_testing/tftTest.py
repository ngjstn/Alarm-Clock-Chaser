import time 
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7735  

BORDER = 20
FONTSIZE = 25

# Configuration for CS and DC pins: 
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

disp = st7735.ST7735R(
    spi, 
    rotation=270, 
    height=128, 
    x_offset=2, 
    y_offset=3,  
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Create blank image for drawing.
if disp.rotation % 180 == 90:
    height = disp.width 
    width = disp.height
else:
    width = disp.width  
    height = disp.height

image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


while True: 
    draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)

    (font_width, font_height) = font.getsize(current_time)
    draw.text(
        (width // 2 - font_width // 2, height // 2 - font_height // 2),
        current_time,
        font=font,
        fill=(255, 255, 255),
    )
    disp.image(image)