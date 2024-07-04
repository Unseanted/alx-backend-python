#!/usr/bin/env python3
'''Task 102 module.
'''

from typing import List, Tuple, Union

def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2) -> List[Union[int, float]]:
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # Changed to a tuple to match the expected input type

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

# Checking the annotations
print(zoom_array.__annotations__)

