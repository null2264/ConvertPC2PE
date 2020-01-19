import os
from blocksPC import pcfile
from blocksPE import pefile
#Variables
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Supported Version :", bcolors.BOLD + "PC 1.15.x -> PE 1.14.x.x")
print(bcolors.WARNING + "WARNING!", bcolors.ENDC + "This converter cant convert shaderpack and optifine required resource pack!")
inPCResource = str(input("What is the folder name of the Resource Pack ? ") or "BlockinBlock")

pngdir="/home/ziro/my Files/PE Port Project/" + inPCResource + "/assets/minecraft/textures/block/"
inPEResource = inPCResource + "PE"
pngdirPE="/home/ziro/my Files/PE Port Project/" + inPEResource + "/textures/blocks/"

#pcfile = blocks.pcfile
#pefile = blocks.pefile

input0=1
error=0
blockOK=0
blockNO=0

print("")
print("LOGS:")
# ---------- Check folders ----------
if not os.path.exists(pngdirPE):
    os.makedirs(pngdirPE)
else:
    print("Folder", inPEResource , "already exist, skipped")
    pass

# --------- Rename -----------------

while input0 < len(pcfile):
    try : # Try to do the following commands
        os.rename(pngdir + pcfile[input0], pngdirPE + pefile[input0])
        if pcfile[input0] == pefile[input0]:
            print(bcolors.OKGREEN + "OK!", bcolors.ENDC + pcfile[input0], "Have the same name with PE texture name, no need to rename")
        else:
            print(bcolors.OKGREEN + "OK!", bcolors.ENDC + pcfile[input0], "Successfully converted,", "renamed to", pefile[input0])
        input0 = input0 + 1
        blockOK = blockOK + 1
    except: # Keeps going even if some files is not found, also print out which file it is"
        pass
        print(bcolors.FAIL + "ERROR!", bcolors.ENDC + "The following file:", pcfile[input0], "is not found, skipped")
        input0 = input0 + 1
        error = error + 1
        blockNO = blockNO + 1
print("---------------------------------------------")
print(bcolors.BOLD + "Summary" + bcolors.ENDC)
print("---------------------------------------------")
print(blockOK, "blocks successfully converted")
print(blockNO, "blocks failed being converted")
if error == 1: # Print out how many errors there are
    print("Convertion completed with", error, "error")
elif error >=2:
    print("Convertion completed with", error, "errors")
elif error == 0:
    print("Convertion completed with no error")
else:
    print("Convertion failed")
print("---------------------------------------------")
# My notes to user
print("* Leaves will not converted, i haven't figured it out the method to do image proccessing with python... Heck i dont even know if its possible")
