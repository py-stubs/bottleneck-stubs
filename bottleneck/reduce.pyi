from typing import overload

import numpy as np
from numpy.typing import NDArray

from bottleneck.types import (
    Float64OutArray,
    Float64OutScalar,
    NumericArray,
    NumericScalar,
)

@overload
def nansum[T: NumericScalar](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def nansum[T: NumericScalar](a: NDArray[T], axis: None = None) -> T: ...
@overload
def nanmean(a: NDArray[np.float32], axis: int) -> NDArray[np.float32]: ...
@overload
def nanmean(
    a: Float64OutArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def nanmean(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def nanmean[T: Float64OutScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanstd(a: NDArray[np.float32], axis: int, ddof: int = 0) -> NDArray[np.float32]: ...
@overload
def nanstd(
    a: Float64OutArray,
    axis: int,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def nanstd(a: NDArray[np.float32], axis: None = None, ddof: int = 0) -> np.float32: ...
@overload
def nanstd[T: Float64OutScalar](
    a: NDArray[T], axis: None = None, ddof: int = 0
) -> T: ...
@overload
def nanvar(a: NDArray[np.float32], axis: int, ddof: int = 0) -> NDArray[np.float32]: ...
@overload
def nanvar(
    a: Float64OutArray,
    axis: int,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def nanvar(a: NDArray[np.float32], axis: None = None, ddof: int = 0) -> np.float32: ...
@overload
def nanvar[T: Float64OutScalar](
    a: NDArray[T], axis: None = None, ddof: int = 0
) -> T: ...
@overload
def nanmin[T: NumericScalar](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def nanmin[T: NumericScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanmax[T: NumericScalar](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def nanmax[T: NumericScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def median(a: NDArray[np.float32], axis: int) -> NDArray[np.float32]: ...
@overload
def median(
    a: Float64OutArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def median(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def median[T: Float64OutScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanmedian(a: NDArray[np.float32], axis: int) -> NDArray[np.float32]: ...
@overload
def nanmedian(
    a: Float64OutArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def nanmedian(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def nanmedian[T: Float64OutScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def ss[T: Float64OutScalar](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def ss[T: Float64OutScalar](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanargmin(
    a: NumericArray,
    axis: int,
) -> NDArray[np.int64]: ...
@overload
def nanargmin(
    a: NumericArray,
    axis: None = None,
) -> np.int64: ...
@overload
def nanargmax(
    a: NumericArray,
    axis: int,
) -> NDArray[np.int64]: ...
@overload
def nanargmax(
    a: NumericArray,
    axis: None = None,
) -> np.int64: ...
@overload
def anynan(
    a: NumericArray,
    axis: None = None,
) -> bool: ...
@overload
def anynan(
    a: NumericArray,
    axis: int,
) -> NDArray[np.bool_]: ...
@overload
def allnan(
    a: NumericArray,
    axis: None = None,
) -> bool: ...
@overload
def allnan(
    a: NumericArray,
    axis: int,
) -> NDArray[np.bool_]: ...
