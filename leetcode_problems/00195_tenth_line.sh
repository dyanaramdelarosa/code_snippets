# Problem Link: https://leetcode.com/problems/tenth-line/
# Author: Dyanara Dela Rosa
# Date: May 25, 2026

# 3 solutions:
awk 'NR==10' file.txt
tail -n +10 file.txt | head -1
sed -n '10p' file.txt