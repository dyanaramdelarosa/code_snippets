# Problem Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
# Author: Dyanara Dela Rosa
# Date: February 2024

def sherlockAndAnagrams(s):
    # Write your code here
    words = []
    for i in range(0, len(s)):
        for j in range(1, len(s)+1):
            if i+j > len(s):
                break
            words.append(sorted(s[i: i+j]))

    match_count = 0
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            if i != j and words[i] == words[j]:
                match_count += 1
    return match_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result) + '\n')
        # fptr.write(str(result) + '\n')

    # fptr.close()
