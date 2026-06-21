def on_button_pressed_a():
    판1.change(LedSpriteProperty.X, -1)
    판2.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    판1.change(LedSpriteProperty.X, 1)
    판2.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

판2: game.LedSprite = None
판1: game.LedSprite = None
공1 = game.create_sprite(randint(0, 10), 5)
판1 = game.create_sprite(2, 0)
판2 = game.create_sprite(2, 5)

def on_forever():
    if 공1.is_touching(판1):
        공1.change(LedSpriteProperty.X, randint(0, 5))
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
    if 공1.is_touching(판2):
        공1.change(LedSpriteProperty.X, randint(-5, 0))
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
basic.forever(on_forever)
