import PySimpleGUI as sg

RECTANGLE_HEIGHT, RECTANGLE_WIDTH = 150, 150
BOARD_HEIGHT, BOARD_WIDTH = 600, 600
layout = [
    [sg.Text("Baagchal ")],
    [sg.Graph(canvas_size=(700, 700), graph_bottom_left=(0, 0), graph_top_right=(700, 700),
              background_color='#8b5a2b', key='graph', enable_events=True)],
]





window = sg.Window('Baagchal', layout)
window.Finalize()

graph = window['graph']

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
        graph.DrawLine((x1, y1), (x2, y2), width=8)

    for i in range(4):
         for j in range(4):
             graph.DrawRectangle((x + i * RECTANGLE_WIDTH, y + j * RECTANGLE_HEIGHT), (x + (i + 1) * RECTANGLE_WIDTH, y + (j + 1) * RECTANGLE_HEIGHT), line_color='black', line_width=8)

    for i in range(4):
        for j in range(4):
             graph.DrawCircle((x + i * RECTANGLE_WIDTH, y + j * RECTANGLE_HEIGHT), 25,
                              fill_color="white")
             graph.DrawCircle((x + (i + 1) * RECTANGLE_WIDTH, y + (j + 1) * RECTANGLE_HEIGHT), 25,
                              fill_color='white')


obj2 =  graph.DrawCircle((10, 10), 25,
                              fill_color='white')
obj1 =  graph.DrawCircle((100, 100), 25,
                              fill_color='white')

# graph.TKCanvas
# graph.TKCanvas.tag_bind(obj2, '<Double-1>', lambda event : print(event))
# graph.TKCanvas.tag_bind(obj1, '<Double-1>', lambda event : print(event))
# print(dir(graph.TKCanvas))

graph.draw_image("board.png", location=(0,400))
# draw_board()

while True:
    event, values = window.read()
    # print(event)
    # draw_board()
    if event in [None, "Exit"]:
        break

    x, y = values["graph"]
    figures = graph.get_figures_at_location((x, y))
    graph.delete_figure(figures[0])
    print(type(figures[0]))