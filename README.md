# Bottleneck stubs

## How to install
This project is managed with UV. If you have it, simply run:

    uv add git+https://github.com/OutSquareCapital/bn-typed.git

## How to use
This is just a stub package, who will allow type checking with pylance, and (most likely) mypy, pyright etc.. I don't use those so idk.
Since bottleneck recommend to use float and int 32/64 (because all others types aren't speeded up by the library), all other dtypes will warn about typing errors. All funcs are, so far, implemented like that:
```python
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
```
This allow dynamic type detection, so you can know know your in-> out results. I personally hate silent type casting at runtime.
Now your app take 2x more memory because a silent float32->float64 has been done at step 65/129 in your pipeline. 

## Example
**Edit: I just realized that I don't even know how to instanciate ndarrays correctly (or my sleep schedule is too messed up), because I passed the list as the shape, so the arrays were filled with unrelated values. However the "dtype" arg is what concerns us here so it doesn't matter too much.
### No type hints problem
Even if bottleneck doesn't spam pylance with errors anymore, and you get nice autocomplete + funcs signatures at dev time, you still need to use types hints from the numpy typing package to make it work correctly:
```python
import bottleneck as bn
import numpy as np
from numpy.typing import NDArray

data_example: list[int] = [1, 2, 3, 4, 6]

arr_float = np.ndarray(shape=data_example, dtype=np.float32)
arr_int = np.ndarray(shape=data_example, dtype=np.int32)
# Ruff suggest NDArray[float32], which is correct
mean = bn.move_mean(a=arr_float, window=2)
# Ruff suggest NDArray[float32], which is NOT correct, should be float64
mean_int = bn.move_mean(a=arr_int, window=2)
# Ruff suggest Any, which is always correct I guess, but not very helpful
mean_list = bn.move_mean(a=data_example, window=2)

print(mean)
print(mean_int)
print(mean_list)
```

Pylance will complain (a few examples below)
```
Type of "arr_float" is partially unknown
  Type of "arr_float" is "ndarray[Unknown, Unknown]"
Type of "arr_int" is partially unknown
  Type of "arr_int" is "ndarray[Unknown, Unknown]"
Argument type is partially unknown
  Argument corresponds to parameter "a" in function "move_mean"
  Argument type is "ndarray[Unknown, Unknown]"
Argument type is partially unknown
  Argument corresponds to parameter "a" in function "move_mean"
  Argument type is "ndarray[Unknown, Unknown]"
Argument of type "list[int]" cannot be assigned to parameter "a" of type "NDArray[int32] | NDArray[int64] | NDArray[float64]" in function "move_mean"
  Type "list[int]" is not assignable to type "NDArray[int32] | NDArray[int64] | NDArray[float64]"
    "list[int]" is not assignable to "ndarray[_Shape, dtype[int32]]"
    "list[int]" is not assignable to "ndarray[_Shape, dtype[int64]]"
    "list[int]" is not assignable to "ndarray[_Shape, dtype[float64]]"
......
```

Even if the final output works
```python
float32
float64
float64
[nan 1.5 2.5 3.5 5. ]
[[[[[           nan  8.0481615e-40  6.6787006e-39 -3.5263642e-30
     -4.7123581e-27  3.7899877e-18]
    [           nan  1.6144600e+30  0.0000000e+00  1.2676506e+30
      1.2676506e+30  0.0000000e+00]
    [           nan  3.6412147e-34  1.2676506e+30  1.2676506e+30
      1.8185267e+27  2.4118489e+27]
    [           nan  2.3327234e-32  5.0706024e+30  5.0706024e+30
      0.0000000e+00  6.8642045e-40]]

   [[           nan  2.8215511e-36  1.3675956e-38  3.6434661e-34
      3.6433274e-34  0.0000000e+00]
    [           nan  5.6043665e+34  0.0000000e+00  8.3797648e-43]]]]]
# Stopping here for brevity sake
```
### Solution
If you add the NDArray type hints from the numpy.typing package, everything works.
```python
arr_float: NDArray[np.float32] = np.ndarray(shape=data_example, dtype=np.float32)
arr_int: NDArray[np.int32] = np.ndarray(shape=data_example, dtype=np.int32)
# unchanged here
mean = bn.move_mean(a=arr_float, window=2)
# Now  Ruff suggest NDArray[float64], correct!
mean_int = bn.move_mean(a=arr_int, window=2)
# the rest is unchanged, mean_list still throw warnings, which is desired behavior
```

## Contributions, licences, etc...

Contributions welcome! Idk anything about licences and all that so I'll leave it blank atm.