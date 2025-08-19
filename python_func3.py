def get_tub_son(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        return False
    return True


#print(get_tub_son(11))


