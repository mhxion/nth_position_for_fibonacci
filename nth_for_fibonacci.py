from math import sqrt
from math import floor
import decimal


def nth_fib(x, _len):
    """Calculating nth term through Binet's formula with accurate intefer precision"""
    decimal.getcontext().prec = _len * 2
    nth_fib = (
        (1 + decimal.Decimal(5).sqrt()) ** x - (1 - decimal.Decimal(5).sqrt()) ** x
    ) / (2 ** x * decimal.Decimal(5).sqrt())
    return int(nth_fib)


def nth_fib_without_precision(x, _len):
    """Calculating nth term through Binet's formula with no accurate precision (incorrect digits after 13th)"""
    nth_fib = (
        (1 + decimal.Decimal(5).sqrt()) ** x - (1 - decimal.Decimal(5).sqrt()) ** x
    ) / (2 ** x * decimal.Decimal(5).sqrt())
    return int(nth_fib)


def nth_fib_len(x, _len):
    return len(str(nth_fib(x, _len)))


def nth_for_fib(number):
    """Yields the nth position"""
    str_number = str(number)
    _len = len(str_number)

    n = (
        6 + 5 * (int(_len * 0.75) - 1) + 4 * round((3 * (_len - 1)) / 13)
        if _len == 8 or _len == 4
        else 6 + 5 * int(_len * 0.75) + 4 * round((3 * (_len - 1)) / 13)
    )

    n_begin, n_end, n_hop, n_jump = n - 5, n + 5, n + 10, n + 15

    if _len > nth_fib_len(n, _len):
        if _len == nth_fib_len(n_end, _len):
            nth = [n, n_end + 3]
        elif _len == nth_fib_len(n_hop, _len):
            nth = [n_end, n_hop + 3]
        elif _len == nth_fib_len(n_jump, _len):
            nth = [n_hop, n_jump + 3]
        else:
            raise ValueError(
                "Uh oh! The number is over 8.88e187 or 901th place. For some reason the equation for n doesn't work with numbers over 8.88e187. I'll have to work on the n's algorithm more for this."
            )
    elif _len <= nth_fib_len(n, _len):
        nth = [n_begin, n]

    for _ in range(nth[0], nth[1] + 1):
        if list(str_number)[:13] == list(str(nth_fib_without_precision(_, _len)))[:13]:
            yield _
    # return nth_fib(868, _len)88793027306605937532517516910637647045239090036365766884466525589158360259770006891772711976920559280382807770394537471560061517120086971996377683290300054868066659454250625417891167369401
    # return nth


# if __name__ == "__main__":
#     print(
#         list(
#             nth_for_fib(
#                 2584
#             )
#         )
#     )
# import timeit

# print(
#     timeit.timeit(
#         "nth_for_fib(2350704430272641239071841033501890806135341594051678146868727563621503575841361361660546174279787382902052764874870847641179)", "from __main__ import nth_for_fib", number=1000000
#     )
# )
