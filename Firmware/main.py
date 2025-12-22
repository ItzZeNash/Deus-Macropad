import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.A0,  # SW1
    board.A1,  # SW2
    board.A2,  # SW3
    board.A3,  # SW4
    board.D6,  # SW5
    board.D7,  # SW6
    board.D0,  # SW7
    board.D1,  # SW8
    board.D2,  # SW9
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [
    [
        KC.ESC,                     # SW1
        KC.TAB,                     # SW2
        KC.MACRO("8808000"),   # SW3

        KC.LCTRL(KC.C),             # SW4
        KC.LCTRL(KC.V),             # SW5
        KC.LCTRL(KC.Z),             # SW6

        KC.MEDIA_PLAY_PAUSE,        # SW7
        KC.MEDIA_NEXT_TRACK,        # SW8
        KC.MEDIA_PREV_TRACK,        # SW9
    ]
]

if __name__ == '__main__':
    keyboard.go()
