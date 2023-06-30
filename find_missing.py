def find_missing(input):
  input.sort()
  missing_number = -1
  for i in range(len(input)):
      if i+1 != int(input[i]):
          missing_number = i
  return missing_number
