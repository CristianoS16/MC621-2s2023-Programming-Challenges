a, b, c, d = map(int, input().split())
s = a/b
z = c/d
"""
Probability of SmallR winning in the first round:
s
Probability of SmallR winning in the second round (probability of him missing the first (1-s) and Zanoes also missing the first (1-z)):
(1-s)(1-z)s
Probability of SmallR winning in the third round (similar to previous):
(1-s)^2(1-z)^2s

The probability that Small wins is the sum of these probabilities:
s + (1-s)(1-z)s + (1-s)^2(1-z)^2s

Here I used chatGPT to help solve the series
The formula for the sum of a finite geometric series is given by:
Sum = a / (1 - r)
In this case a = s e r = is the ratio between consecutive terms: (1-s)^2(1-z)^2s/(1-s)(1-z)s = (1-s)(1-z)
"""
print(s / (1 - (1-s)*(1-z)))
