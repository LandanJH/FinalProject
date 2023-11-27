from abc import ABC, abstractmethod
import os
import re

class Hash(ABC):
    
    @abstractmethod
    def Parse():
        pass

class DCC2(Hash):

    hashes = []
    pattern_DCC2 = r"(\$DCC2\$)(.*)"    

    def Parse(self):
        print('you made it here')


something = DCC2()
something.Parse()