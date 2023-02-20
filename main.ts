input.onButtonPressed(Button.A, function () {
    if (lightspot.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        time_interval = time_interval - 50
    } else {
        game.gameOver()
    }
})
let time_interval = 0
let lightspot: game.LedSprite = null
lightspot = game.createSprite(2, 2)
time_interval = 600
basic.forever(function () {
    lightspot.move(1)
    lightspot.ifOnEdgeBounce()
    basic.pause(time_interval)
})
