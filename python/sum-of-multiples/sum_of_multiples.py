def sum_of_multiples(limit, multiples):
    return sum({n for factor in multiples if factor for n in range(factor, limit, factor)})
