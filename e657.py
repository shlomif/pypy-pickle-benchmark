import os
import pickle
import sys
from array import array
M = 10**9+7
nn = 10**12 + 1

max_alpha = 10**7


def myload(basename):
    """docstring for myload"""
    return pickle.load(
        open(os.getenv('HOME') + "/tmp/" + basename + ".pickle", "rb"))


powM2 = myload('powM2')
powpow = myload('powpow')

if False:
    powM2 = array('L', powM2)
    powpow = array('L', powpow)


def calcIFast(alpha):
    """ uses incremental nCK calc """
    total, combos = 0, 1
    for numLetters in range(alpha-1, 1, -1):
        combos *= numLetters + 1
        combos %= M
        combos *= powM2[alpha-numLetters]
        combos %= M
        sign = 1 if ((alpha-numLetters) & 1) else -1
        total += (combos * powpow[numLetters] * sign)
        total %= M
    sign = 1 if ((alpha-1) & 1) else -1
    total += (sign * ((alpha*nn)-1))
    total %= M
    return total

# i(10**2,1e12,1000000007) = 937709213 in 0.0029880000000162
# i(10**3,1e12,1000000007) = 761012922 in 0.019723999999996522
# i(10**4,1e12,1000000007) = 760918903 in 0.11362000000002581
# i(10**5,1e12,1000000007) = 5362748 in 1.0634489999999914
# i(10**6,1e12,1000000007) = 535160784 in 10.934123
# i(10**7,1e12,1000000007) = 219493139 in 170.85763000000003


s = 0
# last = 9988403
# s = 5806056895905
start = int(sys.argv[1])
end = int(sys.argv[2])
for alpha in range(start, end+1):
    # startTime = time.clock()
    # ans =
    # elapsedTime = time.clock()-startTime
    s += calcIFast(alpha)
    # print("i({},1e12) = {} in {}".format(alpha, ans, elapsedTime))
    # print("i({}) = {}".format(alpha, ans))
    # print("s = {}".format(s))
    # sys.stdout.flush()
# s += 1
print("start = {} ; end = {} ; sum = {}".format(start, end, s))
