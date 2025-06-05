import bottleneck as bn
import numpy as np
from numpy.typing import NDArray

def main() -> None:
    data_example: list[int] = [1, 2, 3, 4, 6]

    arr_float: NDArray[np.float32] = np.ndarray(shape=data_example, dtype=np.float32)
    arr_int: NDArray[np.int32] = np.ndarray(shape=data_example, dtype=np.int32)
    mean: NDArray[np.float32] = bn.move_mean(a=arr_float, window=2)
    mean_int: NDArray[np.float64] = bn.move_mean(a=arr_int, window=2)
    print(mean)
    print(mean_int)

if __name__ == "__main__":
    main()