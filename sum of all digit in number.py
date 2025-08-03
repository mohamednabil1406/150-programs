# sum of all digit

def sum_of_digit(num):
    sum=0
    while  num!=0:
        digit=num%10
        sum+=digit
        num//=10
    return sum
num=12345
print(sum_of_digit(num))

