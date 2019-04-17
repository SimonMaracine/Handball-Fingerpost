import pyglet
from pyglet.window import key, mouse
import countdown
from table import Table, table, WIDTH, HEIGHT

main_window = pyglet.window.Window(WIDTH, HEIGHT, "Handball Score Table", vsync=True, visible=False)
icon1 = pyglet.image.load("..\\gfx\\icon1.png")  # window icons
icon2 = pyglet.image.load("..\\gfx\\icon2.png")
main_window.set_icon(icon1, icon2)
main_window.set_visible(True)

background = pyglet.image.load("..\\gfx\\table2.png")

closed = False
fps = pyglet.clock.ClockDisplay()
pyglet.clock.schedule_interval(table.update, 1 / 48)


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
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE and table.time_out_timer is None:
        if not table.timer.running:
            table.timer.start()
            table.update_players_timers("start", table.get_players())
        else:
            table.timer.pause()
            table.update_players_timers("pause", table.get_players())
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
        table.team1.request_time_out()
        if table.timer.running:
            table.time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
            table.timer.pause()
            table.update_players_timers("pause", table.get_players())
        if table.time_out_timer is not None:
            if not table.time_out_timer.running:
                table.time_out_timer.start()
            else:
                table.time_out_timer.pause()
    elif symbol == key.Y:
        table.team2.request_time_out()
        if table.timer.running:
            table.time_out_timer = countdown.Timer(WIDTH//2 - 82, HEIGHT//2 + 185, 55, 60)  # 1 minute countdown
            table.timer.pause()
            table.update_players_timers("pause", table.get_players())
        if table.time_out_timer is not None:
            if not table.time_out_timer.running:
                table.time_out_timer.start()
            else:
                table.time_out_timer.pause()
    elif symbol == key.R:
        table.timer.restart()
        table.time_out_timer = None
        table.update_players_timers("release", table.get_players())


@main_window.event
def on_mouse_press(x, y, button, modifiers):
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
