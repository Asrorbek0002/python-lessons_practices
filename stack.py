# # LIFO, Last in, First out
#
# class Stack:
#     """When the number enters first and the last goes out first """
#     def __init__(self):
#         """There are attributes"""
#         self.stack_list=[]
#
#     def get_add(self,value):
#          self.stack_list.append(value)
#
#     def get_remove(self):
#         return self.stack_list.pop()
#
#     def show(self):
#         return self.stack_list
#
#
#
# stack=Stack()
#
# stack.get_add(1)
# stack.get_add(2)
# stack.get_add(3)
# stack.get_add(4)
# #print(stack.show())
#
# stack.get_remove()
# #print(stack.show())
#
#
# # FIFO, First in, First out
#
# class Queue:
#     def __init__(self):
#         self.queue=[]
#
#     def get_add(self,queue):
#           self.queue.append(queue)
#
#     def get_remove(self):
#         return self.queue.pop()
#
#     def show(self):
#         return self.queue
#
# queue = Queue()
# queue.get_add(1)
# queue.get_add(2)
# queue.get_add(3)
# queue.get_add(4)
# print(queue.show())
#
# queue.get_remove()
# queue.get_remove()
# print(queue.show())



# LIFO, Last in , First out

# class Stack:
#     def __init__(self):
#         self.stack=[]
#
#     def set_add(self,add):
#         self.stack.append(add)
#
#     def get_stack(self):
#         return self.stack
#
#     def get_pop(self):
#         return self.stack.pop()
#
#     def get_show(self):
#         return self.stack
#
# stack=Stack()
#
# stack.set_add(1)
# stack.set_add(2)
# stack.set_add(3)
# stack.set_add(4)
# stack.set_add(5)
# stack.set_add(6)
# stack.set_add(7)
# stack.set_add(8)
# stack.set_add(9)
# stack.set_add(10)
# stack.set_add(11)
#
# print(stack.get_stack())
#
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
# print(stack.get_pop())
#
# print(stack.get_show())

# FIFO, First in , First out

class StackX:
    def __init__(self):
        self.stackX=[]

    def set_add(self,add):
        self.stackX.append(add)

    def get_stack(self):
        return self.stackX

    def get_remove(self):
        return self.stackX.pop(0)

    def get_show(self):
        return self.stackX


stack=StackX()

stack.set_add(1)
stack.set_add(2)
stack.set_add(3)
stack.set_add(4)
stack.set_add(5)
stack.set_add(6)
stack.set_add(7)
stack.set_add(8)
stack.set_add(9)
stack.set_add(10)
stack.set_add(11)

print(stack.get_stack())
print(stack.get_show())
print(stack.get_remove())
print(stack.get_show())









































