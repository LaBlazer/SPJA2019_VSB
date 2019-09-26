import math, itertools

def spherical_sector(r, h):
    if isinstance(r, (int, float)) and isinstance(h, (int, float)):
        return (2*math.pi*r*r*h)/3
    return False

def sqr(nums, pow):
    if isinstance(nums, list):
        return [i**pow for i in nums if isinstance(i, (int, float))]
    elif isinstance(nums, (int, float)):
        return nums**pow
    return False

def shuffle(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return ''.join(''.join(letter) for letter in itertools.zip_longest(str1, str2, fillvalue=''))
    return False

print(spherical_sector(10, 20))
print(spherical_sector(3.3, 5.2))
print(spherical_sector("x", 550))
print(sqr([1, 2, 3, 4], 3))
print(sqr([1, "hehe", 3, 4], 3))
print(sqr(5, 2))
print(sqr("8", 2))
print(shuffle("Hello", "World"))
print(shuffle("Test", "String"))
print(shuffle("AA", "BBBB"))
print(shuffle(1, "test"))