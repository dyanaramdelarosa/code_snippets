# Problem link: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
# Author: Dyanara Dela Rosa
# Date: April 2024

def whatFlavors(cost, money):
    # Write your code here
    instances = Counter(cost)
    print(instances)
    for flavor_cost in instances:
        change = money - flavor_cost

        if change in instances:
            if flavor_cost == change and instances[change] > 1:
                print(cost.index(flavor_cost)+1, cost.index(change, cost.index(change)+1)+1)
            elif flavor_cost == change and instances[change] == 1:
                continue
            else:
                print(cost.index(flavor_cost)+1, cost.index(change)+1)

            break

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
