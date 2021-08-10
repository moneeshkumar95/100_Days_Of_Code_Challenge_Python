print('Day 80\n')

def product_integer(n):
    output = [None] * len(n)
    product = 1
    i = 0

    while i < len(n):
        output[i] = product
        product *= n[i]
        i += 1

    product = 1
    i = len(n) - 1

    while i >= 0:
        output[i] *= product
        product *= n[i]
        i -= 1

    return output

ip = [1,2,3,4]
print(f'Input: {ip}\nOutput: {product_integer(ip)}\n')

ip = [0,1,2,3,4]
print(f'Input: {ip}\nOutput: {product_integer(ip)}\n')

ip = [2,4,6,8]
print(f'Input: {ip}\nOutput: {product_integer(ip)}\n')