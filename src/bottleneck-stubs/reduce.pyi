from typing import overload

import numpy as np
from numpy.typing import NDArray

from ._types import IntArray, IntScalar, NumericArray, NumericScalar

@overload
def nansum[T: NumericScalar](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def nansum[T: NumericScalar](a: NDArray[T], axis: None = None) -> T: ...
@overload
def nanmean(a: NDArray[np.float32], axis: int) -> NDArray[np.float32]: ...
@overload
def nanmean(
    a: NDArray[np.float64] | IntArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def nanmean(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def nanmean[T: IntScalar | np.float64](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanstd(a: NDArray[np.float32], axis: int, ddof: int = 0) -> NDArray[np.float32]: ...
@overload
def nanstd(
    a: NDArray[np.float64] | IntArray,
    axis: int,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def nanstd(a: NDArray[np.float32], axis: None = None, ddof: int = 0) -> np.float32: ...
@overload
def nanstd[T: IntScalar | np.float64](
    a: NDArray[T], axis: None = None, ddof: int = 0
) -> T: ...
@overload
def nanvar(a: NDArray[np.float32], axis: int, ddof: int = 0) -> NDArray[np.float32]: ...
@overload
def nanvar(
    a: NDArray[np.float64] | IntArray,
    axis: int,
    ddof: int = 0,
) -> NDArray[np.float64]: ...
@overload
def nanvar(a: NDArray[np.float32], axis: None = None, ddof: int = 0) -> np.float32: ...
@overload
def nanvar[T: IntScalar | np.float64](
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
    a: NDArray[np.float64] | IntArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def median(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def median[T: IntScalar | np.float64](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def nanmedian(a: NDArray[np.float32], axis: int) -> NDArray[np.float32]: ...
@overload
def nanmedian(
    a: NDArray[np.float64] | IntArray,
    axis: int,
) -> NDArray[np.float64]: ...
@overload
def nanmedian(a: NDArray[np.float32], axis: None = None) -> np.float32: ...
@overload
def nanmedian[T: IntScalar | np.float64](
    a: NDArray[T],
    axis: None = None,
) -> T: ...
@overload
def ss[T: IntScalar | np.float64](a: NDArray[T], axis: int) -> NDArray[T]: ...
@overload
def ss[T: IntScalar | np.float64](
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
