import itertools

from PIL import Image, ImageDraw, ImageFont

from .board import Board


def tbraille(fontname, size, text):
    try:
        font = ImageFont.truetype(font=fontname, size=size)
    except:
        font = ImageFont.load_default()

    # Don't use font.getsize.
    # It doesn't support multiline text, and differ from ImageDraw.getsize.
    image = Image.new('L', (0, 0))
    draw = ImageDraw.Draw(image)
    img_size = draw.multiline_textsize(text, font=font)
    img_size = (img_size[0], img_size[1] + size)

    image = image.resize(img_size)
    draw = ImageDraw.Draw(image)
    draw.multiline_text((0, 0), text, font=font, fill=(255,))

    board = Board(*img_size)
    pixmap = image.load()
    for x, y in itertools.product(range(img_size[0]), range(img_size[1])):
        board[x, y] = pixmap[x, y]
    return str(board).rstrip()
