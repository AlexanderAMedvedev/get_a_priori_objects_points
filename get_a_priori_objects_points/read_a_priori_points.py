import json
from pathlib import Path
import numpy as np


def read_a_priori_points(
    a_priori_points: Path, debug: bool = False
) -> tuple[np.ndarray, bool, np.ndarray, bool] | None:
    prefix = "\nfun:read_a_priori_points"

    points_key = "points"
    do_move_points_key = "do_move_points"
    final_origin_point_key = "final_origin_point"
    do_convert_mm_2_m_key = "do_convert_mm_2_m"
    final_origin_point = None
    try:
        with open(a_priori_points) as file:
            data = json.load(file)
            points: np.ndarray = np.array(data[points_key], dtype=np.float32)
            do_move_points: bool = data[do_move_points_key]
            if do_move_points:
                final_origin_point: np.ndarray = np.array(
                    data[final_origin_point_key], dtype=np.float32
                )
            do_convert_mm_2_m: bool = data[do_convert_mm_2_m_key]
            if debug:
                print(f"{prefix}")
                print(f"A priori points from file:\n {points}")
                print(f"Do move points flag: {do_move_points}")
                print(f"Final origin point: {final_origin_point}")
                print(f"do convert from mm to m flag: {do_convert_mm_2_m}")

            return (points, do_move_points, final_origin_point, do_convert_mm_2_m)
    except (OSError, ValueError, KeyError) as error:
        print(f"FILE {a_priori_points} ISN'T PARSED ({error}),\n\
              CHECK THE INPUT FILE")
        return None
