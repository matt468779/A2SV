                                                            B. Quality vs Quantity
                                                            time limit per test2 seconds
                                                            memory limit per test256 megabytes
                                                            inputstandard input
                                                            outputstandard output
 
You are given a sequence of n non-negative integers a1,a2,…,an. Initially, all the elements of the sequence are unpainted. You can paint each number Red––––– or Blue¯¯¯¯¯¯¯¯¯¯¯ (but not both), or leave it unpainted.

For a color c, Count(c) is the number of elements in the sequence painted with that color and Sum(c) is the sum of the elements in the sequence painted with that color.

For example, if the given sequence is [2,8,6,3,1] and it is painted this way: [2¯¯¯,8,6––,3¯¯¯,1] (where 6 is painted red, 2 and 3 are painted blue, 1 and 8 are unpainted) then Sum(Red–––––)=6, Sum(Blue¯¯¯¯¯¯¯¯¯¯¯)=2+3=5, Count(Red–––––)=1, and Count(Blue¯¯¯¯¯¯¯¯¯¯¯)=2.

Determine if it is possible to paint the sequence so that Sum(Red–––––)>Sum(Blue¯¯¯¯¯¯¯¯¯¯¯) and Count(Red–––––)<Count(Blue¯¯¯¯¯¯¯¯¯¯¯).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤1000). Description of the test cases follows.

The first line of each test case contains an integer n (3≤n≤2⋅105) — the length of the given sequence.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the given sequence.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print YES if it is possible to paint the given sequence satisfying the above requirements, and NO otherwise.

You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive response).

Example
inputCopy
4
3
1 2 3
5
2 8 6 3 1
4
3 5 4 2
5
1000000000 1000000000 1000000000 1000000000 1000000000
outputCopy
NO
YES
NO
NO
Note
In the first test case, there is no possible way to paint the sequence. For example, if you paint the sequence this way: [1¯¯¯,2¯¯¯,3––] (where 3 is painted red, 1 and 2 are painted blue) then Count(Red–––––)=1<Count(Blue¯¯¯¯¯¯¯¯¯¯¯)=2, but Sum(Red–––––)=3≯Sum(Blue¯¯¯¯¯¯¯¯¯¯¯)=3. So, this is not a possible way to paint the sequence.

In the second test case, a possible way to paint the sequence is described in the statement. We can see that Sum(Red–––––)=6>Sum(Blue¯¯¯¯¯¯¯¯¯¯¯)=5 and Count(Red–––––)=1<Count(Blue¯¯¯¯¯¯¯¯¯¯¯)=2.

In the third test case, there is no possible way to paint the sequence. For example, if you paint the sequence this way: [3––,5––,4¯¯¯,2¯¯¯] (where 3 and 5 are painted red, 4 and 2 are painted blue) then Sum(Red–––––)=8>Sum(Blue¯¯¯¯¯¯¯¯¯¯¯)=6 but Count(Red–––––)=2≮Count(Blue¯¯¯¯¯¯¯¯¯¯¯)=2. So, this is not a possible way to paint the sequence.

In the fourth test case, it can be proven that there is no possible way to paint the sequence satisfying sum and count constraints.
