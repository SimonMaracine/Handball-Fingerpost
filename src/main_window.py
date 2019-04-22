import pyglet
from pyglet.window import key, mouse
import countdown
from table import Table, table
import second_window
import window0
import config
from config import WIDTH, HEIGHT

main_window = None


def start():
    global main_window
    main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table", vsync=True, visible=False)

    @main_window.event
    def on_draw():
        main_window.clear()
        background.blit(0, 0)
        table.team1.render()
        table.team2.render()
        table.show_timers()
        table.show_round()
        Table.show_players(table.get_players("left"))
        Table.show_players(table.get_players("right"))
        Table.show_suspended_players(table.get_players("left"))
        Table.show_suspended_players(table.get_players("right"))
        table.show_buttons()
        if table.player_panel:
            table.player_panel.render()
        fps.draw()

    @main_window.event
    def on_key_release(symbol, modifiers):
        global fullscreen
        if symbol == key.SPACE:
            if table.time_out_timer is None:
                if not table.timer.running:
                    table.timer.start()
                    table.update_players_timers("start", table.get_players())
                else:
                    table.timer.pause()
                    table.update_players_timers("pause", table.get_players())
            else:
                if table.time_out_timer.running:
                    table.time_out_timer.pause()
                else:
                    table.time_out_timer.start()
        elif symbol == key.LEFT:
            table.team1.set_name(input("Type first team's name: "))
        elif symbol == key.RIGHT:
            table.team2.set_name(input("Type second team's name: "))
        elif symbol == key.UP:
            table.timer.set_time(int(input("Time: ")))
        elif symbol == key.A:
            table.advance_round(1)
        elif symbol == key.Z:
            table.advance_round(-1)
        elif symbol == key.ENTER and table.timer.finished:
            table.advance_round(1)
            table.timer.restart()
        elif symbol == key.T:
            if table.timer.running:
                table.team1.request_time_out()
                table.time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60, sound)  # 1 minute countdown
                table.timer.pause()
                table.update_players_timers("pause", table.get_players())
            if table.time_out_timer is not None:
                table.time_out_timer.start()
        elif symbol == key.Y:
            if table.timer.running:
                table.team2.request_time_out()
                table.time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60, sound)  # 1 minute countdown
                table.timer.pause()
                table.update_players_timers("pause", table.get_players())
            if table.time_out_timer is not None:
                table.time_out_timer.start()
        elif symbol == key.R:
            table.timer.restart()
            table.time_out_timer = None
            table.update_players_timers("release", table.get_players())
        elif symbol == key.F:
            if not fullscreen:
                main_window.set_fullscreen(True, width=WIDTH, height=HEIGHT)
                fullscreen = True
            else:
                main_window.set_fullscreen(False, width=WIDTH, height=HEIGHT)
                fullscreen = False
        elif symbol == key.W:
            if config.num_second_windows < 1:
                second_window.start()
        elif symbol == key.B:
            window0.menu_scene()
            main_window.close()
            second_window.second_window.close()

    @main_window.event
    def on_mouse_release(x, y, button, modifiers):
        if button == mouse.LEFT:
            # print('The left mouse button was pressed at ({}, {}).'.format(x, y))
            table.update_player_functionality(x, y)

    @main_window.event
    def on_mouse_motion(x, y, dx, dy):  # to update buttons' visuals
        for button in map(lambda player: player.get_button(), table.get_players("remained")):
            button.pressed(x, y)
        if table.player_panel:
            for button in table.player_panel.get_buttons():
                button.pressed(x, y)

    @main_window.event
    def on_close():
        pyglet.app.exit()

    icon1 = pyglet.image.load("..\\gfx\\icon1.png")  # window icons
    icon2 = pyglet.image.load("..\\gfx\\icon2.png")
    main_window.set_icon(icon1, icon2)
    main_window.set_visible(True)

    background = pyglet.image.load("..\\gfx\\table2.png")
    sound = pyglet.media.load("..\\sounds\\sound.wav", streaming=False)

    fullscreen = False
    fps = pyglet.clock.ClockDisplay()
    pyglet.clock.schedule_interval(table.update, 1 / 48)
