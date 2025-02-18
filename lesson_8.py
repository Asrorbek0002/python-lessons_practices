s# lambda haqida malumot

# def func(x,y):
#     return x+y
# print(func(2,5))

#multiply=lambda x,y:x*y
#print(multiply(2,2))

#multiple=lambda x : x%2==0
#print(multiple(2))

"""
map(func,itreble)
itreble=> dict,list,set
func=> def


"""

# def doubt(n):
#     return n*2
#
#numbers=[5,6,7,8]
# result=map(doubt,numbers)
# print(list(result))

#
# def is_even(n):
#     return n%2==0
#
# result = filter(is_even,numbers)
# print(list(result))

# m=list(map(lambda x,y:x*y,[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]))
# print(m)

#f=list(filter(lambda x:x%2!=0,[1,2,3,4,5,6,7,8,9]))
#print(f)


d={
    1:0,
    2:0,
    3:1,
    4:2,
    5:3
}
#
#
# m_d=list(map(lambda key,value:key+value,d.keys(),d.values()))

from functools import reduce

r=list(reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,0])) # 1+2=3 3+3=6 6+4=10
print(r)


















