from tkinter import *
from collections import  namedtuple

RECTANGLE_HEIGHT, RECTANGLE_WIDTH = 150, 150
BOARD_HEIGHT, BOARD_WIDTH = 600, 600

grid = [['_' for _ in range(6)] for _ in range(6)]
# Place tiger at corners
grid[0][0] = grid[0][5] = grid[5][0] = grid[5][5] = 'T'


Move = namedtuple("Move", "x y")

object_to_be_moved = None
move_from = Move(None, None)
move_to = Move(None, None)
selected = None

def onObjectClick(event):
    global move_from, move_to, object_to_be_moved, selected
    # print(type(event.widget))
    print('Clicked', event.x, event.y, event.widget)
    obj = event.widget.find_closest(event.x, event.y)
    print(canv.coords(obj))


    print(obj)
    if move_from == (None, None):
        move_from = Move(*canv.coords(obj))
        selected = canv.create_rectangle(canv.bbox("tiger_1"), outline="green", width=4, tag="selected")
        object_to_be_moved = obj
    elif move_to == (None, None):
        move_to = Move(*canv.coords(obj))

        if move_from != move_to:
            # delete the object
            canv.delete(canv.find_closest(move_to.x, move_to.y, halo=5))
            canv.delete(selected)

            if move_from.x == move_to.x and move_from.y != move_to.y:
                # Up ki down
                canv.move(object_to_be_moved, 0, (move_to.y - move_from.y))

            elif move_from.y == move_to.y and move_to.x != move_to.y:
                # Left or right
                canv.move(object_to_be_moved, (move_to.x - move_from.x), 0)

            blank_3 = canv.create_image(move_from.x, move_from.y, image=blank_img, anchor=NW)
            canv.tag_bind(blank_3, '<Button-1>', onObjectClick)
            canv.update()
            print(f"Move {object_to_be_moved} from {move_from} to {move_to}")
        move_from = Move(None, None)
        move_to = Move(None, None)
        object_to_be_moved = None
        selected = None








root = Tk()
root.geometry("1024x768")
root.title("AI Plays Baagchal")
canv = Canvas(root, width=700, height=700, bg='#8b5a2b')

def draw_board():
    x, y = 50, 50
    coordinates = [[(x, y), (x + BOARD_WIDTH, y + BOARD_HEIGHT)],
                  [(x + BOARD_WIDTH // 2, y), (x + BOARD_WIDTH, y + BOARD_HEIGHT // 2)],
                   [(x, y + BOARD_HEIGHT), (x + BOARD_WIDTH, y)],
                   [(x, y + BOARD_HEIGHT // 2), (x + BOARD_WIDTH // 2, y)],
                   [(x, y + BOARD_HEIGHT // 2), (x + BOARD_WIDTH // 2, y + BOARD_HEIGHT)],
                   [(x + BOARD_WIDTH // 2, y + BOARD_WIDTH), (x + BOARD_WIDTH, y + BOARD_HEIGHT // 2)],
                   ]
    for (x1, y1), (x2, y2) in coordinates:
        canv.create_line((x1, y1), (x2, y2), width=8)

    for i in range(4):
         for j in range(4):
             canv.create_rectangle((x + i * RECTANGLE_WIDTH, y + j * RECTANGLE_HEIGHT), (x + (i + 1) * RECTANGLE_WIDTH, y + (j + 1) * RECTANGLE_HEIGHT), width=8)

    # for i in range(4):
    #     for j in range(4):
    #          canv.create_oval((x + i * RECTANGLE_WIDTH, y + j * RECTANGLE_HEIGHT), 5, 5,
    #                           )
    #          canv.create_oval((x + (i + 1) * RECTANGLE_WIDTH, y + (j + 1) * RECTANGLE_HEIGHT), 5, 5,
    #                           )


draw_board()
# Load goat image
goat_img = PhotoImage(file='goats/goat_64x64.png')
goat_object = canv.create_image(600, 10, image=goat_img, anchor=NW, tag="goat")

# Load blank image
blank_img = PhotoImage(file='blank_64x64.png')

# Load tiger image
tiger_img = PhotoImage(file='tigers/tiger_64x64.png')

blank_1 = canv.create_image(170, 10, image=blank_img, anchor=NW)
blank_2 = canv.create_image(310, 10, image=blank_img, anchor=NW)
blank_3 = canv.create_image(455, 10, image=blank_img, anchor=NW)
tiger_1 = canv.create_image(35, 10, image=tiger_img, anchor=NW, tag="tiger_1")






canv.tag_bind(goat_object, '<Button-1>', onObjectClick)
canv.tag_bind(tiger_1, '<Button-1>', onObjectClick)
canv.tag_bind(blank_1, '<Button-1>', onObjectClick)
canv.tag_bind(blank_2, '<Button-1>', onObjectClick)
canv.tag_bind(blank_3, '<Button-1>', onObjectClick)


canv.pack()
root.mainloop()
