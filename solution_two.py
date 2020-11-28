import math

class ArrayHelper:
  """
    Group array into n equal array sizes. 
    Each array is not guaranteed to be same size
    Returns an array of n size arrays
  """
  @classmethod
  def group_array(cls, array, n):
    if not array:
      raise ValueError("Empty array given")

    array_length = len(array)

    if n < 1:
      raise ValueError(f'{n} is invalid. n should be greater than 0')

    if n > array_length:
      raise ValueError(f'n = {n} is greater than array')

    group_size = 0
    remaining = 0
    
    max_divisor = math.ceil(math.sqrt(array_length))

    if n <= max_divisor:
      group_size = math.ceil(array_length / n)
      remaining = array_length % group_size
    else:
      group_size = array_length // n
      remaining = (array_length % n) + group_size

    if remaining > n and (remaining // 2) > group_size:
      group = remaining // n
      group_size += group
      remaining = n - group_size
      
    grouped_elements = []
    for i in range(0, array_length, group_size):
      if i == array_length - remaining:
        grouped_elements.append(array[i:])
        break
      else:
        grouped_elements.append(array[i:i + group_size])

    return grouped_elements

# Test data
input_empty = []
input_array_main = [1, 2, 3, 4, 5]
input_array_10 = [1,2,3,4,5,6,7,8,9,10]
input_array_20 = list(range(1, 21))
input_array_25 = list(range(1, 26))
input_array_77 = list(range(1, 78))
input_array_100 = list(range(1, 101))

for i in range(1, len(input_array_main) + 1):
  grouped_arrays = ArrayHelper.group_array(input_array_main, i)
  print(grouped_arrays)
  assert len(grouped_arrays) == i

for i in range(1, len(input_array_20) + 1):
  grouped_arrays = ArrayHelper.group_array(input_array_20, i)
  print(grouped_arrays)
  assert len(grouped_arrays) == i