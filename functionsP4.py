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

triangle = [[1], [1,1]]
def pascal(n):
	if n < 1:
            print("Error You Failed or invalid number of rows!")


pascal(1)
'''
output:
1
'''

pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''                                                              
