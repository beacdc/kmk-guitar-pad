print("Starting")

import board

from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.keypad import KeysScanner


encoder_map = [KC.MW_UP, KC.MW_DOWN]
matrix_map = [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.ESPACE]
single_key_map = [KC.B]


class MyKeyboard(KMKKeyboard):
    def __init__(self):

        encoder = RotaryioEncoder(
            pin_a=board.GP14,
            pin_b=board.GP15,
        )
        col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,)
        row_pins = (board.GP29,)
        diode_orientation = DiodeOrientation.COL2ROW
        key_config = [board.GP26]
        key_scanner = KeysScanner(
            # require argument:
            pins=key_config,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )
        matrix_scanner = MatrixScanner(
            column_pins=col_pins,
            row_pins=row_pins,
            columns_to_anodes=diode_orientation
        )
        self.matrix = [matrix_scanner, key_scanner, encoder]


keyboard = MyKeyboard()

# keyboard.modules.append(Layers())
keyboard.keymap = [matrix_map + single_key_map + encoder_map]


if __name__ == '__main__':
    keyboard.go()
