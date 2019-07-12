import pyglet
from pyglet.window import key, mouse
from pyglet.gl import glEnable, glBlendFunc, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA

import src.countdown as countdown
from src.button import Button
from src.table import Table, table
import src.second_window as second_window
import src.window0 as window0
import src.config as config
from src.config import WIDTH, HEIGHT, icon1, icon2, background, \
    img1, img2, img3, img4, img5, ring_sound

main_window = None


def start():
    global main_window
    main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table", vsync=True, visible=False)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

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
        for button in buttons:
            button.render(False)
        if table.player_panel:
            table.player_panel.render()
        # fps.draw()

    @main_window.event
    def on_key_release(symbol, modifiers):
        nonlocal fullscreen
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
        elif symbol == key.A:
            table.advance_round(1)
        elif symbol == key.Z:
            table.advance_round(-1)
        elif symbol == key.T:
            if table.timer.running:
                table.team1.request_time_out()
                table.time_out_timer = countdown.Timer(WIDTH//2 - 94, HEIGHT//2 + 185, 55, 60, ring_sound)  # 1 minute countdown
                table.timer.pause()
                table.update_players_timers("pause", table.get_players())
            if table.time_out_timer is not None:
                table.time_out_timer.start()
        elif symbol == key.Y:
            if table.timer.running:
                table.team2.request_time_out()
                table.time_out_timer = countdown.Timer(WIDTH//2 - 94, HEIGHT//2 + 185, 55, 60, ring_sound)  # 1 minute countdown
                table.timer.pause()
                table.update_players_timers("pause", table.get_players())
            if table.time_out_timer is not None:
                table.time_out_timer.start()
        elif symbol == key.R:
            if table.timer.finished:
                table.advance_round(1)
                table.timer.restart()
            else:
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
            window0.start()
            window0.window0.activate()
            main_window.close()
            second_window.second_window.close()

    @main_window.event
    def on_mouse_release(x, y, button, modifiers):
        if button == mouse.LEFT:
            # print('The left mouse button was pressed at ({}, {}).'.format(x, y))
            table.update_player_functionality(x, y)
            if buttons[0].pressed(x, y):
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
            elif buttons[1].pressed(x, y):
                if table.timer.finished:
                    table.advance_round(1)
                    table.timer.restart()
                else:
                    table.timer.restart()
                    table.time_out_timer = None
                    table.update_players_timers("release", table.get_players())
            elif buttons[2].pressed(x, y):
                if table.timer.running:
                    table.team1.request_time_out()
                    table.time_out_timer = countdown.Timer(WIDTH // 2 - 94, HEIGHT // 2 + 185, 55, 60, ring_sound)  # 1 minute countdown
                    table.timer.pause()
                    table.update_players_timers("pause", table.get_players())
                if table.time_out_timer is not None:
                    table.time_out_timer.start()
            elif buttons[3].pressed(x, y):
                if table.timer.running:
                    table.team2.request_time_out()
                    table.time_out_timer = countdown.Timer(WIDTH // 2 - 94, HEIGHT // 2 + 185, 55, 60, ring_sound)  # 1 minute countdown
                    table.timer.pause()
                    table.update_players_timers("pause", table.get_players())
                if table.time_out_timer is not None:
                    table.time_out_timer.start()
            elif buttons[4].pressed(x, y):
                table.advance_round(1)
            elif buttons[5].pressed(x, y):
                table.advance_round(-1)

    @main_window.event
    def on_mouse_motion(x, y, dx, dy):  # to update buttons' visuals
        for button in map(lambda player: player.get_button(), table.get_players("remained")):
            button.pressed(x, y)
        if table.player_panel:
            for button in table.player_panel.get_buttons():
                button.pressed(x, y)
        for button in buttons:
            button.pressed(x, y)

    @main_window.event
    def on_close():
        pyglet.app.exit()

    main_window.set_icon(icon1, icon2)
    main_window.set_visible(True)

    start_stop = Button(265, 400, "", 0, image=img1, secondary_color=(200, 200, 200, 255))
    start_stop.width = img1.width
    start_stop.height = img1.height
    restart = Button(474, 400, "", 0, image=img2, secondary_color=(200, 200, 200, 255))
    restart.width = img2.width
    restart.height = img2.height
    time_out1 = Button(40, 375, "", 0, image=img3, secondary_color=(200, 200, 200, 255))
    time_out1.width = img3.width
    time_out1.height = img3.height
    time_out2 = Button(700, 375, "", 0, image=img3, secondary_color=(200, 200, 200, 255))
    time_out2.width = img3.width
    time_out2.height = img3.height
    round_up = Button(470, 360, "", 0, image=img4, secondary_color=(200, 200, 200, 255))
    round_up.width = img4.width
    round_up.height = img4.height
    round_down = Button(470, 315, "", 0, image=img5, secondary_color=(200, 200, 200, 255))
    round_down.width = img5.width
    round_down.height = img5.height

    buttons = (start_stop, restart, time_out1, time_out2, round_up, round_down)

    fullscreen = False
    # fps = pyglet.clock.ClockDisplay()
    pyglet.clock.schedule_interval(table.update, 1 / 48)
