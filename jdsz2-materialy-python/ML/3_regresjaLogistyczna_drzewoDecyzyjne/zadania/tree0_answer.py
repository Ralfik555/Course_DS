import numpy as np

def entropy(pos, neg):
    return -pos*np.log2(pos)-neg*np.log2(neg)

pos = 9/14
neg = 5/14
Hs = entropy(pos, neg)
print("entropy: ", Hs)

pos = 6/8
neg = 2/8
Hs_slaby = entropy(pos, neg)
print("entropy: ", Hs_slaby)

pos = 3/6
neg = 3/6
Hs_silny = entropy(pos, neg)
print("entropy: ", Hs_silny)

Gain_s = Hs-8/14*Hs_slaby-6/14*Hs_silny
print("Gain_s: ", Gain_s)