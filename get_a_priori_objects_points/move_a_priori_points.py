from pathlib import Path
import numpy as np
import cv_shared


def move_a_priori_points(
    input_points: np.ndarray,
    final_origin_point: np.ndarray,
    debug: bool,
    debug_filepath: Path,
) -> np.ndarray:
    prefix='\n\tfun:move_a_priori_points'
    output=input_points-final_origin_point
    if debug:
        result=f"""{prefix}
points in final origin:\n{output}"""
        cv_shared.append_value_to_file(result, debug_filepath)
    return output 
