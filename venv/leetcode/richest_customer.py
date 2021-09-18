customer = [[1,2,3], [4,5,6], [7,8,9]]
wealth = 0
for i in range(len(customer)):
    total_wealth = sum(customer[i])
    wealth = max(wealth, total_wealth)
print(wealth)







