# Nth position for a given Fibonacci number

This is small algorithmic script I cooked up while playing with fibonacci squence programs. The algorithm for finding the nth position is based on empirical scribbles.

## Usage

The script returns a generator object which includes a single integer which is the position of the given fibonacci number.

```python
from nth_for_fibonacci import nth_for_fib

print(list(nth_for_fib(10610209857723)))
# prints [100]
```
`nth_for_fib()` attribute should be used for any valid output.

## Performance

The script generates a constant time complexity O(1). For a million iteration, it takes about 1.7 seconds on average.

```python
timeit.timeit("nth_for_fib(2350704430272641239071841033501890806135341594051678146868727563621503575841361361660546174279787382902052764874870847641179)", "from __main__ import nth_for_fib", number=1000000)

# returns 1.705661797997891
```

## Limitations

There are some limitations as I only get so much time to work on this. The only known limitations are:

1. It can't tell if the given number doesn't belong the fibonacci group, as I didn't write anything to guard that. 
2. The script doesn't work or throws an error if the given value is over 8.88 x 10<sup>187</sup> or over the 901th Fibonacci position. Possibly because of the nature of the Fibonacci series, for values over 8.88 x 10<sup>187</sup> a new equation is required. I will be working on this.
 
## Contribution

Contributions for issues, developments are welcome. Please make a pull request or open an issue.

## License and Attribution

The script is © copyrighted under the MIT license, not the best license to ensure credition, I hope you won't mind. 