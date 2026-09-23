from pathlib import Path
import numpy as np

from get_a_priori_objects_points.move_a_priori_points import move_a_priori_points
from get_a_priori_objects_points.read_a_priori_points import read_a_priori_points


def get_a_priori_objects_points_pipeline(
    filepath: Path, debug: bool = False
) -> np.ndarray[np.ndarray]:
    prefix = "\nfun:get_a_priori_objects_points_pipeline"
    MM_2_M_CONVERSION_FACTOR: np.float32 = 0.001
    initial_points, do_move_points, final_origin_point, do_convert_mm_2_m = (
        read_a_priori_points(
            filepath,
            debug,
        )
    )

    if (not do_move_points) and (not do_convert_mm_2_m):
        if debug:
            print(prefix)
            print(f"do_convert_mm_2_m flag: {do_convert_mm_2_m}")
            print(f"initial_points:")
            print(f"{initial_points}")
        return initial_points
    if (not do_move_points) and do_convert_mm_2_m:
        initial_points = initial_points * MM_2_M_CONVERSION_FACTOR
        if debug:
            print(prefix)
            print(f"do_convert_mm_2_m flag: {do_convert_mm_2_m}")
            print(f"initial_points:")
            print(f"{initial_points}")
        return initial_points
    # do_move_points=True case:
    final_points = move_a_priori_points(
        initial_points,
        final_origin_point,
        debug,
    )

    if do_convert_mm_2_m:
        final_points = final_points * MM_2_M_CONVERSION_FACTOR

    if debug:
        print(prefix)
        print(f"do_convert_mm_2_m flag: {do_convert_mm_2_m}")
        print(f"final_points:")
        print(f"{final_points}")

    return final_points
