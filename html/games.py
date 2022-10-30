import turtle
import pygame
import sys
import random
import tkinter as tk
from threading import Lock
from pygame.locals import *
def pong():
    win = turtle.Screen()
    win.title("poing")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    #paddle a
    pa = turtle.Turtle()
    pa.speed(0)
    pa.shape("square")
    pa.color("white")
    pa.shapesize(stretch_wid=5,stretch_len=1)
    pa.penup()
    pa.goto(-350,0)
    #paddle b
    pb = turtle.Turtle()
    pb.speed(0)
    pb.shape("square")
    pb.color("white")
    pb.shapesize(stretch_wid=5,stretch_len=1)
    pb.penup()
    pb.goto(350,0)

    #ball
    b = turtle.Turtle()
    b.speed(0)
    b.shape("square")
    b.color("grey")
    b.penup()
    b.goto(0,0)
    b.dx = 0.1
    b.dy = 0.01
    #functions
    def pa_up():
        y = pa.ycor()
        y += 20
        pa.sety(y)

    def pa_down():
        y = pa.ycor()
        y -= 20
        pa.sety(y)

    def pb_up():
        y = pb.ycor()
        y += 20
        pb.sety(y)

    def pb_down():
        y = pb.ycor()
        y -= 20
        pb.sety(y)

    #keyboard binding
    win.listen()
    win.onkeypress(pa_up,"w")
    win.onkeypress(pa_down,"s")
    win.onkeypress(pb_up,"Up")
    win.onkeypress(pb_down,"Down")

    while True:
        win.update()

        #move the ball
        b.setx(b.xcor()+b.dx)
        b.sety(b.ycor()+b.dy)

        #border 
        if b.ycor()>290:
            b.sety(290)
            b.dy *= -1
        if b.ycor()<-290:
            b.sety(-290)
            b.dy *= -1
        if b.xcor()>390:
            b.goto(0,0)
            b.dx *= -1
        if b.xcor()<-390:
            b.goto(0,0)
            b.dx *= -1
        if pa.ycor()>290:
            pa.sety(290)
        if pa.ycor()<-290:
            pa.sety(-290)
        if pb.ycor()>290:
            pb.sety(290)
        if pb.ycor()<-290:
            pb.sety(-290)
        #collisions
        

def snakegame():
            class Snake():
                def __init__(self):
                    self.length = 1
                    self.positions = [((screen_width/2), (screen_height/2))]
                    self.direction = random.choice([up, down, left, right])
                    self.color = (17, 24, 47)
                    self.score = 0

                def get_head_position(self):
                    return self.positions[0]

                def turn(self, point):
                    if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
                        return
                    else:
                        self.direction = point

                def move(self):
                    cur = self.get_head_position()
                    x,y = self.direction
                    new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
                    if len(self.positions) > 2 and new in self.positions[2:]:
                        self.reset()
                    else:
                        self.positions.insert(0,new)
                        if len(self.positions) > self.length:
                            self.positions.pop()

                def reset(self):
                    self.length = 1
                    self.positions = [((screen_width/2), (screen_height/2))]
                    self.direction = random.choice([up, down, left, right])
                    self.score = 0

                def draw(self,surface):
                    for p in self.positions:
                        r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
                        pygame.draw.rect(surface, self.color, r)
                        pygame.draw.rect(surface, (93,216, 228), r, 1)

                def handle_keys(self):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                self.turn(up)
                            elif event.key == pygame.K_DOWN:
                                self.turn(down)
                            elif event.key == pygame.K_LEFT:
                                self.turn(left)
                            elif event.key == pygame.K_RIGHT:
                                self.turn(right)

            class Food():
                def __init__(self):
                    self.position = (0,0)
                    self.color = (20, 181, 63)
                    self.randomize_position()

                def randomize_position(self):
                    self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

                def draw(self, surface):
                    r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
                    pygame.draw.rect(surface, self.color, r)
                    pygame.draw.rect(surface, (93, 216, 228), r, 1)

            def drawGrid(surface):
                for y in range(0, int(grid_height)):
                    for x in range(0, int(grid_width)):
                        if (x+y)%2 == 0:
                            r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                            pygame.draw.rect(surface,(114, 24, 217), r)
                        else:
                            rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                            pygame.draw.rect(surface, (65, 38, 153), rr)

            screen_width = 500
            screen_height = 500

            gridsize = 25
            grid_width = screen_width/gridsize
            grid_height = screen_height/gridsize

            up = (0,-1)
            down = (0,1)
            left = (-1,0)
            right = (1,0)

            def main():
                pygame.init()

                clock = pygame.time.Clock()
                screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

                surface = pygame.Surface(screen.get_size())
                surface = surface.convert()
                drawGrid(surface)

                snake = Snake()
                food = Food()

                myfont = pygame.font.SysFont("monospace",16)

                while (True):
                    clock.tick(10)
                    snake.handle_keys()
                    drawGrid(surface)
                    snake.move()
                    if snake.get_head_position() == food.position:
                        snake.length += 1
                        snake.score += 1
                        food.randomize_position()
                    snake.draw(surface)
                    food.draw(surface)
                    screen.blit(surface, (0,0))
                    text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
                    screen.blit(text, (5,10))
                    pygame.display.update()

            main()
