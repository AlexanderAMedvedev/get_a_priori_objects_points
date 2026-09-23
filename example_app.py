from pathlib import Path

import numpy as np
import get_a_priori_objects_points

A_PRIORI_POINTS_FILEPATH = (
    Path(__file__).resolve().parent.parent
    / "data_find_back_holes/a_priori_objects_points.json"
)
DEBUG = True
DEBUG_FILEPATH = "get_a_priori_objects_points_debug.output"


def main() -> None:
    if DEBUG:
        open(DEBUG_FILEPATH, "w").close()
    get_a_priori_objects_points.get_a_priori_objects_points_pipeline(
        A_PRIORI_POINTS_FILEPATH, DEBUG, debug_filepath=DEBUG_FILEPATH,
    )

if __name__ == "__main__":
    main()
