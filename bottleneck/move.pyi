from typing import overload

import numpy as np
from numpy.typing import NDArray
from bottleneck.types import Float64OutArray

@overload
def move_mean(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_mean(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_median(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_median(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_max(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_max(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_min(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_min(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_sum(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_sum(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_std(
    a: NDArray[np.float32],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[np.float32]: ...
@overload
def move_std(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def move_var(
    a: NDArray[np.float32],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[np.float32]: ...
@overload
def move_var(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def move_argmin(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_argmin(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_argmax(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_argmax(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
@overload
def move_rank(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_rank(
    a: Float64OutArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
