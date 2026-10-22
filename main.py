decimal_number = int(input());
whole_number = float(input());


sum_decimal = float(whole_number + decimal_number);
sum_chopped = int(sum_decimal);
print(sum_decimal);
print(sum_chopped);
print(str(decimal_number) + " + " + str(whole_number) + " = " + str(sum_decimal));