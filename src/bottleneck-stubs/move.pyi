from typing import overload

import numpy as np
from numpy.typing import NDArray

from ._types import IntArray

@overload
def move_mean(
    a: NDArray[np.float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[np.float32]: ...
@overload
def move_mean(
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
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
    a: NDArray[np.float64] | IntArray,
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[np.float64]: ...
