from pathlib import Path

import numpy as np
import get_a_priori_objects_points

A_PRIORI_POINTS_FILEPATH = (
    Path(__file__).resolve().parent.parent
    / "data_find_back_holes/a_priori_objects_points.json"
)
DEBUG = True


def main() -> None:
    get_a_priori_objects_points.get_a_priori_objects_points_pipeline(
        A_PRIORI_POINTS_FILEPATH, DEBUG
    )

if __name__ == "__main__":
    main()
