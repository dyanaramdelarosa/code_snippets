# Problem Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# Author: Dyanara Dela Rosa
# Date: January 2024

def makeAnagram(a, b):
    # Write your code here
    a = sorted(a)
    b = sorted(b)
    deletion_count = 0
    i, j = 0, 0
    print(a)
    print(b)
    while i < len(a) and j < len(b):
        print(f"a[i]: {a[i]}")
        print(f"b[j]: {b[j]}")
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
            deletion_count += 1
        else:
            j += 1
            deletion_count += 1

    if i >= len(a):
        deletion_count += len(b)-j
    if j >= len(b):
        deletion_count += len(a)-i

    return deletion_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(str(res) + '\n')
    # fptr.write(str(res) + '\n')

    # fptr.close()
