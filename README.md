# Interexy junior python dev task

## Algorithm

_Our task is to find all the elements that are necessary for any combination of numbers that make up the sum equal to the number x.
We have one coin of each denomination from the "coins_list" list.
You need to collect all the required coins for any suitable combination. They can also be represented as intersections of the sets of all suitable combinations.
We will assume that a coin is optional if there is at least one combination that satisfies the task condition and does not include this coin (if there are no such combinations, then the coin is mandatory).
Let's check every coin.
Let's build a template list of the type "1, 0, 0, 0, 0, 0,...0(x)". That is, a list of ones and zeros in x.
Now, with the help of denominations, we shift this unit by index. It itself has index 0, so all offsets will generate possible positions. Thus, we get a cast from 1 for all numbers that can be obtained with such offsets (combinations). If 1 is at position x, then there is a combination in such a list that contains the sum of some elements equal to x.
We will throw out one denomination and check for a suitable combination. Thus, we fix all the necessary denominations._

## Functions

### foo()
        This function implements main algorithm.
        We check each coin for its necessity of presence in list of necessary coins.
        Coin not necessary if there is a pattern of another coins with sum(coins) = x.
        If this pattern exists, we skip coin and mark it as not necessary coin.


### shift(ls, coin)
        This function implements shift for elements in list(ls).
        The shift value is coin.
        Example:
            For list = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0] and coin = 2
            Shifted list = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
        Each element shifts for coin value


## Test

### Test case file

To execute python script with a test file run:
```sh
python task.py < test_case.txt
```

## Note

_Python version 3.11.4_

