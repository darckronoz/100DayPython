#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import turtle

#Snake!
from gameScreen import GameScreen
from turtle import Screen, Turtle, ontimer
from snake import Snake

screen = Screen()
player = Turtle()
snake = Snake(player)
game = GameScreen(screen, snake)
screen.tracer(0,0)

def play_game():
    snake.move()
    game.evaluate_eat()
    if not game.evaluate_dead() and not snake.validate_tail_hit():
        screen.ontimer(play_game, 80)
    else:
        game.display_lose_screen()
    screen.update()

def main():

    screen.onkey(snake.go_up, "w")
    screen.onkey(snake.go_down, "s")
    screen.onkey(snake.go_left, "a")
    screen.onkey(snake.go_right, "d")

    play_game()

    screen.listen()
    screen.exitonclick()
    screen.mainloop()

if __name__ == "__main__":
    main()