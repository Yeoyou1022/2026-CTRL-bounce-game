input.onButtonPressed(Button.A, function () {
    판1.change(LedSpriteProperty.X, -1)
    판2.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    판1.change(LedSpriteProperty.X, 1)
    판2.change(LedSpriteProperty.X, 1)
})
let 판2: game.LedSprite = null
let 판1: game.LedSprite = null
let 공1 = game.createSprite(randint(0, 10), 5)
판1 = game.createSprite(2, 0)
판2 = game.createSprite(2, 5)
basic.forever(function () {
    if (공1.isTouching(판1)) {
        공1.change(LedSpriteProperty.X, randint(0, 5))
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
    }
    if (공1.isTouching(판2)) {
        공1.change(LedSpriteProperty.X, randint(-5, 0))
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
        공1.change(LedSpriteProperty.Y, -1)
        basic.pause(1000)
    }
})
