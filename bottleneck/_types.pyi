import numpy as np
from numpy.typing import NDArray

type IntScalar = np.int32 | np.int64
type FloatScalar = np.float32 | np.float64
type NumericScalar = IntScalar | FloatScalar
type IntArray = NDArray[np.int32] | NDArray[np.int64]
type FloatArray = NDArray[np.float32] | NDArray[np.float64]
type NumericArray = IntArray | FloatArray
