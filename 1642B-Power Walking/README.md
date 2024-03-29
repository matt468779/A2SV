B. Power Walking
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Sam is a kindergartener, and there are n children in his group. He decided to create a team with some of his children to play "brawl:go 2".

Sam has n power-ups, the i-th has type ai. A child's strength is equal to the number of different types among power-ups he has.

For a team of size k, Sam will distribute all n power-ups to k children in such a way that each of the k children receives at least one power-up, and each power-up is given to someone.

For each integer k from 1 to n, find the minimum sum of strengths of a team of k children Sam can get.

Input
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤3⋅105) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤3⋅105).

The second line contains n integers a1,a2,…,an (1≤ai≤109) — types of Sam's power-ups.

It is guaranteed that the sum of n over all test cases does not exceed 3⋅105.

Output
For every test case print n integers.

The k-th integer should be equal to the minimum sum of strengths of children in the team of size k that Sam can get.

Example
inputCopy
2
3
1 1 2
6
5 1 2 2 2 4
outputCopy
2 2 3 
4 4 4 4 5 6 
Note
One of the ways to give power-ups to minimise the sum of strengths in the first test case:

k=1:{1,1,2}
k=2:{1,1},{2}
k=3:{1},{1},{2}
One of the ways to give power-ups to minimise the sum of strengths in the second test case:

k=1:{1,2,2,2,4,5}
k=2:{2,2,2,4,5},{1}
k=3:{2,2,2,5},{1},{4}
k=4:{2,2,2},{1},{4},{5}
k=5:{2,2},{1},{2},{4},{5}
k=6:{1},{2},{2},{2},{4},{5}
