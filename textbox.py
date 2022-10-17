class TextBox:
    X = 0
    Y = 0
    H = 35
    W = 200
    text_size = 24

    # COLORS
    background_color = color(140, 140, 140)
    foreground_color = color(0, 0, 0)
    background_color_selected = color(160, 160, 160)
    border = color(30, 30, 30)

    border_enable = False
    border_weight = 1

    text_content = ""
    text_length = 0

    selected = False

    def __init__(self, x, y, w, h):
        self.X = x
        self.Y = y
        self.W = w
        self.H = h

    def draw(self):
        # drawing the background_color
        if self.selected:
            fill(self.background_color_selected)
        else:
            fill(self.background_color)

        if self.border_enable:
            strokeWeight(self.border_weight)
            stroke(self.border)
        else:
            noStroke()

        rect(self.X, self.Y, self.W, self.H)

        # drawing the text it self
        fill(self.foreground_color)
        textSize(self.text_size)
        text(self.text_content, self.X + (textWidth("a") / 2), self.Y + self.text_size)

    # if the keycode is ENTER return True else return False
    def key_pressed(self, KEY, KEYCODE):
        __is_key_captal_letter = False
        __is_key_small_letter = False
        __is_key_number = False

        if self.selected:
            if KEYCODE == BACKSPACE:
                self._backspace()

            elif KEYCODE == 32:  # SPACE
                self._addText(" ")

            elif KEYCODE == ENTER:
                return True
            else:
                # check is the key is a letter or a number
                __is_key_captal_letter = KEY >= "A" and KEY <= "Z"
                __is_key_small_letter = KEY >= "a" and KEY <= "z"
                __is_key_number = KEY >= "0" and KEY <= "9"

            if __is_key_captal_letter or __is_key_small_letter or __is_key_number:
                self._addText(KEY)

        return False

    def _addText(self, text):
        # if the width of the text is within the limits of the text box
        if textWidth(self.text_content + text) < self.W:
            self.text_content += text
            self.text_length += 1

    def _backspace(self):
        if self.text_length - 1 >= 0:
            self.text_content = self.text_content.substring(0, self.text_length - 1)
            self.text_length -= 1

    # method to test if the point is over the textbox
    def overBox(self, x, y):
        if x >= self.X and x <= self.X + self.W:
            if y >= self.Y and y <= self.Y + self.H:
                return True

        return False

    def pressed(self, x, y):
        if self.overBox(x, y):
            self.selected = True

        else:
            self.selected = False
