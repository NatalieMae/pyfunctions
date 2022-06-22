def hello():
    print("Hello my Peeps!")

def pack():
    print([1, 2, 3] )

hello()
pack()

def eat_lunch(*food_list):
    for i in food_list:
        print(i)
    if food_list == "Banana's":
        print("First I eat " + food_list[0])
    elif food_list == "Ham Sandwich":
        print("Next I eat " + food_list[1])
    else: 
        return ("My lunchbox is empty!")

eat_lunch([])