########################################################################################################################
##################################### Libraries used ###################################################################
########################################################################################################################
import os,sys
import glob
from string import ascii_uppercase
from numpy import array, reshape , where,dot
from math import pow
Alphabet =ascii_uppercase


#Author: Kirolos Samuel Azmy
#Date: 1-2-2021


########################################################################################################################
##################################### Implementation of Caeser Cipher ##################################################
########################################################################################################################
def Caeser_Encrypt(plain_text,key):
  plain_text =plain_text.replace(" ","").upper()
  result=''
  for i in range (len(plain_text)):
    character=plain_text[i]
    result+=chr((ord(character) + key-65) % 26 + 65)
  return result
  

########################################################################################################################
##################################### Implementation of Playfair Cipher ################################################
########################################################################################################################

def PlayFair_Encrypt(Plain_text,Key):
  cipher_text=[]
  generated_key_matrix=Generate_Key_Matrix(Key)
  plain_text_pairs=Modify_Plain_Text(Plain_text)
  
  #iterating on the pairs in the plain text and pass through the Key matrix to make the cipher text 
  #Applying the rules
  for plain_text_pair in plain_text_pairs:
    #flag to insure which rule that the pair follow
    flag=False
    #Rule 1 : if both elements of the pair are in the same row , so that shift right will be applied in both elements
    for row in generated_key_matrix:
      if plain_text_pair[0] in row and plain_text_pair[1] in row:
        #first we need to find the indexing of both elements in the row as if the element is the last element in the row , we will shift it to the right to be the first element
        #first convert row to a normal list in order to use find function to return the index of the letter in the row(much easier than where function)
        row_list=row.tolist()
        #get the indices of the plain_text_pairs
        index_1=row_list.index(plain_text_pair[0])
        index_2=row_list.index(plain_text_pair[1])

        if index_1 < 4:
          cipher_text.append(row_list[index_1+1])
        elif index_1 == 4 :
          cipher_text.append(row_list[0])
        
        if index_2 <4:
          cipher_text.append(row_list[index_2+1])
        elif index_2==4:
          cipher_text.append(row_list[0])
        
        flag=True

    if flag:
      continue    
    #Rule 2 : if the elements of the pair are in the same column , so that we will increment the position by one , first we need to iterate over the transpose of the numpy array so that we now iterate
    #over the column but in easier way
    for column in generated_key_matrix.T:
      if plain_text_pair[0] in column and plain_text_pair[1] in column:
        #first we need to find the indexing of both elements in the column as if the element is the last element in the column , we will shift it to the right to be the first element
        #first convert column to a normal list in order to use find function to return the index of the letter in the column(much easier than where function)
        column_list=column.tolist()
        index_1=column_list.index(plain_text_pair[0])
        index_2=column_list.index(plain_text_pair[1])
        if index_1 < 4:
          cipher_text.append(column_list[index_1+1])
        elif index_1 ==4 :
          cipher_text.append(column_list[0])
        
        if index_2 <4:
          cipher_text.append(column_list[index_2+1])
        elif index_2==4:
          cipher_text.append(column_list[0])
        flag=True    
    
    if flag:
      continue

    #Rule 3 , if both of them are not in the same col. or rows 
    #it will return 2 tuples , the first one is row position and dtype , the second tuple is column pos and dtype
    index_1=where(generated_key_matrix==plain_text_pair[0])
    index_2=where(generated_key_matrix==plain_text_pair[1])

    first_row,first_column=index_1[0][0],index_1[1][0]
    second_row,second_column=index_2[0][0],index_2[1][0]   

    cipher_text.append(generated_key_matrix[first_row][second_column])
    cipher_text.append(generated_key_matrix[second_row][first_column])

  cipher_text_string=''.join([str(elem) for elem in cipher_text])
  return cipher_text_string



def Generate_Key_Matrix(key):
  generated_key=list()
#lambda function in order to be used to return the key with capital letter and with 'J' get replaced with 'I' 
#but with repeated letters
  first_modify=lambda char: char.upper().replace('J','I')
  un_modified_key=first_modify(key+Alphabet)
  #in order to remove the repeated letters
  for _ in un_modified_key:
    if _ not in generated_key and _ in ascii_uppercase:
      generated_key.append(_)

  Generated_KeY_Matrix=array(generated_key).reshape((5,5))

  return Generated_KeY_Matrix

   
