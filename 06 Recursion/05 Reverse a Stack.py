'''
You are given a stack of integers. Your task is to reverse the stack using recursion. 
You may only use standard stack operations (push, pop, top/peek, isEmpty). 
You are not allowed to use any loop constructs or additional data structures like arrays or queues.
Your solution must modify the input stack in-place to reverse the order of its elements.
'''

def insertAtBottom(stack, x):

    if not stack:
        stack.append(x)
        return

    top = stack.pop()

    insertAtBottom(stack, x)

    stack.append(top)


def reverseStack(stack):

    if not stack:
        return stack

    top = stack.pop()

    reverseStack(stack)

    insertAtBottom(stack, top)
    
    
stack = [4,3,2,1]
reverseStack(stack)
print(stack)