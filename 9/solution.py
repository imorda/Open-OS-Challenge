import math


def sh(x):
    result = 0.
    cur_x = x
    cur_fact = 1
    cur_power = 1
    for i in range(10):
        result += cur_x / cur_fact
        cur_power += 2
        cur_x *= x
        cur_x *= x
        cur_fact *= cur_power - 1
        cur_fact *= cur_power
    return result


x = 0.5
print(f"{math.sinh(x): .60f}")
print(f"{sh(x): .60f}")
print(sh(x) - math.sinh(x))
print(sh(x) == math.sinh(x))
