# numpy

### ndarray运算

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
```

## numpy基本数学函数

### 1 计算平方根

```python

import numpy as np

print(np.sqrt(9))
print(np.sqrt([1, 4, 9]))

```

### 2 计算指数

```python
import numpy as np

print(np.exp(0))
```

### 3 计算对数

```python
import numpy as np

print(np.log(2.71828))
```

### 4 计算正值

```python 
import numpy as np

print(np.sin(np.pi / 2))
```

### 5 计算绝对值

```python
import numpy as np

print(np.abs(-1))
```

### 5 四舍五入

```python
import numpy as np

print(np.round([3.2, 4.5, 8.1, 9.6]))
```

### 6 向上取整

```python
import numpy as np

arr = np.array([1.6, 25.1, 81.7])
print(np.ceil(arr))
```

### 7 检测缺失值

```python

import numpy as np

print(np.isnan([1, 2, np.nan]))
```

## 统计函数

