class FibonacciIterator:
  def __init__(self, max_value=None):
    self.a, self.b = 0, 1
    self.max_value = max_value

  def __iter__(self):
    return self

  def __next__(self):
    result = self.a
    self.a, self.b = self.b, self.a + self.b
    if self.max_value is not None and self.a > self.max_value:
      raise StopIteration
    return result

fibonacci = FibonacciIterator(20)

for x in fibonacci:
  print(x)
