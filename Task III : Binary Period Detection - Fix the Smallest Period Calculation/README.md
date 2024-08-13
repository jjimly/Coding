Consider a non-empty string S = S[0]S[1]...S[Q-1] consisting of Q characters. The period of this string is the smallest positive integer P such that:
            - P ≤ Q/2 and
            - S[K] = S[K+P] for every K, where 0 ≤ K < Q - P.
For example, 8 is the period of "codilitycodilityco" and 7 is the period of "abracadabracadabra".
A positive integer M is the binary period of a positive integer N if M is the period of the binary representation of N
For example, 4 is the binary period of 955, because the binary representation of 955 is "1110111011" and its period is 4.
You are given an implementation of a function:
    def solution(N) :
           d = [0] * 30
           l = 0
           while (n > 0):
                      d[l] = n % 2
                      n //= 2
                      l += 1
           for p in range(1, 1+l):
                 ok = True
                 for i in range(l - p):
                        if d[i] != d[i+p]:
                              ok = False
                              break
                  if ok:
                        return p
          return -1

This function, when given a positive integer N, returns the binary period of N. The function returns -1 if N does not have a binary period.
For example, given N = 955 the function returns 4, as explained in the example above.
The attached code is still incorrect for some inputs. Despite the error(s), the code may produce a correct answer for the example test cases. The goal of the exercise is to find and fix the bug(s) in the implementation. You can modify at most two lines.
Assume that:
     - N is an integer within the range [1..1,000,000,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.