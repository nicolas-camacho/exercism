DROPS = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]


def convert(number):
    return ''.join(
        drop[1] for drop in DROPS if number % drop[0] == 0
        ) or str(number)
