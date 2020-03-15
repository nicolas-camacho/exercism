def classify(number):
    if number > 0: 
        total = sum([x for x in range(1, number) if number % x == 0])
        if total == number:
            return "perfect"
        if total > number:
            return "abundant"
        if total < number:
            return "deficient"
    else:
        raise ValueError("Invalid Input")