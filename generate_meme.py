from PIL import Image, ImageDraw, ImageFont
import textwrap


def swap_caps(text):
    text = text.lower()
    ret = []
    for i in range(0, len(text)):
        if i%2 == 0:
            ret.append(text[i].upper())
        else:
            ret.append(text[i])

    return ret


def bob_mock(text):
    # load image
    im = Image.open('images/spongebob.jpg')
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size

    # load font

    font = ImageFont.truetype(font='fonts/impact.ttf', size=int(image_height/10))

    # wrap text
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(text, width=chars_per_line)

    # draw top lines
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

    im.save('meme-' + im.filename.split('/')[-1])


args = 'this is a test sentence'
bob_mock(args)
print(swap_caps("HELLO"))
