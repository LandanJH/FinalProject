    __  __           __       ________                               
   / / / /___ ______/ /_     / ____/ /__  ____ _____  ________  _____
  / /_/ / __ `/ ___/ __ \   / /   / / _ \/ __ `/ __ \/ ___/ _ \/ ___/
 / __  / /_/ (__  ) / / /  / /___/ /  __/ /_/ / / / (__  )  __/ /    
/_/ /_/\__,_/____/_/ /_/   \____/_/\___/\__,_/_/ /_/____/\___/_/     
                                                                   
Author: Landan
Purpose: Cleans and organizes hashes in a way that optimizes the password cracking procedure for PBF

# How to use
## Arguments

** -f (file) **
usage: specify a file that has the hashes you need parsed out
** -d (directory) **
usage: specify a directory that has the hashes you need parsed out
** -m (mode) **
usage: specify the mode or hash type that you are looking for (currently only NTLM and DCC2)
** -M (match) **
usage: matches the username, hash, and password information for the user profiles being cracked
