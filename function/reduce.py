#reduce():applies a function to an iterable and reduce it to a ssingle cumulative value.
#performs function on first two element and repeat process until 1 value remians
#reuce(function, iterable)

import functools
# letters=["H","E","L","L","O"]
# word=functools.reduce(lambda x,y,: x+y,letters)
# print(word)

factorial=[5,4,3,2,1]
result=functools.reduce(lambda x,y:x*y,factorial)
print(result)

