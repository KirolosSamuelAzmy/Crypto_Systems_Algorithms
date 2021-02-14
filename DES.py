#Author: Kirolos Samuel Azmy
#Date: 1-2-2021

########################################################################################################################
##################################### DES LOCK_UP TABLES ###############################################################
########################################################################################################################

# Initial Permutation Table, IP table, ex. [58] -> [1]
initial_perm =[
58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7
]


# Expansion Permutation Table
exp_d =[
32, 1, 2, 3, 4, 5, 4, 5,
6, 7, 8, 9, 8, 9, 10, 11,
12, 13, 12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21, 20, 21,
22, 23, 24, 25, 24, 25, 26, 27,
28, 29, 28, 29, 30, 31, 32, 1
]

    # 8 S-boxes Table
s_box = [
[
[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
[
[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
[
[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
[
[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
[
[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
[
[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
[
[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
[
[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]



# P-box Permutation Table, FP table, [16] -> [1]
p_box = [
16, 7, 20, 21,
29, 12, 28, 17,
1, 15, 23, 26,
5, 18, 31, 10,
2, 8, 24, 14,
32, 27, 3, 9,
19, 13, 30, 6,
22, 11, 4, 25]


# Final Permutation Table
final_perm = [
40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25
]


# First_permutation_Key
first_permutation_key_table = [
57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4
]


# Number of bit shifting
# 16 Rounds total
# Round #1, 2, 9, 16 are 2 bits-shift, others are 1 bit-shift
shift_table = [
1, 1, 2, 2,
2, 2, 2, 2,
1, 2, 2, 2,
2, 2, 2, 1
]



# Key- Compression Table 56bits to 48bits, permuted choice2
key_comp = [
14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19, 12, 4, 26, 8,
16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55,
30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32
]

########################################################################################################################
##################################### DES Steps ########################################################################
########################################################################################################################


#Steps to generate the key:
# 1)Get the key from the user and convert to binary 
# 2)Make the first permutation to convert into from 64 bit key into 56 Key
# 3)Divide the key into two parts of left and right parts
# 4)Rotate shift
# 5)Concatenate the 2 parts of the key
# 6)Finally put the key in second permutation


#Steps to encrypt 
# 1) Initial permutation of text 
# 2) Splitting the plain text into 2 parts
# 3) Exansion permutation of the plain text
# 4) XOR K[i] and right_expanded 
# 5) S-box substitution
# 6) P-box permutation
# 5) XOR & Swap



########################################################################################################################
##################################### DES HELPER FUNCTIONS #############################################################
########################################################################################################################

def hex2bin(hexadecimal):
    val = int(hexadecimal, 16)
    val = bin(val)
    s = str(val)[2:]
    while len(s) < 64:
        s = '0' + s
    return s


def bin2hex(binary):
    val = int(binary, 2)
    val = hex(val)
    return str(val).upper()[2:]


def permute(text, permutation_choice, no_permutation):
    per = ""
    for permuate_number in range(no_permutation):
        per += text[permutation_choice[permuate_number] - 1]
    return per


def shift(text,no_shifts):
    s = ""
    for i in range(no_shifts):
        for j in range(1, 28):
            s += text[j]
        s += text[0]
        k = s
        s = ""
    return k


def xor(a,b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"
    return ans



########################################################################################################################
##################################### DES MAIN FUNCTIONS ###############################################################
########################################################################################################################

def key_generation(key):
    #first the key is entered as string in hex representation so i will first convert it to binary
    key = hex2bin(key)
    # getting 56 bit key from 64 bit using the first_permutation_key_table
    key = permute(key, first_permutation_key_table, 56)  # key without parity
    # Splitting the key into two 28bits-parts
    left = key[:28]
    right = key[28:]

    #For every round of the 16 round there is a key generated so that i looped over them for 16 times
    round_key_binary = []
    for i in range(16):
        # Shifting
        left = shift(left, shift_table[i])
        right = shift(right, shift_table[i])

        # Combining
        combine = left + right

        # Key Compression, compress 56 bits key into 48 bits key
        round_key = permute(combine, key_comp, 48)

        # Add N-round key into the list in binary format
        round_key_binary.append(round_key)    
    return round_key_binary

def modify_plaintext(plain_text):
   # Hexadecimal to Binary
    plain_text = hex2bin(plain_text)  
    # Initial Permutation
    plain_text = permute(plain_text, initial_perm, 64)
    # Splitting plain text into two parts, each one has 32 bits
    left = plain_text[:32]
    right = plain_text[32:]

    return right, left





# 16 rounds of Feistel encryption
def encrypt(right_plain_text,left_plain_text ,round_key_binary):
    for i in range(16):
        # F-function Part
        # 1) Expansion Permutation for Right side
        right_expanded = permute(right_plain_text, exp_d, 48)

        # 2) XOR K[i] and right_expanded
        x = xor(round_key_binary[i], right_expanded)

        # 3) S-box substitution
        op = ""
        for j in range(8):
            row = 2 * int(x[j * 6]) + int(x[j * 6 + 5])
            col = 8 * int(x[j * 6 + 1]) + 4 * int(x[j * 6 + 2]) + 2 * int(x[j * 6 + 3]) + int(x[j * 6 + 4])
            val = s_box[j][row][col]
            op += str(val // 8)
            val = val % 8
            op += str(val // 4)
            val = val % 4
            op += str(val // 2)
            val = val % 2
            op += str(val)

        # 4) P-box permutation
        op = permute(op, p_box, 32)

        # 5) XOR left and right
        x = xor(op, left_plain_text)

        # give the result to L(i-1)
        left_plain_text = x
        # swap right side and left side
        # Ri = L(i-i) & Li = R(i-1)
        if i != 15:
            left_plain_text, right_plain_text = right_plain_text, left_plain_text

    # Combination
    combine = left_plain_text + right_plain_text
    cipher = bin2hex(permute(combine, final_perm, 64))
    return cipher



flag=1
while(flag==1):
    choice = int(input("For encyption just press 0 ONLY and for decryption press 1 : "))
    print("")
    if choice==0:
        key=input("Please Enter the Key in terms of 16 HEX character with NO SPACES : ")
        print("**************************************************************************************")
        #Taking the Plain_text , key & number of encryption from the user
        plain_text=input("Please Enter the plain text in terms of 16 character with NO SPACES : ")
        print("**************************************************************************************")
        no_encrypt=int(input("Please Enter the number of encyption you want : "))
        print("**************************************************************************************")
        #Modifying the Plain_text
        right,left=modify_plaintext(plain_text)
        #Key_Generation
        round_key_in_binary=key_generation(key)
        cipher = encrypt(right,left, round_key_in_binary)
        for i in range(0,no_encrypt-1):
            #Modifying the Plain_text
            right,left=modify_plaintext(cipher)
            cipher = encrypt(right,left, round_key_in_binary)

        print("Cipher Text: " + cipher)

    elif choice==1:
        key=input("Please Enter the Key in terms of 16 HEX character with NO SPACES : ")
        #Taking the Plain_text , key & number of encryption from the user
        cipher_text=input("Please Enter the cipher text in terms of 16HEX character with NO SPACES : ")
        print("**************************************************************************************")
        #Modifying the Plain_text
        right,left=modify_plaintext(cipher_text)
        #Key_Generation
        round_key_in_binary=key_generation(key)
        cipher_first = encrypt(right,left, round_key_in_binary)
        for i in range(0,1):
            #Modifying the Plain_text
            right,left=modify_plaintext(cipher_first)
            plain_text = encrypt(right,left, round_key_in_binary)

        print("The Plain Text is: " + plain_text)
    
    print("###################################################################################################")
    print("###################################################################################################")
    print("1 - Continue using the program ")
    print("2 - Exit ")
    flag = int(input("Enter 1 to continue using it & 2 to exit the program "))





