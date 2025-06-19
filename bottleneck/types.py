from numpy.typing import NDArray
import numpy as np

type IntScalar = np.int32 | np.int64
type FloatScalar = np.float32 | np.float64
type Float64OutScalar = IntScalar | np.float64
type NumericScalar = IntScalar | FloatScalar
type IntArray = NDArray[np.int32] | NDArray[np.int64]
type FloatArray = NDArray[np.float32] | NDArray[np.float64]
type Float64OutArray = NDArray[np.float64] | IntArray
type NumericArray = IntArray | FloatArray
