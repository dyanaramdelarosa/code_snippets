# Problem Link: https://www.hackerrank.com/challenges/greedy-florist
# Author: Dyanara Dela Rosa
# Date: February 2024

# Problem Definition: Compute the minimum cost for buying all the flowers given k buyers.
# The cost of a flower can be computed using the formula:
#   (kth customer's number of purchases + 1) x flower's original price

def getMinimumCost(k, c):
    """
    Function that computes the minimum cost for buying all the flowers
    The function sorts the cost in descending order in order to buy the most expensive flowers
    first with a smaller multiplier. The first k flowers are bought by different buyers as well,
    therefore minimizing the cost.
    Args:
        k (int): number of buyers
        c (list[int)): cost of flowers

    Returns:
        int: minimum cost
    """
    c = sorted(c, reverse=True)
    i, cost, buy_counter = 0, 0, 0

    while i < len(c):
        cost += sum(c[i: i+k]) * (buy_counter + 1)
        i += k
        buy_counter += 1
    return cost


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    # fptr.write(str(minimumCost) + '\n')
    print(str(minimumCost) + '\n')

    # fptr.close()
