import sys
import os


# Kjører copycase

#PATH = "I:\\STOLAV - Kreftklinikken\\Avdelinger kreft\\Avdeling for stråleterapi\\Fysikere\\Jacob\\CopyCase"

PATH = "H:/Dokumenter/Github/CopyCase"
sys.path.append(PATH)

import CopyCase as copycase

copycase.copycase(PATH)
