# Problem link: https://www.hackerrank.com/challenges/luck-balance
# Author: Dyanara Dela Rosa
# Date: February 2024

def luckBalance(k, contests):
    # Write your code here
    luck_balance, i = 0, 0
    while i < len(contests):
        if contests[i][1] == 0:
            luck_balance += contests[i][0]
            contests.pop(i)
        else:
            i += 1
    contests = sorted(contests)

    k = len(contests) - k
    
    for contest in contests:
        if k > 0:
            luck_balance -= contest[0]
            k -= 1
        else:
            luck_balance += contest[0]
    return luck_balance


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    # fptr.write(str(result) + '\n')
    print(str(result) + '\n')

    # fptr.close()
