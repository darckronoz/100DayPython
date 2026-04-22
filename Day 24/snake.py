from turtle import Turtle

tail_length = 0
tail = {}

class Snake:
    def __init__(self, player: Turtle):
        self.snake = player
        self.set_up_turtle()

    def set_up_turtle(self):
        self.snake.color("white")
        self.snake.penup()
        self.snake.speed(1)
        self.snake.shape("square")

    def increase_length(self):
        global tail_length
        tail_length += 1
        clone = self.snake.clone()
        if self.snake.heading() == 0:
            clone.goto(clone.xcor() - 20, clone.ycor())
        elif self.snake.heading() == 180:
            clone.goto(clone.xcor() + 20, clone.ycor())
        elif self.snake.heading() == 90:
            clone.goto(clone.xcor(), clone.ycor()-20)
        elif self.snake.heading() == 270:
            clone.goto(clone.xcor(), clone.ycor()+20)
        tail[tail_length] = clone


    def move_tail(self, latest):
        latest_pos = latest
        for i in range(1,tail_length+1):
            current = tail[i].position()
            tail[i].goto(latest_pos)
            latest_pos = current

    def move(self):
        position = self.snake.position()
        self.snake.forward(20)
        if len(tail) > 0:
            self.move_tail(position)

    def get_position(self):
        return self.snake.position()

    def go_up(self):
        if self.snake.heading() not in [90, 270]:
            self.snake.speed(0)
            self.snake.setheading(90)
            self.snake.heading()
            self.snake.speed(1)

    def go_down(self):
        if self.snake.heading() not in [90, 270]:
            self.snake.speed(0)
            self.snake.setheading(270)
            self.snake.heading()
            self.snake.speed(1)

    def go_right(self):
        if self.snake.heading() not in [0, 180]:
            self.snake.speed(0)
            self.snake.setheading(0)
            self.snake.heading()
            self.snake.speed(1)

    def go_left(self):
        if self.snake.heading() not in [0, 180]:
            self.snake.speed(0)
            self.snake.setheading(180)
            self.snake.heading()
            self.snake.speed(1)

    def validate_tail_hit(self):
        (snake_x, snake_y) = self.snake.position()
        for i in range(1,tail_length+1):
            (tail_x, tail_y) = tail[i].position()
            if int(snake_x) in range(int(tail_x)-10, int(tail_x)+10) and int(snake_y)  in range(int(tail_y)-10, int(tail_y)+10):
                return True
        return False

