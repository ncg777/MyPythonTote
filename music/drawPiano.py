import cairo
import numpy as np
from enum import Enum

class KeyColor(Enum):
    WHITE = (1, 1, 1)
    BLACK = (0, 0, 0)

def draw_piano(highlighted_notes, output_file):
    white_width = 30
    black_width = 20
    # Define key array with size 12
    keys = [
        {'color': KeyColor.WHITE, 'x': white_width*0},
        {'color': KeyColor.BLACK, 'x': (white_width*1)-(black_width/2)},
        {'color': KeyColor.WHITE, 'x': white_width*1},
        {'color': KeyColor.BLACK, 'x': (white_width*2)-(black_width/2)},
        {'color': KeyColor.WHITE, 'x': white_width*2},
        {'color': KeyColor.WHITE, 'x': white_width*3},
        {'color': KeyColor.BLACK, 'x': (white_width*4)-(black_width/2)},
        {'color': KeyColor.WHITE, 'x': white_width*4},
        {'color': KeyColor.BLACK, 'x': (white_width*5)-(black_width/2)},
        {'color': KeyColor.WHITE, 'x': white_width*5},
        {'color': KeyColor.BLACK, 'x': (white_width*6)-(black_width/2)},
        {'color': KeyColor.WHITE, 'x': white_width*6}
    ]

    # Create a new image surface
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 50+(white_width*7), 200)
    ctx = cairo.Context(surface)

    # Set background color
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    # Draw keys
    for key in keys:
        ctx.set_source_rgb(*key['color'].value)
        width = white_width
        if key['color'] == KeyColor.BLACK:
            width = black_width
        ctx.rectangle(key['x']+25, 50, width, 100 if key['color'] == KeyColor.WHITE else 70)
        ctx.set_source_rgb(0, 0, 0)  # Black outline
        ctx.set_line_width(1)
        ctx.stroke()
        ctx.fill()

        if key['color']== KeyColor.BLACK:
            ctx.set_source_rgb(*key['color'].value)
            ctx.rectangle(key['x']+25, 50, width, 100 if key['color'] == KeyColor.WHITE else 70)
            ctx.fill()

    # Highlight notes
    for note in highlighted_notes:
        ctx.set_source_rgb(1, 0, 0)
        if keys[note]['color'] == KeyColor.WHITE:
            ctx.arc(keys[note]['x']+25 + white_width / 2, 140, 5, 0, 2 * np.pi)
        else:
            ctx.arc(keys[note]['x']+25 + (black_width / 2), 110, 5, 0, 2 * np.pi)
        ctx.fill()

    # Save image
    surface.write_to_png(output_file)

if __name__ == '__main__':
    draw_piano([0, 3, 8], 'test.png')