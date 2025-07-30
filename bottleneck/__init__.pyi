"""
# Bottleneck

Bottleneck is a collection of fast NumPy array functions written in C.

## Functions Reference

Bottleneck provides the following functions:

### Reduce

Functions that reduce the input array along the specified axis.

- nansum
- nanmean
- nanstd
- nanvar
- nanmin
- nanmax
- median
- nanmedian
- ss
- nanargmin
- nanargmax
- anynan
- allnan

### Non-Reduce

Functions that do not reduce the input array and do not take axis as input.

- replace

### Non-reduce with axis

Functions that do not reduce the input array but operate along a specified axis.

- rankdata
- nanrankdata
- partition
- argpartition
- push


### Moving Window

Functions that operate along a (1d) moving window.

- move_sum
- move_mean
- move_std
- move_var
- move_min
- move_max
- move_argmin
- move_argmax
- move_median
- move_rank

## Type aliases

- IntScalar: Represents a scalar integer, which can be either `np.int32` or `np.int64`.
- FloatScalar: Represents a scalar floating-point number, which can be either `np.float32` or `np.float64`.
- NumericScalar: Represents a scalar that can be either an integer (`np.int32` or `np.int64`) or a floating-point number (`np.float32` or `np.float64`).
- IntArray: Represents a NumPy array of integers, which can contain elements of type `np.int32` or `np.int64`.
- FloatArray: Represents a NumPy array of floating-point numbers, which can contain elements of type `np.float32` or `np.float64`.
- NumericArray: Represents a NumPy array that can contain elements of type `np.int32`, `np.int64`, `np.float32`, or `np.float64`.

These type aliases are purely internal for bottleneck type stubs writing convenience.

"""

from bottleneck.move import (
    move_argmax,
    move_argmin,
    move_max,
    move_mean,
    move_median,
    move_min,
    move_rank,
    move_std,
    move_sum,
    move_var,
)
from bottleneck.non_reduce import (
    argpartition,
    nanrankdata,
    partition,
    push,
    rankdata,
    replace,
)
from bottleneck.reduce import (
    allnan,
    anynan,
    median,
    nanargmax,
    nanargmin,
    nanmax,
    nanmean,
    nanmedian,
    nanmin,
    nanstd,
    nansum,
    nanvar,
    ss,
)

__all__ = [
    "move_argmax",
    "move_argmin",
    "move_mean",
    "move_median",
    "move_std",
    "move_var",
    "nanmax",
    "nanmean",
    "nanmin",
    "nanstd",
    "move_max",
    "move_min",
    "move_sum",
    "move_rank",
    "nansum",
    "nanmedian",
    "replace",
    "rankdata",
    "nanrankdata",
    "partition",
    "argpartition",
    "push",
    "nanargmin",
    "nanargmax",
    "anynan",
    "allnan",
    "median",
    "ss",
    "nanvar",
]
