print("Starting")

import board

from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys

class MyKeyboard(KMKKeyboard):
    def __init__(self):

        encoder = RotaryioEncoder(
            pin_a=board.GP14,
            pin_b=board.GP15,
            divisor=2
        )
        col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP7)
        row_pins = (board.GP29,)
        diode_orientation = DiodeOrientation.COL2ROW
        key_config = [board.GP26, board.GP8]
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
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers()) 
keyboard.modules.append(MouseKeys())

encoder_map_l0 = [KC.MW_UP, KC.MW_DOWN]
matrix_map_l0 = [KC.SPACE, KC.N5, KC.N4, KC.N3, KC.N2, KC.N1]
single_key_map_l0 = [KC.TO(1), KC.B]


encoder_map_l1 = [KC.VOLU, KC.VOLD]
matrix_map_l1 = [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS]
single_key_map_l1 = [KC.TO(0), KC.MSTP]

keyboard.keymap = [(matrix_map_l0 + single_key_map_l0 + encoder_map_l0),
                   (matrix_map_l1 + single_key_map_l1 + encoder_map_l1)]


if __name__ == '__main__':
    keyboard.go()