#Function to return the pairs of the plain text
def Modify_Plain_Text(Plain_text):
  text=Plain_text.replace(" ","").upper().replace('J','I')
  Plain_Text_Pair=[]
  first_element_pair=''
  second_element_pair=''
  flag=False
  i=0
  for char in text:
    if flag :
      i+=1
      flag=False
      continue
    first_element_pair=char
    #if the character is the last one in the plain text , the second element in the pair will be X
    if ((i+1))==len(Plain_text):
      second_element_pair='X'
    else:
    #if not, the second element in the pair will be the next character
      second_element_pair=text[i+1]
    
    #if the second element in the pair is not the same as the first one , so that Construct the pair with the elements
    if first_element_pair!=second_element_pair:
      Plain_Text_Pair.append(first_element_pair+second_element_pair)
      i+=1
      flag=True
    else:
      Plain_Text_Pair.append(first_element_pair+'X')
      i+=1
    
  return Plain_Text_Pair 



########################################################################################################################
##################################### Implementation of Hill Cipher ####################################################
########################################################################################################################

def generate_key(prem_key,num_order):
    prem_key_list=list(prem_key.split(' '))
    prem_key_list=[int(i) for i in prem_key_list]
    key_matrix=array(prem_key_list).reshape(num_order,num_order)
    return key_matrix    

def generate_plain_text_matrix(plain_text,num_order):
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.upper()
    plain_text_list=list(plain_text)

    if len(plain_text_list) % num_order==0:
        pass
    else :
        while len(plain_text_list)%num_order !=0:
            plain_text_list.append('X')
            # plain_text_list.append(plain_text_list[-1])
        
    plain_text_list_indices=[ord(element) - 65 for element in plain_text_list]
    plain_text_matrix=array(plain_text_list_indices).reshape(-1,num_order)
    return plain_text_matrix


def Hill_Encrypt(plain_text,key,num_order):
    plain_text_matrix=generate_plain_text_matrix(plain_text,num_order)
    key_matrix=generate_key(key,num_order)
    output_list=[]
    for row in plain_text_matrix:
        output=dot(key_matrix,row)%26
        output=output.tolist()
        for element in output:
            output_list.append(element+1)

    cipher_text=''
    for element in output_list:
        cipher_text+=chr(element+64)
    return cipher_text


########################################################################################################################
##################################### Implementation of Vernam Cipher ##################################################
########################################################################################################################

def Vernam_Encrypt(plain_text,key):
    # convert into Upper cases and remove spaces
    plain_text=plain_text.replace(" ","").upper()
    key=key.replace(" ","").upper()
    
    # conditional statements
    if(len(plain_text)!=len(key)):
        print("Lengths are different")
    else:
        cipher_text=""
        # iterating through the length
        for i in range(len(plain_text)):
            k1=ord(plain_text[i])-65
            k2=ord(key[i])-65
            s=chr((k1+k2)%26+65)
            cipher_text+=s
        return cipher_text




########################################################################################################################
##################################### Implementation of Vigenere Cipher in repeating mode ##############################
########################################################################################################################


def Vigenere_Repeating_Mode_Encrypt(plain_text,key):
    index=0
    cipher_text=""

    # convert into Upper cases and remove spaces
    plain_text=plain_text.replace(" ","").upper()
    key=key.replace(" ","").upper()
    
    # For generating key, the given keyword is repeated
    # in a circular manner until it matches the length of 
    # the plain text.
    for char in plain_text:
        if char in Alphabet:
            # to get the number corresponding to the alphabet
            alpha_offset=ord(key[index])-ord('A')
            encrypt_number=(ord(char)-ord('A')+alpha_offset)%26
            encrypt_char=chr(encrypt_number+ord('A'))
            
            # adding into cipher text to get the encrypted message
            cipher_text+=encrypt_char
            
            # for cyclic rotation in generating key from keyword
            index=(index+1)%len(key)
        # to not to change spaces or any other special
        # characters in their positions
        else:
            cipher_text+=char
    
    return cipher_text


########################################################################################################################
##################################### Implementation of Vigenere Cipher in auto mode ###################################
########################################################################################################################



# This function generates the key
def Vigenere_generate_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i]
            i += 1
    return key

def Vigenere_Auto_Mode_Encrypt(plain_text,key):
    newKey=Vigenere_generate_key(plain_text,key)
    newKey=newKey.upper()
    plain_text=plain_text.upper()
    cipher_text=''
    for index,char in enumerate(plain_text):
        off=ord(newKey[index])-ord('A')
        # implementing algo logic here
        encrypt_num=(ord(char)-ord('A')+off)%26
        encrypt=chr(encrypt_num+ord('A'))    
        # adding into cipher text to get the encrypted message
        cipher_text+=encrypt

    
    return cipher_text   





