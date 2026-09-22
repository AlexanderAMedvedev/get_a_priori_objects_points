import json
from pathlib import Path
import numpy as np


def read_a_priori_points(
    a_priori_points: Path, debug: bool = False
) -> tuple[np.ndarray, bool, np.ndarray] | None:
    prefix = "fun:read_a_priori_points"

    points_key = "points"
    do_move_points_key = "do_move_points"
    final_origin_point_key = "final_origin_point"
    final_origin_point = None
    try:
        with open(a_priori_points) as file:
            data = json.load(file)
            points: np.ndarray = np.array(data[points_key])
            do_move_points: bool = data[do_move_points_key]
            if do_move_points:
                final_origin_point: np.ndarray = np.array(
                    data[final_origin_point_key]
                )
            if debug:
                print(f"{prefix}")
                print(f"A priori points from file: {points}")
                print(f"Do move points flag: {do_move_points}")
                print(f"Final origin point: {final_origin_point}")

            return (points, do_move_points, final_origin_point)
    except (OSError, ValueError, KeyError) as error:
        print(f"FILE {a_priori_points} ISN'T PARSED ({error}),\n\
              CHECK THE INPUT FILE")
        return None
