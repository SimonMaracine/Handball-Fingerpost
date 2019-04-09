import pyglet


def rect(x, y, width, height, color):
    pyglet.graphics.draw(
        6,
        pyglet.gl.GL_TRIANGLES,
        ("v2i", (x, y,
                 x + width, y,
                 x + width, y + height,
                 x + width, y + height,
                 x, y + height,
                 x, y)),
        ("c4B", color * 6)
    )