########################################################################################################################
##################################### READING & WRITING BUILT IN TEXT MODE #############################################
########################################################################################################################
def Txt_output():


  input_folders=['Caesar','Hill','PlayFair','Vernam','Vigenere']
  output_folders=['Caesar','Hill','PlayFair','Vernam','Vigenere']
  input_text=[]

  input_caesar_keys=[3,6,12]
  input_playfair_keys=['rats','archangel']
  input_hill_key_2X2='5 17 8 3'
  input_hill_key_3X3='2 4 12 9 1 6 7 5 3'
  input_vigenere_repeat_key='pie'
  input_vigenere_auto_key='aether'
  input_vernam_key='SPARTANS'



  input_file='Input Files\\Input Files\\'
  out_file='Output Files'
  my_path=os.path.abspath(os.path.dirname(__file__))
  input_path=os.path.join(my_path,input_file)
  output_path=os.path.join(my_path,out_file)
  #print(output_path)

  if out_file in os.listdir(os.path.abspath(os.path.dirname(__file__))):
      pass
  else:
      #making output file folder
      os.mkdir(output_path)

  for folder in input_folders:        
      for file in os.listdir(input_path+folder):
          if file.endswith(".txt"):
              f=open(input_path+folder+'/'+file,'r')
              f=f.read().splitlines()
              input_text.append(f)
      
  input_text_caesar=input_text[0]
  input_text_Hill_2X2=input_text[1]
  input_text_Hill_3X3=input_text[2]
  input_text_playfair=input_text[3]
  input_text_vernam=input_text[4]
  input_text_vigenere=input_text[5]


  # Caesar Cipher ##############################
  completeName = os.path.join(output_path,"Caesar_Output.txt")      
  Caesar_file=open(completeName,'w')
  for plain_text in input_text_caesar:
    for key in input_caesar_keys:
      Caesar_file.write("The encryption of : "+plain_text+" using the key "+str(key)+' in Caesar mode \n')
      Caesar_file.write(Caeser_Encrypt(plain_text,key)+'\n')
    Caesar_file.write("**************************************************************************** \n")


  # Hill 2X2 Cipher ##############################
  completeName = os.path.join(output_path,"Hill_2X2_Output.txt")      
  Hill_2X2_file=open(completeName,'w')
  for plain_text in input_text_Hill_2X2:
    Hill_2X2_file.write("The encryption of : "+plain_text+" using the key "+ "(" + input_hill_key_2X2 +")"+' in Hill_2X2 mode \n')
    Hill_2X2_file.write(Hill_Encrypt(plain_text,input_hill_key_2X2,2)+'\n')
    Hill_2X2_file.write("**************************************************************************** \n")


  # Hill 3X3 Cipher ##############################
  completeName = os.path.join(output_path,"Hill_3X3_Output.txt")      
  Hill_3X3_file=open(completeName,'w')
  for plain_text in input_text_Hill_3X3:
    Hill_3X3_file.write("The encryption of : "+plain_text+" using the key "+ "(" + input_hill_key_3X3 +")"+' in Hill_3X3 mode \n')
    Hill_3X3_file.write(Hill_Encrypt(plain_text,input_hill_key_3X3,3)+'\n')
    Hill_3X3_file.write("**************************************************************************** \n")


  # Playfair Cipher ##############################
  completeName = os.path.join(output_path,"Playfair_Output.txt")      
  Playfair_file=open(completeName,'w')
  for plain_text in input_text_playfair:
    for key in input_playfair_keys:
      Playfair_file.write("The encryption of : "+plain_text+" using the key "+ "("+key+")"+' in playfair mode \n')
      Playfair_file.write(PlayFair_Encrypt(plain_text,key)+'\n')
    Playfair_file.write("**************************************************************************** \n")

  # Vigenere_repeat Cipher ##############################
  completeName = os.path.join(output_path,"Vigenere_repeat_Output.txt")      
  Vigenere_repeat_file=open(completeName,'w')
  for plain_text in input_text_vigenere:
    Vigenere_repeat_file.write("The encryption of : "+plain_text+" using the key "+ "("+input_vigenere_repeat_key+")"+' in Vigenere repeat mode \n')
    Vigenere_repeat_file.write(Vigenere_Repeating_Mode_Encrypt(plain_text,input_vigenere_repeat_key)+'\n')
    Vigenere_repeat_file.write("**************************************************************************** \n")


  # Vigenere_auto Cipher ##############################
  completeName = os.path.join(output_path,"Vigenere_auto_Output.txt")      
  Vigenere_auto_file=open(completeName,'w')
  for plain_text in input_text_vigenere:
    Vigenere_auto_file.write("The encryption of : "+plain_text+" using the key "+ "("+input_vigenere_auto_key+")"+' in Vigenere auto mode \n')
    Vigenere_auto_file.write(Vigenere_Auto_Mode_Encrypt(plain_text,input_vigenere_auto_key)+'\n')
    Vigenere_auto_file.write("**************************************************************************** \n")


  # vernam Cipher ##############################
  completeName = os.path.join(output_path,"Vernam.txt")      
  vernam_file=open(completeName,'w')
  for plain_text in input_text_vernam:
    vernam_file.write("The encryption of : "+plain_text+" using the key "+ "(" + input_vernam_key +")"+' in Vernam mode \n')
    vernam_file.write(Vernam_Encrypt(plain_text,input_vernam_key)+'\n')
    vernam_file.write("**************************************************************************** \n")



