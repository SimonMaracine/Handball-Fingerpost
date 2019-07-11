import pyglet
import src.config  # init some variables
import src.window0 as window0

if __name__ == "__main__":
    print("Handball Score Table " + src.config.VERSION)
    window0.start()
    pyglet.app.run()
