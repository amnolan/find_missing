def find_missing(input):
  # first find the "actual" sum of elements in the array
  sum_elems = sum(input)

  # then get the expected length of the array (assuming one item is missing, we increase by one to get the "expected" length)
  n = len(input) + 1

  # calculate the expected value, assuming a sequence where each number appears only once
  expected_sum = (n * (n + 1) ) / 2

  # subtract the difference to find the missing value (thus find the missing number in the array)
  return expected_sum - sum_elems 
