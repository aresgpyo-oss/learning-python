code = input();
amount = int(input());

print(code == "GOLD");
print("X" in code);
print(amount >= 50 and amount <= 200);
print(code == "GOLD" or not (amount >= 50 and amount <= 200));