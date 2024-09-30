def maximum_wealth(accounts: list[list]):
    max_wealth_so_far = 0
    for account in accounts:
        customer_wealth = 0
        for amount in account:
            customer_wealth += amount

        max_wealth_so_far = max(max_wealth_so_far, customer_wealth)
    return max_wealth_so_far

print(f'Maximum wealth is: {maximum_wealth([[1,5],[7,3],[3,5]])}')
print(f'Maximum wealth is: {maximum_wealth([[1,2,3],[3,2,1]])}')