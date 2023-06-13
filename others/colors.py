import colorsys
from io import BytesIO
from colorthief import ColorThief
import requests
from PIL import Image, ImageTk

DEG30 = 30/360.
def adjacent_colors(rgb: list[int], d: float = DEG30) -> list[map]:
    '''
    Takes in an RGB color value, and returns a list of mapped adjacent colors.
    '''

    r, g, b = map(lambda x: x/255., rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = [(h + d) % 1 for d in (-d, d)]
    adjacent = [map(lambda x: int(round(x * 255)), colorsys.hls_to_rgb(hi, l, s))
            for hi in h]
    return adjacent

def analogous_colors(rgb: list[int]) -> list[int]:
    '''
    Takes in an RGB color value, and returns a list of analogous colors directly.
    '''

    colors = adjacent_colors(rgb)
    colors[0] = [i for i in colors[0]]
    colors[1] = [i for i in colors[1]]

    return colors

# print(analogous_colors([255, 3, 0]))

def complementary(rgb: list[int]) -> list[int]:
    '''Returns RGB components of complementary color'''

    hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    return [int(color) for color in colorsys.hsv_to_rgb((hsv[0] + 0.5) % 1, hsv[1], hsv[2])]

# print(complementary([255,0,0]))

def rgb_to_hex(rgb: list[int]) -> str:
    '''
    Converts an RGB to its Hex format.
    '''
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

# print([rgb_to_hex(analogous_colors([255,0,0])[0])])

def dominant_color_finder(image_path: str) -> list[int]:
    '''
    Returns the most common RGB values from the image.
    '''
    image = ColorThief(image_path)
    color = image.get_color(quality = 1)

    return color



# response = requests.get('https://i.stack.imgur.com/JM4F2.png', timeout = 1)
# img = Image.open(BytesIO(response.content))
# img = img.resize((150, 150))

# cover = ImageTk.PhotoImage(img)
# print(rgb_to_hex(dominant_color_finder(cover)))
