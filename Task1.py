#This program contains the function 'convert_list_to_integer' which takes a list of integers and joins all the elements. 
#The fuction loops through the list of integers
# and uses the index of the element in the list to determine the place value of the number(number of zeros)
# then it adds all the numbers to get the desired output

def convert_list_to_integer(lst):
    """ This function takes a list of integers and joins the elements
        Arg: 
            -lst: list of integers values
        Return:
            - joined list elements of type integer
    """
    sum = 0
    for index, number in enumerate(lst):
        place_value = (number * (10 ** (len(lst) - index - 1))) 
        sum = sum + place_value  #first determine the number of zero's: (10 ** (len(lst) - index - 1), the multiply element value and add to sum
    return sum # For example, lst = [1,2,3] will be sum = 100 + 20 + 3

print(convert_list_to_integer([8,3,5,1])) #prints 8351
print(convert_list_to_integer([1, 22, 333, 4444])) #prints 1223334444
print("The answer to life:", convert_list_to_integer([4,2]))
