#n is a year
# n/4 = true
# n/100 = false
# n / 400 = true
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# def is_leap(year):
#     leap = False
#
#     if year%4==0 and year%400==0:
#         return False
#     elif year%100==0:
#         return True
#
#     return
# result = int(input())
# print(is_leap(year))

def is_every4(n):
    if n%400==0:
        return True
    if n%100==0:
        return False

    if n % 4 == 0:
        return True
    else:
        return False


anyword = int(input())
result = is_every4(anyword) #year is n
print(result)


