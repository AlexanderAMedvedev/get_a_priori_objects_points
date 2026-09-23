import copy
import numpy as np


def move_a_priori_points(
    input_points: np.ndarray,
    final_origin_point: np.ndarray,
    debug: bool = False,
) -> np.ndarray:
    prefix='\nfun:move_a_priori_points'
    output=input_points-final_origin_point
    if debug:
            print(f'{prefix}')
            print(f'points in final origin:\n {output}')
    return output 
