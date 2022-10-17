from textbox import TextBox
from button import Button

MIN_X_POSITION = 120  # do not allow shape to overlap the form
MAX_X_POSITION = 250
MAX_Y_POSITION = 400

buttons = []
text_boxes = []

locked = False
name = ""

# button submit action
def btn_create_circle_method(y, x, h):
    try:
        _x = int(x) + int(MIN_X_POSITION)
        _x = _x if _x <= MAX_X_POSITION else MAX_X_POSITION
        _y = y if y >= MAX_Y_POSITION else MAX_Y_POSITION

        circle(int(_y), int(_x), int(h))
    except Exception as error:
        print(error)
        pass


def btn_create_square_method(y, x, w, h):
    try:
        _x = int(x) + int(MIN_X_POSITION)
        _x = _x if _x <= MAX_X_POSITION else MAX_X_POSITION
        _y = y if y >= MAX_Y_POSITION else MAX_Y_POSITION

        rect(int(_y), int(_x), int(w), int(h))
    except Exception as error:
        print(error)
        pass


def setup():
    size(400, 250)

    # TEXT
    textSize(24)
    fill(0, 0, 0)

    text("Y", 8, 32)
    text("X", 160, 32)
    text("Height", 8, 64)
    text("Width", 160, 64)

    # TEXTBOX
    text_box_y = TextBox(80, 8, 60, 30)
    text_box_y.border_enable = True

    text_box_x = TextBox(220, 8, 60, 30)
    text_box_x.border_enable = True

    text_box_height = TextBox(80, 40, 60, 30)
    text_box_height.border_enable = True

    text_box_widht = TextBox(220, 40, 60, 30)
    text_box_widht.border_enable = True

    text_boxes.append(text_box_x)
    text_boxes.append(text_box_y)
    text_boxes.append(text_box_height)
    text_boxes.append(text_box_widht)

    # BUTTONS
    btn_circle = Button(8, 80, 100, 30)
    btn_circle.button_text = "Circle"
    btn_circle.action = lambda: btn_create_circle_method(
        text_box_y.text_content, text_box_x.text_content, text_box_height.text_content
    )

    btn_square = Button(120, 80, 100, 30)
    btn_square.button_text = "Square"
    btn_square.action = lambda: btn_create_square_method(
        text_box_y.text_content,
        text_box_x.text_content,
        text_box_height.text_content,
        text_box_widht.text_content,
    )

    buttons.append(btn_circle)
    buttons.append(btn_square)


def draw():
    # draw the textboxes
    for t in text_boxes:
        t.draw()

    # draw the buttons
    for b in buttons:
        b.draw()


# this is a default method of processing
def mousePressed():
    for t in text_boxes:
        t.pressed(mouseX, mouseY)

    for b in buttons:
        b.pressed(mouseX, mouseY)


# this is a default method of processing
def mouseReleased():
    for b in buttons:
        b.released()


# this is a default method of processing
def keyPressed():
    for t in text_boxes:
        t.key_pressed(key, keyCode)
