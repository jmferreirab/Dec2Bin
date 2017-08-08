def dec2bin(n):
    if n < 0:
        return 'Solo un entero positivo'
    elif n == 0:
        return '0'
    else:
        return dec2bin(n//2) + str(n%2)

print("El numero en binario es: " + dec2bin(int(input("Enter a decimal number"))));