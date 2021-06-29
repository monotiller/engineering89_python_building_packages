from app.complicated_calc import ComplicatedCalc

divide_numbers = ComplicatedCalc.divisible(3, 2)
modulous_numbers = ComplicatedCalc.modulus(2, 10)
positive_numbers = ComplicatedCalc.positive(-2)

print(divide_numbers.calc_list)
print(modulous_numbers.calc_list)
print(positive_numbers.calc_list)