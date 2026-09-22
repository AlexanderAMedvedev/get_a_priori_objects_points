from pathlib import Path
import numpy as np

from get_a_priori_objects_points.move_a_priori_points import move_a_priori_points
from get_a_priori_objects_points.read_a_priori_points import read_a_priori_points


def get_a_priori_objects_points_pipeline(
    filepath: Path, debug: bool = False
) -> np.ndarray[np.ndarray]:

    initial_points, do_move_points, final_origin_point = read_a_priori_points(
        filepath,
        debug,
    )

    if not do_move_points:
        return initial_points

    final_points = move_a_priori_points(
        initial_points,
        final_origin_point,
        debug,
    )
    return final_points