########################################################################################################################
##################################### Mode of operation of CONSOLE command #############################################
########################################################################################################################





########################################################################################################################
##################################### Choosing the mode of operation ###################################################
########################################################################################################################

def main():
  while(True):
    print("********************************************************************************************************************")
    print("Please enter only 1 or 2 or 3 for choices below ")
    print("Please enter the mode of operation from the options below : ")
    print("1- Read & Write built in examples from text file ")
    print("2- You enter one Plain text and a certain key for classical cipher")
    print("3- EXIT")
    options = int(input())

    if options ==1:
        Txt_output()
        print("Encryption done on examples in Input Files and the cipher text are in the folder Ouptut Files ")
        print("********************************************************************************************************************")
    elif options ==2:
        #plain text
        plain_text=input("Please enter the plain text : ")
        #caesar key & Encryption
        caesar_key=int(input("Please enter the key of the Caesar cipher : "))
        print("The cipher text of the plain text : "+plain_text+" by using caeser cipher is : "+Caeser_Encrypt(plain_text,caesar_key))
        print("********************************************************************************************************************")
        #playfair key
        Playfair_key=input("Please enter the key of the Playfair cipher : ")
        print("The cipher text of the plain text : "+plain_text+" by using Playfair cipher is : "+PlayFair_Encrypt(plain_text,Playfair_key))
        print("********************************************************************************************************************")

        #hill keys & Encryption
        print("Please enter the order of the Hill key matrix : ")
        hill_order = int(input())
        hill_key =input("Please enter the hill key in terms of number seperated by a space between each element : ")
        print("The cipher text of the plain text : "+plain_text+" by using hill cipher is : "+Hill_Encrypt(plain_text,hill_key,hill_order))
        print("********************************************************************************************************************") 

        #Vernam_key & Encryption
        vernam_key=input("Please enter the key of the Vernam cipher , Note that the key should be the same size of the plainText : ")
        print("The cipher text of the plain text : "+plain_text+" by using vernam cipher is : "+Vernam_Encrypt(plain_text,vernam_key))
        print("********************************************************************************************************************") 

        #Vigenere_key & Encryption
        #Choose Vigenere mode 
        print("for repeated Vigenere mode please press 1 , for auto Vigenere mode please press 2 , for both press 3 ")
        vigenere_options = int(input())
        if vigenere_options == 1:
             vigenere_repeated_key=input("Please enter the key of the repeated mode of vigenere cipher :")
             print("The cipher text of the plain text : "+plain_text+" by using repeated mode of vigenere cipher is : "+Vigenere_Repeating_Mode_Encrypt(plain_text,vigenere_repeated_key))
             print("********************************************************************************************************************") 
        elif vigenere_options == 2:
             vigenere_auto_key=input("Please enter the key of the auto mode of vigenere cipher : ")
             print("The cipher text of the plain text : "+plain_text+" by using auto mode of vigenere cipher is : "+Vigenere_Auto_Mode_Encrypt(plain_text,vigenere_auto_key))
             print("********************************************************************************************************************") 
        elif vigenere_options == 3:
             vigenere_repeated_key=input("Please enter the key of the repeated mode of vigenere cipher :")
             vigenere_auto_key=input("Please enter the key of the auto mode of vigenere cipher : ")
             print("The cipher text of the plain text : "+plain_text+" by using repeated mode of vigenere cipher is : "+Vigenere_Repeating_Mode_Encrypt(plain_text,vigenere_repeated_key))
             print("The cipher text of the plain text : "+plain_text+" by using auto mode of vigenere cipher is : "+Vigenere_Auto_Mode_Encrypt(plain_text,vigenere_auto_key))
             print("********************************************************************************************************************") 
        

    elif options==3:
      exit()
      break

# Executes the main function
if __name__ == '__main__':
    main()



