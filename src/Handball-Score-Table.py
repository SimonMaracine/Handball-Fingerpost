import pyglet
import main_window
import second_window

VERSION = "v0.0"

if __name__ == "__main__":
    print("Handball Score Table " + VERSION)
    main_window.main_window.activate()  # set focus to the main window
    pyglet.app.run()
