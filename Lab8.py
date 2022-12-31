# function name: shift_cipher_encode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):
        length = len(string)
        encrypt = ""
        for i in range(0,length):
                if(string[i].isalpha() ==True):
                        if (string[i].isupper() == True):
                                x = ord(string[i])
                                x+=n
                                if(x>90):
                                        x = 65+(x%90)-1  
                                encrypt+= chr(x)
                        elif(string[i].islower()== True):
                                x = ord(string[i])
                                x+=n
                                if(x>122):
                                        x = 97+(x%122)-1
                                encrypt+=chr(x)
                else:
                        
                        encrypt+=string[i]
                
                                
        return encrypt

                                
                                
                        
                        
                




# function name: shift_cipher_decode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_decode(string, n):
        length = len(string)
        encrypt = ""
        for i in range(0,length):
                if(string[i].isalpha() ==True):
                        if (string[i].isupper() == True):
                                x = ord(string[i])
                                x-=n
                                if(x<65):
                                        x = 90-(65%x)+1  
                                encrypt+= chr(x)
                        elif(string[i].islower()== True):
                                x = ord(string[i])
                                x-=n
                                if(x<97):
                                        x = 122-(97%x)+1  
                                encrypt+= chr(x)
                else:
                        
                        encrypt+=string[i]
                
                                
        return encrypt


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run

# Wmfauw ak yjwsl! :)
#print(shift_cipher_encode("Eunice is great! :)", 18)) 
# Qobkbny sc qbokd dyy!!!
#print(shift_cipher_encode("Gerardo is great too!!!", 10)) 
# Gjwsfwit nx fqxt lwjfy! :I
#print(shift_cipher_encode("Bernardo is also great! :D", 5)) 
# WYWM229 cm nby vymn wfumm un WMOFV
#print(shift_cipher_encode("CECS229 is the best class at CSULB", 20)) 

# This is the 2nd lab.
#print(shift_cipher_decode("Qefp fp qeb 2ka ixy.", 23))
# ThErE r m@ny m0rE Labs 2 come!
#print(shift_cipher_decode("KyViV i d@ep d0iV Crsj 2 tfdv!", 17))
# s0 B prepared!
#print(shift_cipher_decode("y0 H vxkvgxkj!", 6))
# pineapples
#print(shift_cipher_decode("buzqmbbxqe", 12))




