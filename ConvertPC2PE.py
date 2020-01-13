import os
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

pcfile=["PC Textures' Name Patterns",
        "acacia_door_bottom.png",
        "acacia_door_top.png",
        "acacia_planks.png",
        "acacia_sapling.png",
        "acacia_trapdoor.png",
        "acacia_log.png",
        "acacia_log_top.png",
        "activator_rail.png",
        "activator_rail_on.png",
        "allium.png",
        "andesite.png",
        "anvil.png",
        "anvil_top.png",
        "attached_melon_stem.png",
        "attached_pumpkin_stem.png",
        "azure_bluet.png",
        "bamboo_large_leaves.png",
        "bamboo_singleleaf.png",
        "bamboo_small_leaves.png",
        "bamboo_stage0.png",
        "bamboo_stalk.png",
        "barrel_bottom.png",
        "barrel_side.png",
        "barrel_top.png",
        "barrel_top_open.png",
        "beacon.png",
        "bedrock.png",
        "bee_nest_bottom.png",
        "bee_nest_front.png",
        "bee_nest_front_honey.png",
        "bee_nest_side.png",
        "bee_nest_top.png",
        "beehive_end.png",
        "beehive_front.png",
        "beehive_front_honey.png",
        "beehive_side.png",
        "beetroots_stage0.png",
        "beetroots_stage1.png",
        "beetroots_stage2.png",
        "beetroots_stage3.png",]
pefile=["PE Textures' Name Pattern",
        "door_acacia_lower.png",
        "door_acacia_upper.png",
        "planks_acacia.png",
        "sapling_acacia.png",
        "acacia_trapdoor.png",
        "log_acacia.png",
        "log_acacia_top.png",
        "rail_activator.png",
        "rail_activator_powered.png",
        "flower_allium.png",
        "stone_andesite.png",
        "anvil_base.png",
        "ancil_top_damaged_0.png",
        "melon_stem_connected.png",
        "pumpkin_stem_connected.png",
        "flower_houstonia.png",
        "bamboo_leaf.png",
        "bamboo_singleleaf.png",
        "bamboo_small_leaf.png",
        "bamboo_sapling.png",
        "bamboo_stem.png",
        "barrel_bottom.png",
        "barrel_side.png",
        "barrel_top.png",
        "barrel_top_open.png",
        "beacon.png",
        "bedrock.png",
        "bee_nest_bottom.png",
        "bee_nest_front.png",
        "bee_nest_front_honey.png",
        "bee_nest_side.png",
        "bee_nest_top.png",
        "beehive_top.png",
        "beehive_front.png",
        "beehive_front_honey.png",
        "beehive_side.png",
        "beetroots_stage_0.png",
        "beetroots_stage_1.png",
        "beetroots_stage_2.png",
        "beetroots_stage_3.png",]

input0=1
error=0

print("")
print("LOGS:")
if not os.path.exists(pngdirPE):
    os.makedirs(pngdirPE)
else:
    print("Folder", inPEResource , "already exist, skipped")
    pass

while input0 < len(pcfile):
    try : # Try to do the following commands
        os.rename(pngdir + pcfile[input0], pngdirPE + pefile[input0])
        if pcfile[input0] == pefile[input0]:
            print(bcolors.OKGREEN + "OK!", bcolors.ENDC + pcfile[input0], "Have the same name with PE texture name, no need to rename")
        else:
            print(bcolors.OKGREEN + "OK!", bcolors.ENDC + pcfile[input0], "Successfully converted,", "renamed to", pefile[input0])
        input0 = input0 + 1
    except: # Keeps going even if some files is not found, also print out which file it is"
        pass
        print(bcolors.FAIL + "ERROR!", bcolors.ENDC + "The following file:", pcfile[input0], "is not found, skipped")
        input0 = input0 + 1
        error = error + 1
print("---------------------------------------------")
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
print("* Trapdoors only need to be moved to", pngdirPE)
