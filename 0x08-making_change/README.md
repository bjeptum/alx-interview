## 0x08. Making Change

For the “0. Change comes from within” project, I tackled a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. 

The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. 

This project challenged me to apply my understanding of algorithms to devise a solution that is not only correct but also efficient.

## Solution

- Create an array min_coins where min_coins[i] represents the minimum number of coins needed to make a total of i.

- Initialize min_coins[0] = 0, because 0 coins are needed to make a total of 0.

- Initialize all other values of min_coins[i] to a large number (float('inf')), since initially, it is not known how to make these totals.

- For each coin in the coins list, update the min_coins array for all totals from the coin's value to total.

- If I can make a total i using a coin, I check if using that coin results in fewer coins than the current minimum stored in min_coins[i].

- After processing all the coins, check min_coins[total]. If it is still float('inf'), it means it's not possible to make the total with the given coins, so return -1.

- Otherwise, return min_coins[total], which gives the minimum number of coins required.