from functools import partial

def mul (x:int,y:int):
    return x*y

mulBy2=partial(mul,2)

print(mulBy2(5))
