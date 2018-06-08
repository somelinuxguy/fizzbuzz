# Python 3, of course.
for number in range(100):
  print("Working number {}".format(number))
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
# a new line to keep the output pretty.  
  print()