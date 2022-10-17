from textbox import TextBox
from button import Button


buttons = []
text_boxes = []

locked = False
name = ""

# button submit action
def btn_submit_method():
    print("pressed")


def setup():
    size(400, 250)

    # text
    text_box = TextBox(100, 103, 200, 35)
    text_box.border_enable = True
    text_boxes.append(text_box)

    # Buttons
    submit_btn = Button(100, 143, 200, 35)
    submit_btn.button_text = "Submit!"
    submit_btn.action = btn_submit_method
    buttons.append(submit_btn)


def draw():
    background(40, 160, 40)

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
        print("oi")
        t.key_pressed(key, keyCode)
