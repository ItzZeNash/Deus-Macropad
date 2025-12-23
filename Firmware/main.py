import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)


PINS = [
    board.A2,   # SW1 (GPIO28)
    board.A3,   # SW2 (GPIO29)
    board.SCK,  # SW3 (GPIO2)
    board.RX,   # SW4 (GPIO1)
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Switches pull to GND when pressed
    pull=True,                  # Enable internal pull-up resistors
)

keyboard.keymap = [
    [
        KC.LCTRL(KC.HOME),           # SW1 - Scroll to top (Ctrl+Home)
        KC.PGDN,                     # SW2 - Scroll down (Page Down)
        KC.MACRO("8808000"),         # SW3 - Type "8808000"
        KC.LCTRL(KC.LGUI(KC.LEFT)),  # SW4 - Ctrl+Win+Left Arrow
    ]
]

if __name__ == '__main__':
    keyboard.go()
