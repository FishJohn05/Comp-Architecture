"""Basic Pong movement and collision logic (no graphics or controls yet)."""

WIDTH = 640
HEIGHT = 400

ball_x = 320
ball_y = 200
ball_dx = 4
ball_dy = 3
ball_size = 10

left_paddle_y = 160
right_paddle_y = 160
paddle_height = 80
paddle_width = 12
left_paddle_x = 20
right_paddle_x = WIDTH - 20 - paddle_width


def move_ball():
    global ball_x, ball_y
    ball_x += ball_dx
    ball_y += ball_dy


def wall_collision():
    global ball_y, ball_dy
    if ball_y <= 0:
        ball_y = 0
        ball_dy = abs(ball_dy)
    elif ball_y + ball_size >= HEIGHT:
        ball_y = HEIGHT - ball_size
        ball_dy = -abs(ball_dy)


def paddle_collision():
    global ball_x, ball_dx
    if ball_dx < 0 and left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if ball_y + ball_size >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_dx = abs(ball_dx)
    elif ball_dx > 0 and right_paddle_x - ball_size <= ball_x <= right_paddle_x:
        if ball_y + ball_size >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x - ball_size
            ball_dx = -abs(ball_dx)


def update_game():
    move_ball()
    wall_collision()
    paddle_collision()


if __name__ == "__main__":
    for frame in range(30):
        update_game()
        print(f"Frame {frame + 1}: ball=({ball_x}, {ball_y})")
