#Higher order function: Una función dentro de otra función

def increment(x):
    return x + 1

increment_v2 = lambda x:x+1

def high_order_func(x, func):
    return x + func(x)

high_order_func_v2 = lambda x,func : x + func(x)

result = high_order_func(2, increment_v2)
print(result)

result_lambda = high_order_func_v2(2, lambda x:x+1)
print(result_lambda)