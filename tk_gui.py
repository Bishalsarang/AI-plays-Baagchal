from tkinter import *
from collections import  namedtuple

RECTANGLE_HEIGHT, RECTANGLE_WIDTH = 150, 150
BOARD_HEIGHT, BOARD_WIDTH = 600, 600

grid = [['_' for _ in range(5)] for _ in range(5)]

graphic_board = [
                 [(20, 10), (170, 10), (320, 10), (470, 10), (620, 10)],
                 [(20, 160), (170, 160), (320, 160), (470, 160), (620, 160)],
                 [(20, 310), (170, 310), (320, 310), (470, 310), (620, 310)],
                 [(20, 460), (170, 460), (320, 460), (470, 460), (620, 460)],
                 [(20, 600), (170, 600), (320, 600), (470, 600), (620, 600)],
                 ]

# Place tiger at corners
grid[0][0] = grid[0][4] = grid[4][0] = grid[4][4] = 'T'
grid[0][1] = grid[1][4] = grid[4][3] = grid[4][1] = 'G'



Move = namedtuple("Move", "x y")

object_to_be_moved = None
move_from = Move(None, None)
move_to = Move(None, None)
selected = None

def graphics_coordinates_to_index(x, y):
    for i in range(5):
        for j in range(5):
            if graphic_board[i][j] == (x, y):
                return i, j


def onObjectClick(event):

    global move_from, move_to, object_to_be_moved, selected, grid
    # print(type(event.widget))
    print('Clicked', event.x, event.y, event.widget)
    obj = event.widget.find_closest(event.x, event.y, halo=5)
    print(canv.find_withtag(("blank")))
    print(canv.coords(obj))
    print((canv.itemconfigure(obj).get('tags')[4].split()[:2]))

    clicked_object_tag = canv.itemconfigure(obj).get('tags')[4].split()[0]
    print(clicked_object_tag)

    object_to_be_moved_tag = "blank"
    if object_to_be_moved is not None:
        object_to_be_moved_tag = canv.itemconfigure(object_to_be_moved).get('tags')[4].split()[0]
        if object_to_be_moved_tag.startswith("blank"):
            object_to_be_moved_tag = "blank"



    if move_from == (None, None):
        move_from = Move(*canv.coords(obj))
        selected = canv.create_rectangle(canv.bbox((clicked_object_tag)), outline="green", width=4, tag="selected")
        object_to_be_moved = obj
    elif object_to_be_moved_tag != "blank" and move_to == (None, None):
        move_to = Move(*canv.coords(obj))

        if move_from != move_to:
            # delete the target object
            canv.delete(canv.find_closest(move_to.x, move_to.y, halo=5))
            # delete the selected boc
            canv.delete(selected)

            row_1, col_1 = graphics_coordinates_to_index(*move_from)
            row_2, col_2 = graphics_coordinates_to_index(*move_to)
            if move_from.x == move_to.x and move_from.y != move_to.y:
                # Up ki down
                canv.move(object_to_be_moved, 0, (move_to.y - move_from.y))

            elif move_from.y == move_to.y and move_to.x != move_to.y:
                # Left or right
                canv.move(object_to_be_moved, (move_to.x - move_from.x), 0)
            else:
                # Move diagonally
                canv.move(object_to_be_moved, (move_to.x - move_from.x), (move_to.y - move_from.y))

            blank_3 = canv.create_image(move_from.x, move_from.y, image=blank_img, anchor=NW)
            canv.tag_bind(blank_3, '<Button-1>', onObjectClick)
            canv.update()
            print(f"Move {object_to_be_moved} from {move_from} to {move_to}")

        # delete the selected boc
        canv.delete(selected)
        move_from = Move(None, None)
        move_to = Move(None, None)
        object_to_be_moved = None
        selected = None
    else:
        canv.delete(selected)
        move_from = Move(None, None)
        move_to = Move(None, None)
        object_to_be_moved = None
        selected = None







root = Tk()
root.geometry("1024x768")
root.title("AI Plays Baagchal")
canv = Canvas(root, width=700, height=700, bg='#8b5a2b')

# Load blank image
blank_img = PhotoImage(file='blank_64x64.png')

tiger_img = PhotoImage(file='tigers/tiger_64x64.png')

goat_img = PhotoImage(file='goats/goat_64x64.png')


