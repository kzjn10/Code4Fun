def number_of_steps(num: int) -> int:
    steps = 0
    while num > 0:
        steps += 1
        if num % 2 == 0:
            print(f'Step {steps}) {num} is even; divide by 2 and obtain {(num // 2)}')
            num = num // 2
        else:
            print(f'Step {steps}) {num} is odd; subtract 1 and obtain {num - 1}')
            num = num - 1
    return steps


print(f'Steps: {number_of_steps(14)}')
print(f'Steps: {number_of_steps(8)}')
