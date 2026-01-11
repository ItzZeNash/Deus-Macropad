import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

# Add modules
macros = Macros()
keyboard.modules.append(macros)

# Reordered pins to match physical switches
PINS = [
    board.SDA,   # SW1
    board.SCL,   # SW2
    board.TX,    # SW3
    board.RX,    # SW4
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True,
    interval=0.02,
)

keyboard.keymap = [
    [
        KC.MACRO("8808000"),     # SW1 → Types "8808000"
        KC.MACRO(Press(KC.LGUI), Press(KC.LCTRL), Tap(KC.RIGHT), Release(KC.LCTRL), Release(KC.LGUI)),  # SW2 → Win+Ctrl+Right (SWAPPED)
        KC.MACRO(Press(KC.LGUI), Press(KC.LCTRL), Tap(KC.LEFT), Release(KC.LCTRL), Release(KC.LGUI)),   # SW3 → Win+Ctrl+Left (SWAPPED)
        KC.HOME,                 # SW4 → Home (top of page)
    ]
]

if __name__ == '__main__':
    keyboard.go()
