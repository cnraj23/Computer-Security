# import math function to calculate ceiling
import math

# input plaintext
plaintext = input("\nEnter your plaintext: ").upper()
# print(plaintext)

# convert plain text into list
pt_list = list(plaintext)

# input secret key
secret_key = input("\nEnter your Secretkey: ").upper()
# print(secret_key)

# convert secret key into list
sk_list = list(secret_key)

# defining list of character array
char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', ',', '.', '-', '_']

# calculating length of plain text and secret key
ptext_len = len(plaintext)
sKey_len = len(secret_key)

# initialize the end of 1st loop by calculating the ceiling
# Divide plaintext length by secret key length
loopEnd = int(math.ceil(ptext_len / sKey_len))
# print("Length of \n Plain Text : " + str(ptext_len) + "\n Secret Key : " + str(sKey_len))
# print("\n Total Loops Required : " + str(loopEnd))
# print("\n ***** Loop starts here ***** \n")
# print("Primary Secret key : " + secret_key)
# initialization of new key and cipher text
new_key = ""
cipher_text = ""
loopStart = 0

if sKey_len > ptext_len:
    sKey_len = ptext_len

# adding for loop to plain text
for k in range(0, loopEnd):
    # 2nd loop is for execution of actual encryption. LoopStart is storing value for initial loop variable
    # skey_len is used to indicate the last variable to end loop
    # find index value of plaintext list value
    # find index value of secret key list value
    # use mod 30
    # store the mod value into a list
    # add the new key value for every loop execution


    for i in range(loopStart, sKey_len):
        x = char_list.index(pt_list[i])
        y = char_list.index(sk_list[i])
        m = (x + y) % 30
        z = char_list[m]
        new_key = new_key + z
        # print(z)

    # This cipher text variable is storing the actual Encrypted text
    # this is re-initializing the loop for next round
    # this is generating new secret key with addition of old key with new ciphered text
    # Store the new secret key into list
    cipher_text = cipher_text + new_key

    loopStart = sKey_len
    secret_key = secret_key + new_key
    sk_list = list(secret_key)
    sKey_len = len(secret_key)
    #    print("New Secret Key : " + str(secret_key))
    new_key = ""

    # if the length of plain text is in  " odd values "
    # this condition will solve the problem of re-initialization of ending of the 2nd for loop
    if sKey_len > ptext_len:
        sKey_len = ptext_len

# print("\n ***** Loop Ends ******")
print("\n CIPHER TEXT IS : " + str(cipher_text))

# ***************************************************************************************************************
# Name : Vigenere cipher
# BY : CHINMAY RAJGURU
# Date : 02/19/2017
