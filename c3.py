def my_avg(*args):
    avg = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            avg += arg
        else:
            return None
    return avg / len(args)

def my_map(func, lst):
    return [func(x) for x in lst] if callable(func) and isinstance(lst, list) else None

def divide(num, lst):
    if isinstance(num, (int, float)) and all(isinstance(i, (int, float)) for i in lst):
        return my_map(lambda x: x // num, lst)
    else:
        return None

def process_numbers(filename):
    prices = {}
    with open(filename, "rt") as file:
        calls = [line.rstrip().split(",") for line in file if line]
        for callee, caller, price in calls:
            if caller not in prices:
                prices[caller] = {}

            if any(c[1] == callee for c in calls):
                prices[caller]["cena_firemne"] = prices.get(caller).get("cena_firemne", 0.0) + float(price)
            else:
                prices[caller]["cena_ostatne"] = prices.get(caller).get("cena_ostatne", 0.0) + float(price)
    return prices

print(my_avg(2, 4, 6, 8, 10))
print(my_avg(2.4, 5, 6.3, 5, 9))
print(my_avg("hehe", 2, 5))
print(divide(2, [5, 10, 15, 20, 22.5, 44.8]))
print(divide(2, [66.6, 55.5, 8, 3, "hehe"]))
print(divide("x", [10, 20, 30]))
print(process_numbers("calls.txt"))

