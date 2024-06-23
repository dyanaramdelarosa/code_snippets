# Problem link: https://www.hackerrank.com/challenges/pairs/problem
# Author: Dyanara Dela Rosa
# Date: April 2024

def pairs(k, arr):
    # Write your code here
    num_of_solutions = 0
    instances = Counter(arr)
    print(instances)

    for x in instances:
        # 2 = x - y
        # k = x-y
        # k-x = -y
        # x-k = y
        # print(x,y)

        y = x-k
        if y in instances:
            num_of_solutions += 1

    return num_of_solutions


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(str(result))
