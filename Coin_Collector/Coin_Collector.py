from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

boy = Actor("boy")
boy.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
def draw():
    screen.fill("green")
    if not game_over:
        boy.draw()
        coin.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    else:
        screen.draw.text("Game Over", color="red", center=(WIDTH // 2, HEIGHT // 2), fontsize=50)
        screen.draw.text("Final Score: " + str(score), color="white", center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=30)
def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)
def time_up():
    global game_over
    game_over = True
def update():
    global score
    if not game_over:
        if keyboard.left:
            boy.x = max(0, boy.x - 2)
        if keyboard.right:
            boy.x = min(WIDTH, boy.x + 2)
        if keyboard.up:
            boy.y = max(0, boy.y - 2)
        if keyboard.down:
            boy.y = min(HEIGHT, boy.y + 2)
        if boy.colliderect(coin):
            score += 10
            place_coin()
clock.schedule(time_up, 10.0)
place_coin()
