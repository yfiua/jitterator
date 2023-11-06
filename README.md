# jitterator
A Python decorator that jitters the parameters of a function to test its robustness.

## Installation

```sh
pip install git+https://github.com/yfiua/jitterator
```
## Usage

Add the decorator `@jitterate(jitter, mode)` to the function. 

* `jitter` is the amount of jittering, which defaults to 0.05
* `mode` can be `'+'` (additive, default) or `'*'` (multiplicative)

For example:

```python
from jitterator import jitterate

def test_fun(x, y, z):
    return x + y * z

@jitterate(.01)
def test_fun_jittered(x, y, z):
    return test_fun(x, y, z)

x, y, z = 1, 2, 3

val = test_fun(x, y, z)
res_jittered = [test_fun_jittered(1, 2, 3) for i in range(10)]
vals_jittered, args_jittered = zip(*res_jittered)
```

You can then plot the jittered results.

The input parameters of the jittered function can be of different types such as numpy arrays, but must be additive or multiplicative, depending on the mode. For example

```python
def test_fun_np(x, y):
    return np.dot(x, y)

@jitterate(.01, '+')
def test_fun_np_jittered(x, y):
    return test_fun_np(x, y)

x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
```

![Example plot](example-plot.png)

## TODOs

* Separate jitters for different parameters
* Distribution of the jitter
