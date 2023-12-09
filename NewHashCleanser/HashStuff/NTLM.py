import re
import os
from User import User
from HashStuff.AbstractHashClass import Hash

class NTLM(Hash):

    hashes = []
    pattern = r"(.*?):(.*?):(.*?):(.*?):::" # NTLM Regex pattern

    def Pattern_Parser(list, pattern):
    # This function uses regular expression to fing NTLM or DCC2 hashes and returns the hashes in a list
        hashes = []
        for x in range (len(list)):
            tmp = list[x]
            #if(pattern == '(\$DCC2\$)(.*)' or pattern == '(.*?):(.*?):(.*?):(.*?):::'): #DCC2 or NTLM
            regex = re.compile(pattern)
            hash = regex.search(tmp)
            if(hash !=  None):
                hashes.append(hash[0])
        return hashes

    def Match_Parser (list, pattern):
    # Function to grab the hash username and password information and return lists containing that information
        hashList = []
        otherList = []
        for x in range (len(list)):
            tmp = list[x]
            regex = re.compile(pattern)
            hash = regex.search(tmp)
            if (pattern == '(.*?):(.*)(.*):(.*):::'): # non cracked hash 
                hashList.append(hash[4]) # should relate to the hash
                otherList.append(hash[1]) # should relate to the username
            elif (pattern == '(.*?):(.*)'): # cracked hash
                hashList.append(hash[1]) # should relate to the hash
                otherList.append(hash[2]) # should relate to the password
            else:
                print('something went wrong')
        return hashList, otherList

    def Directory_Parser(pattern, directory, mode):
    # this function will go through a directory and parse all the information from all the files
        hashes2 = []
        fileslist =  os.listdir(directory)
        for file in fileslist:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                hashes = NTLM.Secrets_Parser(file_path, pattern)
                hashes2 = hashes + hashes2
            if (mode == 'DCC2'):
                NTLM.List_Cleanser(hashes2, 'secretdumps.DCC2')
            else:
                hashes2 = NTLM.Remove_Duplicates(hashes2)
                NTLM.list_to_file(hashes2, 'secretdumps.NTLM')

    def Secrets_Parser(input, pattern):
    # Function to go through secrets folders and pull hashes
        hashes = []
        if (os.path.exists(input) == True):
            # open the file and starting to retrieve the DCC2 and NTLM hashes
            print('Starting parse...')          #I'm assuming this is part of the problem for the printing
            with open(input) as file:
                content = file.readlines()
            # Pull the hashes
            hashes = NTLM.Pattern_Parser(content, pattern) 
        return hashes

    def Match(hashes, cracked, pattern_HASH, pattern_CRACKED):
    # This function will take the file of cracked passwords from hashcat and the NTLM files and match the username to the password
        if (os.path.isfile(hashes) == True and os.path.isfile(cracked) == True):
            # grabbing the hashes and cracked passwords from the input files
            print('Grabbing hashed to be matched')
            with open(hashes) as file:
                hashes_from_file = file.readlines()
                hashes_from_file = NTLM.Remove_Unwanted_Chars(hashes_from_file)
                nonCracked_hash, nonCracked_username = NTLM.Match_Parser(hashes_from_file, pattern_HASH)
                file.close()
            print('Grabbing cracked passwords')
            with open(cracked) as file:
                cracked_from_file = file.readlines()
                cracked_from_file = NTLM.Remove_Unwanted_Chars(cracked_from_file)
                isCracked_hash, isCracked_password = NTLM.Match_Parser(cracked_from_file, pattern_CRACKED)
                file.close()
        else:
            print('Cracked hash or Hash file does not exist, please check the filename')
        NTLM.Match_Helper(isCracked_hash, isCracked_password, nonCracked_hash, nonCracked_username)

    def Match_Helper (isCracked_hash, isCracked_password, nonCracked_hash, nonCracked_username):
        for y in range (len(nonCracked_hash)):
            for x in range (len(isCracked_hash)):
                if (isCracked_hash[x] == nonCracked_hash[y]):
                    if(isCracked_password[x] == ''):
                        isCracked_password[x] = '(NO_PASSWORD_DATA)'
                    crackedAccount = User(nonCracked_username[y], nonCracked_hash[y], isCracked_password[x])
                    NTLM.userList.append(crackedAccount)
        NTLM.User_List_To_File()

    def Remove_Unwanted_Chars(list): # done
    # This function removes the null byte at the end of an item in a list
        list = [
            item.replace('\r', '').replace('\n','') for item in list              
        ]
        return list

    def File_Clenser(input):            # might want to make sure that I can get NTLM hashes from this function
    #Function to go through a file of DCC2 hashes and clean them up
        hash_list = []          # list of uncleaned hashes
        
        # Checking to make sure the file exists
        if (os.path.exists(input) == True):
            # open the file and add each hash into a list
            print('Starting Clense...')         #I'm assuming that this is part of the problem for the printing
            with open(input) as file: 
                hash_list = file.readlines()
            # clean the hashes from the list
            NTLM.List_Cleanser(hash_list, 'tmp')
            # closing the file
            file.close()
        # just in case you put in the wrong file name
        else:  
            print('file does NOT exist')

    def List_Cleanser (hash_list, input):       # might need to make sure that this function can parse NTLM
    # Function to clean a list of dcc2 hashes
        tmp_hashes = []         # temporary placeholder
        tmp_hashes = NTLM.Pattern_Parser (hash_list, NTLM.pattern_DCC2)
        # go through the list and remove null bytes
        cleaned_hashes = NTLM.Remove_Unwanted_Chars(tmp_hashes)
        # go through list and remove the duplicates
        cleaned_hashes = NTLM.Remove_Duplicates(cleaned_hashes)
        # send the list to the 'list_to_file' function
        NTLM.list_to_file(cleaned_hashes, input)

    def Remove_Duplicates(hashes): #done
    # Function ot remove the duplicates from a list
        hashes = list(dict.fromkeys(hashes))
        return (hashes)

    def list_to_file(list, name): #done
    #Function to take a list and puth the list in a file line-by-line
        file = open( name+'.cleaned', 'w')
        for items in list:
            file.write(items+"\n")
        file.close()
        print('Cleaning finished output will be in the file named', name+'.cleaned')    #also might be part of the problem
    
    def User_List_To_File():
        file = open( 'Credentials', 'w')
        for x in range (len(NTLM.userList)):
            file.write(NTLM.userList[x].username+"   ")
            file.write(NTLM.userList[x].hash+"   ")
            file.write(NTLM.userList[x].password + "\n")
        file.close()
        print('Cleaning finished output will be in the file named Credentials')