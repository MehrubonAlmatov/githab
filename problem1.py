accounts = [[1,2,3],[3,2,1]]
max_wealth = 0

for customer in accounts:

    current_wealth = sum(customer)
            
if current_wealth > max_wealth:
    max_wealth = current_wealth
        
print(max_wealth)