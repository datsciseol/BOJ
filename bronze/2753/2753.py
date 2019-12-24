def annual_year(year):
    if year % 400 ==  0:
        result = 1
    elif year % 4 == 0 and year % 100 != 0:
        result = 1
    else:
        result = 0

    return result
year = int(input())
print(annual_year(year))
