import argparse
from HashStuff.DCC2 import DCC2
from HashStuff.NTLM import NTLM
from User import User
from typing import List

userList: List[User] = []

# Argument parcer stuff
parser = argparse.ArgumentParser(description='Hash cleaner for the Domain Caches Credentials 2 hash type')
parser.parse_args
parser.add_argument('-d', '--DIRECTORY', type=str, help='Directory path of the files with the uncleaned DCC2 hashes', default=None)
parser.add_argument('-f', '--FILE', type=str, help='File path of the file with the uncleaned DCC2 hashes', default=None)
parser.add_argument('-m', '--MODE', type=str, help='Type of hash to be found from secretsdump files DCC2 or NTLM', default=None)
parser.add_argument('-M', '--MATCH', type=str, help='Match the cracked password with the user of that password', default=None)
parser.add_argument('-s', '--SECRETS', type=str, help='Path of the file with the secret dump hashes', default=None)
args = parser.parse_args()

# Regex patterns
pattern_DCC2 = r"(\$DCC2\$)(.*)"            
pattern_NTLM = r"(.*?):(.*?):(.*?):(.*?):::"
pattern_HASH = r"(.*?):(.*)(.*):(.*):::"        # need to capture groups 1 for the username and 4 for the hash
pattern_CRACKED= r"(.*?):(.*)"                  # for use with the cracked password file group 1 is the hash and group 2 is the username

if (args.FILE == None and args.SECRETS == None and args.DIRECTORY == None):
    print('Please be sure to include the filename: -f [FILENAME]')
elif(args.SECRETS != None):
    if (args.MODE == 'DCC2'):
        hashes = DCC2.Secrets_Parser(args.SECRETS, pattern_DCC2 )
        DCC2.List_Cleanser(hashes, 'secretdumps.DCC2')
    elif (args.MODE == 'NTLM'):
        hashes = NTLM.Secrets_Parser(args.SECRETS, pattern_NTLM )
        hashes = NTLM.Rem_Duplicates(hashes)
        NTLM.list_to_file(hashes, 'sectretsdump.NTLM')
    else:
        print('Please specify the mode: -m [DCC2 / NTLM]')
elif(args.DIRECTORY != None):
    if (args.MODE == 'DCC2'):
        DCC2.Directory_Parser(pattern_DCC2, args.DIRECTORY, 'DCC2')
    elif (args.MODE == 'NTLM'):
        NTLM.Directory_Parser(pattern_NTLM, args.DIRECTORY, 'NTLM')
    else:
        print('Please specify the mode: -m [DCC2 / NTLM]')
elif(args.MATCH != None):
    if (args.MATCH == '' and args.FILE == ''):
        print('Please include the file with the NTLM hashes and the file with the cracked hashes')
    else:
        NTLM.Match(args.FILE, args.MATCH, pattern_HASH, pattern_CRACKED)
else:
    NTLM.File_Clenser(args.FILE)