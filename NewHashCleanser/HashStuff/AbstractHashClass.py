from abc import ABC, abstractmethod

class Hash(ABC):
    
    hashes = []
    pattern = ""
    pattern_HASH = r"(.*?):(.*)(.*):(.*):::"        # need to capture groups 1 for the username and 4 for the hash
    pattern_CRACKED= r"(.*?):(.*)"                  # for use with the cracked password file group 1 is the hash and group 2 is the username


                            ### These functions are for all of the parsing operations ###
    @abstractmethod
    def Pattern_Parse(): #will need the secretsdump file or directory as well as the hash type
        # This function uses regular expression to fing NTLM or DCC2 hashes and returns the hashes in a list
        pass

    @abstractmethod
    def Match_Parser(): #will need a list and the regex of the hash type
        #Function to grab the hash username and password information and return lists containing that information
        pass

    @abstractmethod
    def Directory_Parser(): #will need the pattern of the hash, name of the directory and the mode input
        #Function will go through a directory and parse all the information from all the files
        pass

    @abstractmethod
    def Secrets_Parser(): #will need the file name and the regex pattern used for parsing
        # function will go through secretsdump.py output (or normal files) and grab the specified hashed for further operations
        pass

                            ### All of these functions are for the matching operations ###
    @abstractmethod
    def Match(): #will need the list of cracked hashes and the list of uncracked hashes
        # Function to grab the hash username and password information and return lists containing that information
        pass

    @abstractmethod
    def Match_Helper(): #will need 4 strings what contain the 2 hashed and the username of the uncracked hash and the pass of the crached one
        # Function will vake the values and match them and return a user instance with the username, hash, and password values filled put
        pass

                            ### All of these functions are for the cleaning of data ###
    @abstractmethod
    def Remove_Unwanted_Chars(): #Will need the list of hashes
        # This function removes the null byte at the end of an item in a list
        pass

    @abstractmethod
    def File_Cleanser(): #will need a file name
        #Function will go through a file and clean the hashes for cracking
        pass

    @abstractmethod # will need a list of hashes and a file input
    def List_Cleanser():
        #Function will do the logic for all of the cleansing
        pass

    @abstractmethod
    def Remove_Duplicates(): # takes a list of hashes
        #Function will remove all of the duplicate hashes from a list
        pass

                            ### These functions are for all of the data to file operations ###
    @abstractmethod
    def List_To_File(): # will take a fist and a name for the output file
        #Function will make an output file of all the clean hashes
        pass
    
    @abstractmethod
    def User_List_To_File(): # Will take a userlist 
        #Function will make a neat file that will include all the credentials for the users
        pass
    

# For the regex for the matching function
#   Hashes
#       group 1: username
#       group 4: hash
#
#   cracked
#       group 1: hash
#       group 2: password

#FUNCTIONS WITHIN THE ORIGIONAL PROGRAM#
# Main ---> Cleanser.py
# UserListToFile ---> User_List_To_File
# Matching ---> Match_Helper
# Match_Parser ---> Match_Parser
# Pattern_Parser ---> Pattern_Parse
# Remove_Null ---> Remove_Unwanted_Chars
# Match ---> Match
# Directory_Parser ---> Directory_Parser
# List_Cleanser ---> List_cleanser
# Secrets_Parser ---> Secrets_Parser
# File_Cleanser ---> File_Cleanser
# Rem_Duplicates ---> Remove_Duplicates
# List_To_File ---> List_To_File