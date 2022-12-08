from turtle import Turtle
# from turtle import Screen 

# create paddle
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
    
    
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    


    def go_up(self):
        '''listen to keyspress and move up'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''listen to keyspress and move down'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # # def go_left():
    # #     '''listen to keyspress and move left'''
    # #     new_x = paddle.xcor() - 20
    # #     paddle.goto( new_x, paddle.ycor())

    # # def go_right():
    # #     '''listen to keyspress and move down'''
    # #     new_x = paddle.xcor() +  20
    # #     paddle.goto( new_x, paddle.ycor())
    # # activate keyspress
    
    # # screen.listen()
    # # screen.onkey(go_up, 'Up')
    # # screen.onkey(go_down, 'Down')