def draw_board(board):
    x, y = 50, 50

    # Contains coordinates


    def draw_lines():
        line_coordinates = [[(x, y), (x + BOARD_WIDTH, y + BOARD_HEIGHT)],
                            [(x + BOARD_WIDTH // 2, y), (x + BOARD_WIDTH, y + BOARD_HEIGHT // 2)],
                            [(x, y + BOARD_HEIGHT), (x + BOARD_WIDTH, y)],
                            [(x, y + BOARD_HEIGHT // 2), (x + BOARD_WIDTH // 2, y)],
                            [(x, y + BOARD_HEIGHT // 2), (x + BOARD_WIDTH // 2, y + BOARD_HEIGHT)],
                            [(x + BOARD_WIDTH // 2, y + BOARD_WIDTH),
                             (x + BOARD_WIDTH, y + BOARD_HEIGHT // 2)],
                            ]
        # Draw Lines
        for (x1, y1), (x2, y2) in line_coordinates:
            canv.create_line((x1, y1), (x2, y2), width=8)

    def draw_boxes():
        for i in range(4):
            for j in range(4):
                bottom_corner_coordinates = (x + i * RECTANGLE_WIDTH, y + j * RECTANGLE_HEIGHT)
                top_corner_coordinates = (
                x + (i + 1) * RECTANGLE_WIDTH, y + (j + 1) * RECTANGLE_HEIGHT)
                canv.create_rectangle(bottom_corner_coordinates, top_corner_coordinates, width=8)

    def draw_blank_buttons():
        corner_coordinates = set()
        init_x, init_y = 20, 10
        corner_coordinates.add((init_x, BOARD_HEIGHT))
        corner_coordinates.add((init_x + 4 * RECTANGLE_WIDTH, init_y))

        # Draw blank at each points
        for i in range(4):
            for j in range(4):
                corner_coordinates.add(
                    (init_x + i * RECTANGLE_WIDTH, init_y + j * RECTANGLE_HEIGHT))
                corner_coordinates.add(
                    (init_x + (i + 1) * RECTANGLE_WIDTH, init_y + (j + 1) * RECTANGLE_HEIGHT))


        for i, (x1, y1) in enumerate(corner_coordinates):
            blank = canv.create_image(x1, y1, image=blank_img, anchor=NW, tag="blank_" + str(i))
            canv.tag_bind(blank, '<Button-1>', onObjectClick)
            canv.tag_bind(blank, '<Button-2>', onObjectClick)

    def place_objects():

        tiger_cnt, goat_cnt, blank_cnt = 0, 0, 0
        for i in range(5):
            for j in range(5):
                x1, y1 = graphic_board[i][j]
                if board[i][j] == 'T':
                    tiger = canv.create_image(x1, y1, image=tiger_img, anchor=NW, tag="tiger_" + str(tiger_cnt))
                    canv.tag_bind(tiger, '<Button-1>', onObjectClick)
                    tiger_cnt += 1

                elif board[i][j] == 'G':
                    goat = canv.create_image(x1, y1, image=goat_img, anchor=NW,
                                              tag="goat_" + str(goat_cnt))
                    canv.tag_bind(goat, '<Button-1>', onObjectClick)
                    goat_cnt += 1
                else:
                    blank = canv.create_image(x1, y1, image=blank_img, anchor=NW,
                                              tag="blank_" + str(blank_cnt))
                    canv.tag_bind(blank, '<Button-1>', onObjectClick)
                    blank_cnt += 1

    draw_lines()
    draw_boxes()
    # draw_blank_buttons()
    place_objects()





draw_board(grid)
# # Load goat image

# goat_object = canv.create_image(600, 10, image=goat_img, anchor=NW, tag="goat")
#
#

# Load tiger image

#
# blank_1 = canv.create_image(175, 10, image=blank_img, anchor=NW)
# blank_2 = canv.create_image(315, 10, image=blank_img, anchor=NW)
# blank_3 = canv.create_image(455, 10, image=blank_img, anchor=NW)
# tiger_1 = canv.create_image(35, 10, image=tiger_img, anchor=NW, tag="tiger_1")
#
#
#
#
#
#
# canv.tag_bind(goat_object, '<Button-1>', onObjectClick)
# canv.tag_bind(tiger_1, '<Button-1>', onObjectClick)
# canv.tag_bind(blank_1, '<Button-1>', onObjectClick)
# canv.tag_bind(blank_2, '<Button-1>', onObjectClick)
# canv.tag_bind(blank_3, '<Button-1>', onObjectClick)


canv.pack()
root.mainloop()
