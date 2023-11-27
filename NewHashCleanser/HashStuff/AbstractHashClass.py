from abc import ABC, abstractmethod

class Hash(ABC):
    
    hashes = []
    pattern = ""

    @abstractmethod
    def Parse(): #will need the secretsdump file or directory as well as the hash type
        # This function uses regular expression to fing NTLM or DCC2 hashes and returns the hashes in a list
        pass

    def Match(): #will need the list of cracked hashes and the list of uncracked hashes
        # Function to grab the hash username and password information and return lists containing that information
        pass

    def RemoveUnwantedChars(): #Will need the list of hashes
        # This function removes the null byte at the end of an item in a list
        pass
# For the regex for the matching function
#   Hashes
#       group 1: username
#       group 4: hash
#
#   cracked
#       group 1: hash
#       group 2: password