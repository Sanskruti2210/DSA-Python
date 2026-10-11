'''
Given a string num consisting of only digits and an integer target.Return all possibilities to insert 
the binary operators '+' , '*' , '-' between the digits of string nums, such that resultant expression 
evaluates to target value.
'''

def expression(index, num, n, result, path, target, value, prev):

    # Base case
    if index == n:

        if value == target:
            result.append(path)

        return

    # Try every possible number starting from index
    for i in range(index, n):

        # Avoid numbers with leading zero
        if i > index and num[index] == "0":
            break

        current = num[index:i + 1]

        # Convert string to integer
        current_num = int(current)

        # First number
        if index == 0:

            expression(i + 1,num,n,result,current,target,current_num,current_num)

        else:

            # +
            expression(i + 1,num,n,result,path + "+" + current,target,value + current_num,current_num)

            # -
            expression(i + 1,num,n,result,path + "-" + current,target,value - current_num,current_num)

            # *
            expression(i + 1,num,n,result,path + "*" + current,target,value - prev + prev * current_num,prev * current_num)


def add_operators(num, target):

    result = []

    expression(0,num,len(num),result,"",target,0,0)

    return result


num = "01"
target = 0

print(add_operators(num, target))
    
