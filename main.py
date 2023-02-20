def on_button_pressed_a():
    global time_interval
    if lightspot.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        time_interval = time_interval - 50
    else:
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

time_interval = 0
lightspot: game.LedSprite = None
lightspot = game.create_sprite(2, 2)
time_interval = 600

def on_forever():
    lightspot.move(1)
    lightspot.if_on_edge_bounce()
    basic.pause(time_interval)
basic.forever(on_forever)
