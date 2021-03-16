def add(x, y):
    """Add Funtion"""
    return x + y

def subtract(x, y):
    """Subtract Funtion"""
    return x - y

def multiply(x, y):
    """Multiply Funtion"""
    return x * y

def divide(x, y):
    """Divide Funtion"""
    if y == 0 :
        raise ValueError('Can not divide by zero!')
    return x / y

#print(divide(10,5))