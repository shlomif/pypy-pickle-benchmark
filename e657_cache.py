import os
import pickle
M = 10**9+7
nn = 10**12 + 1

max_alpha = 10**7

powM2 = []
i = 0
while i <= max_alpha:
    powM2.append(pow(i, M-2, M))
    i += 1
powpow = [0]
for numLetters in range(1, max_alpha):
    powpow.append(((pow(numLetters, nn, M)-1) * powM2[numLetters-1]) % M)

pickle.dump(powM2, open(os.getenv('HOME') + "/tmp/" + "powM2.pickle", "wb"))
pickle.dump(powpow, open(os.getenv('HOME') + "/tmp/" + "powpow.pickle", "wb"))
