import numpy as np

S = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# T = np.array([1, 2, 3, 6, 1, 2, 3, 6])
T = np.array([2, 6, 1, 5, 2, 6, 1, 5])

# P = np.array([1, 2, 2, 2])
P = np.array([1, 3, 1, 2])

C = np.array([0, 0, 0, 0])

# key = np.array([1, 2, 3, 6])
key = np.array([2, 6, 1, 5])

print("Plain Text is : ")
print(P)
print("Key is :")
print(key)

# KSA Phase
j = 0
for i in range(8):
    j = (j + S[i] + T[i]) % 8
    S[i], S[j] = S[j], S[i]
    print("Iteration " + str(i) + " : ")
    print(S)

# PRGA Phase

i = j = m = 0
while True:
    i = (i + 1) % 8

    j = (j + S[i]) % 8

    S[i], S[j] = S[j], S[i]
    t = (S[i] + S[j]) % 8
    k = S[t]
    cipher = k ^ ord(chr(P[m]))
    C[m] = cipher

    m += 1
    if m == 4:
        break
print("Cipher Text is: ")
print(C)

# Date : 03/01/2017
# By : Chinmay Rajguru 