def tetris():
    COLORS = ['gray', 'lightgreen', 'pink', 'blue', 'orange', 'purple']

    class Tetris():
        FIELD_HEIGHT = 20
        FIELD_WIDTH = 10
        SCORE_PER_ELIMINATED_LINES = (0, 40, 100, 300, 1200)
        TETROMINOS = [
            [(0, 0), (0, 1), (1, 0), (1,1)], # O
            [(0, 0), (0, 1), (1, 1), (2,1)], # L
            [(0, 1), (1, 1), (2, 1), (2,0)], # J 
            [(0, 1), (1, 0), (1, 1), (2,0)], # Z
            [(0, 1), (1, 0), (1, 1), (2,1)], # T
            [(0, 0), (1, 0), (1, 1), (2,1)], # S
            [(0, 1), (1, 1), (2, 1), (3,1)], # I
        ]
        
        def __init__(self):
            self.field = [[0 for c in range(Tetris.FIELD_WIDTH)] for r in range(Tetris.FIELD_HEIGHT)]
            self.score = 0
            self.level = 0
            self.total_lines_eliminated = 0
            self.game_over = False
            self.move_lock = Lock()
            self.reset_tetromino()

        def reset_tetromino(self):
            self.tetromino = random.choice(Tetris.TETROMINOS)[:]
            self.tetromino_color = random.randint(1, len(COLORS)-1)
            self.tetromino_offset = [-2, Tetris.FIELD_WIDTH//2]
            self.game_over = any(not self.is_cell_free(r, c) for (r, c) in self.get_tetromino_coords())
        
        def get_tetromino_coords(self):
            return [(r+self.tetromino_offset[0], c + self.tetromino_offset[1]) for (r, c) in self.tetromino]

        def apply_tetromino(self):
            for (r, c) in self.get_tetromino_coords():
                self.field[r][c] = self.tetromino_color

            new_field = [row for row in self.field if any(tile == 0 for tile in row)]
            lines_eliminated = len(self.field)-len(new_field)
            self.total_lines_eliminated += lines_eliminated
            self.field = [[0]*Tetris.FIELD_WIDTH for x in range(lines_eliminated)] + new_field
            self.score += Tetris.SCORE_PER_ELIMINATED_LINES[lines_eliminated] * (self.level + 1)
            self.level = self.total_lines_eliminated // 10
            self.reset_tetromino()

        def get_color(self, r, c):
            return self.tetromino_color if (r, c) in self.get_tetromino_coords() else self.field[r][c]
        
        def is_cell_free(self, r, c):
            return r < Tetris.FIELD_HEIGHT and 0 <= c < Tetris.FIELD_WIDTH and (r < 0 or self.field[r][c] == 0)
        
        def move(self, dr, dc):
            with self.move_lock:
                if self.game_over:
                    return

                if all(self.is_cell_free(r + dr, c + dc) for (r, c) in self.get_tetromino_coords()):
                    self.tetromino_offset = [self.tetromino_offset[0] + dr, self.tetromino_offset[1] + dc]
                elif dr == 1 and dc == 0:
                    self.game_over = any(r < 0 for (r, c) in self.get_tetromino_coords())
                    if not self.game_over:
                        self.apply_tetromino()

        def rotate(self):
            with self.move_lock:
                if self.game_over:
                    self.__init__()
                    return

                ys = [r for (r, c) in self.tetromino]
                xs = [c for (r, c) in self.tetromino]
                size = max(max(ys) - min(ys), max(xs)-min(xs))
                rotated_tetromino = [(c, size-r) for (r, c) in self.tetromino]
                wallkick_offset = self.tetromino_offset[:]
                tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
                min_x = min(c for r, c in tetromino_coord)
                max_x = max(c for r, c in tetromino_coord)
                max_y = max(r for r, c in tetromino_coord)
                wallkick_offset[1] -= min(0, min_x)
                wallkick_offset[1] += min(0, Tetris.FIELD_WIDTH - (1 + max_x))
                wallkick_offset[0] += min(0, Tetris.FIELD_HEIGHT - (1 + max_y))

                tetromino_coord = [(r+wallkick_offset[0], c + wallkick_offset[1]) for (r, c) in rotated_tetromino]
                if all(self.is_cell_free(r, c) for (r, c) in tetromino_coord):
                    self.tetromino, self.tetromino_offset = rotated_tetromino, wallkick_offset

    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.tetris = Tetris()
            self.pack()
            self.create_widgets()
            self.update_clock()

        def update_clock(self):
            self.tetris.move(1, 0)
            self.update()  
            self.master.after(int(1000*(0.66**self.tetris.level)), self.update_clock)
        
        def create_widgets(self):
            PIECE_SIZE = 30
            self.canvas = tk.Canvas(self, height=PIECE_SIZE*self.tetris.FIELD_HEIGHT, 
                                          width = PIECE_SIZE*self.tetris.FIELD_WIDTH, bg="black", bd=0)
            self.canvas.bind('<Left>', lambda _: (self.tetris.move(0, -1), self.update()))
            self.canvas.bind('<Right>', lambda _: (self.tetris.move(0, 1), self.update()))
            self.canvas.bind('<Down>', lambda _: (self.tetris.move(1, 0), self.update()))
            self.canvas.bind('<Up>', lambda _: (self.tetris.rotate(), self.update()))
            self.canvas.focus_set()
            self.rectangles = [
                self.canvas.create_rectangle(c*PIECE_SIZE, r*PIECE_SIZE, (c+1)*PIECE_SIZE, (r+1)*PIECE_SIZE)
                    for r in range(self.tetris.FIELD_HEIGHT) for c in range(self.tetris.FIELD_WIDTH)
            ]
            self.canvas.pack(side="left")
            self.status_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24))
            self.status_msg.pack(side="top")
            self.game_over_msg = tk.Label(self, anchor='w', width=11, font=("Courier", 24), fg='red')
            self.game_over_msg.pack(side="top")
        
        def update(self):
            for i, _id in enumerate(self.rectangles):
                color_num = self.tetris.get_color(i//self.tetris.FIELD_WIDTH, i % self.tetris.FIELD_WIDTH)
                self.canvas.itemconfig(_id, fill=COLORS[color_num])
        
            self.status_msg['text'] = "Score: {}\nLevel: {}".format(self.tetris.score, self.tetris.level)
            self.game_over_msg['text'] = "GAME OVER.\nPress UP\nto reset" if self.tetris.game_over else ""

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
def gamemenu():
    print("[1]pong")
    print("[2]snake game")
    print("[3]tetris")
    print("[0]exit the program")
    uc = int(input("pls chose a game(1,2,3,)or exit the program"))
    if uc == 1:
        pong()
    elif uc == 2:
        snakegame()
    elif uc == 3:
        tetris()
    elif uc == 0:
        exit
    else:
        print()
        print("please enter either 1,2,3")
        gamemenu()
gamemenu()
