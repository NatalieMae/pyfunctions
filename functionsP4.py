numbers = [4, 45, 88, -5]

max_number = max(numbers)
print(max_number)

def mult_list(x):
    return x*3;
num1=5
num2=10
print("The product is: ", mult_list(num1 * num2) )

def rev_string(x):
    return x[::-1]
my_text = rev_string("How many times can you write HannaH backwards? ")
print(my_text)

def num_within(a, b, c):
    return a in range(b, c+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = [2]
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
pascal(5)