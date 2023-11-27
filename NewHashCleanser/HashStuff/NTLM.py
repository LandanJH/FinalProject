import re
import os
from HashStuff.AbstractHashClass import Hash

class NTLM(Hash):

    hashes = []
    pattern = r"(.*?):(.*?):(.*?):(.*?):::" # NTLM Regex pattern

    def Parse():
        pass

    def Match():
        pass