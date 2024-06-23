# Problem Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# Author: Dyanara Dela Rosa
# Date: January 2024

def isValid(s):
    # Write your code here
    char_dict = defaultdict(int)
    for i in s:
        char_dict[i] += 1
    print(list(char_dict.values()).count())
    char_count = set(char_dict.values())
    print(char_count)

    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    while True:
        s = input()

        result = isValid(s)

        # fptr.write(result + '\n')
        print(result + '\n')

    # fptr.close()
