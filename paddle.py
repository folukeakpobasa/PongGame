# create paddle
paddle =  Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    '''listen to keyspress and move up'''
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    '''listen to keyspress and move down'''
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

# def go_left():
#     '''listen to keyspress and move left'''
#     new_x = paddle.xcor() - 20
#     paddle.goto( new_x, paddle.ycor())

# def go_right():
#     '''listen to keyspress and move down'''
#     new_x = paddle.xcor() +  20
#     paddle.goto( new_x, paddle.ycor())
    