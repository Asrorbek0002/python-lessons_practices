# with open('pi.txt') as file:
#     pi=file.read()
#
# print(pi)
# print(type(pi))
# pi=pi.rstrip()
# print(pi)
# pi=pi.replace('\n','')
# print(pi)
# pi=float(pi)
# print(type(pi))


#filename='data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
#

# we read in list

filename='data/talabalar.txt'
with open(filename) as file:
    talabalar=file.readlines()

print(talabalar)

talabalar=[talaba.rstrip() for talaba in talabalar]
print(talabalar)








