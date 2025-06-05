from typing import overload

from numpy import float32, float64, int32, int64
from numpy.typing import NDArray

@overload
def move_mean(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_mean(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_median(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_median(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_max(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_max(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_min(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_min(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_sum(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_sum(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_std(
    a: NDArray[float32],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[float32]: ...
@overload
def move_std(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[float64]: ...
@overload
def move_var(
    a: NDArray[float32],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[float32]: ...
@overload
def move_var(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
    ddof: int = 0,
) -> NDArray[float64]: ...
@overload
def move_argmin(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_argmin(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_argmax(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_argmax(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
@overload
def move_rank(
    a: NDArray[float32], window: int, min_count: int | None = None, axis: int = -1
) -> NDArray[float32]: ...
@overload
def move_rank(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    window: int,
    min_count: int | None = None,
    axis: int = -1,
) -> NDArray[float64]: ...
