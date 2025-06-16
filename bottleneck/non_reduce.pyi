from typing import overload

import numpy as np
from numpy.typing import NDArray

from bottleneck.types import FloatArray, IntArray, NumericArray

@overload
def replace(a: IntArray, old: int, new: int) -> None: ...
@overload
def replace(a: FloatArray, old: float, new: float) -> None: ...
def rankdata(
    a: NumericArray,
    axis: int,
) -> NDArray[np.float64]: ...
def nanrankdata(
    a: NumericArray,
    axis: int,
) -> NDArray[np.float64]: ...
def partition[T: NumericArray](
    a: T,
    kth: int,
    axis: int | None = -1,
) -> T: ...
def argpartition(
    a: NumericArray,
    kth: int,
    axis: int | None = -1,
) -> NDArray[np.int64]: ...
def push[T: NumericArray](a: T, n: int | None = None, axis: int = -1) -> T: ...
