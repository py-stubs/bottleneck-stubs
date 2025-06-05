from typing import overload

from numpy import float32, float64, int32, int64
from numpy.typing import NDArray

@overload
def nansum(a: NDArray[float32], axis: int | None = None) -> NDArray[float32]: ...
@overload
def nansum(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64], axis: int | None = None
) -> NDArray[float64]: ...
@overload
def nanmean(a: NDArray[float32], axis: int | None = None) -> NDArray[float32]: ...
@overload
def nanmean(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64], axis: int | None = None
) -> NDArray[float64]: ...
@overload
def nanmedian(a: NDArray[float32], axis: int | None = None) -> NDArray[float32]: ...
@overload
def nanmedian(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64], axis: int | None = None
) -> NDArray[float64]: ...
@overload
def nanstd(
    a: NDArray[float32], axis: int | None = None, ddof: int = 0
) -> NDArray[float32]: ...
@overload
def nanstd(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64],
    axis: int | None = None,
    ddof: int = 0,
) -> NDArray[float64]: ...
@overload
def nanmin(a: NDArray[float32], axis: int | None = None) -> NDArray[float32]: ...
@overload
def nanmin(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64], axis: int | None = None
) -> NDArray[float64]: ...
@overload
def nanmax(a: NDArray[float32], axis: int | None = None) -> NDArray[float32]: ...
@overload
def nanmax(
    a: NDArray[int32] | NDArray[int64] | NDArray[float64], axis: int | None = None
) -> NDArray[float64]: ...
