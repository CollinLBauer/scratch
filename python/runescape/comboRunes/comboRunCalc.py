from exchangeItem import *
# This import will not work if I split my project into different modules.
# There is a way, and I'm trying to study python documentation to figure it out.
# Relative imports are possible, but they are horribly obfuscated for some goddamn reason.


nullItem = SyntheticItem()


def calcRunCost(essence, talisman, rune, binding=nullItem, numEssence=26, teleport=nullItem):
    return teleport.price + talisman.price + (numEssence * essence.price) + (numEssence * rune.price) + binding.price/16

def calcRunOutput(combo_rune, numEssence=26, bind=True):
    if bind:
        return numEssence * combo_rune.price
    else:
        return (numEssence * combo_rune.price) / 2

def calcRunXp():
    pass

def fastestXp():
    pass

def showDifference(cost,output):
    diff = output - cost
    if diff > 0:
        return "Profit: {}".format(diff)
    else:
        return "Loss:  {}".format(diff)


def main():
    # common
    print("Obtaining common item prices...", end="", flush=True)
    essence_pure = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Pure_essence")
    print(".", end="", flush=True)
    necklace_binding = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Binding_necklace")
    print(".", end="", flush=True)
    rune_astral = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Astral_rune")
    print(".", end="", flush=True)
    magic_imbue = SyntheticItem("Magic Imbue",(rune_astral.price*2))
    print("Done")


    # basic runes
    print("Obtaining basic rune prices...", end="", flush=True)
    rune_air = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Air_rune")
    print(".", end="", flush=True)
    rune_water = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Water_rune")
    print(".", end="", flush=True)
    rune_earth = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Earth_rune")
    print(".", end="", flush=True)
    rune_fire = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Fire_rune")
    print("Done")

    # talsmans
    print("Obtaining talisman prices...", end="", flush=True)
    talisman_air = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Air_talisman")
    print(".", end="", flush=True)
    talisman_water = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Water_talisman")
    print(".", end="", flush=True)
    talisman_earth = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Earth_talisman")
    print(".", end="", flush=True)
    talisman_fire = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Fire_talisman")
    print("Done")
    
    # combo runes
    print("Obtaining combo rune prices...", end="", flush=True)
    rune_mist = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Mist_rune")
    print(".", end="", flush=True)
    rune_dust = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Dust_rune")
    print(".", end="", flush=True)
    rune_mud = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Mud_rune")
    print(".", end="", flush=True)
    rune_smoke = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Smoke_rune")
    print(".", end="", flush=True)
    rune_steam = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Steam_rune")
    print(".", end="", flush=True)
    rune_lava = ExchangeItem("https://oldschool.runescape.wiki/w/Exchange:Lava_rune")
    print("Done")


    # Note that when making combination runes, when visiting one altar, you bring the talisman
    # and runes of the other element.
    # i.e. Earth runes at the Fire altar create Lava runes.


    # mist
    print("\nMist runes...")
    cost_mist_from_air = calcRunCost(essence_pure, talisman_water, rune_water, necklace_binding)
    cost_mist_from_water = calcRunCost(essence_pure, talisman_air, rune_air, necklace_binding)
    outp_mist = calcRunOutput(rune_mist)

    print("  from Air altar")
    print("    Cost:   {}".format(cost_mist_from_air))
    print("    Output: {}".format(outp_mist))
    print("    {}".format(showDifference(cost_mist_from_air, outp_mist)))
    
    print("  from Water altar")
    print("    Cost:   {}".format(cost_mist_from_water))
    print("    Output: {}".format(outp_mist))
    print("    {}".format(showDifference(cost_mist_from_water, outp_mist)))
    

    # dust
    print("\nDust runes...")
    cost_dust_from_earth = calcRunCost(essence_pure, talisman_air, rune_air, necklace_binding)
    cost_dust_from_air = calcRunCost(essence_pure, talisman_earth, rune_earth, necklace_binding)
    outp_dust = calcRunOutput(rune_dust)
    
    print("  from Earth altar")
    print("    Cost:   {}".format(cost_dust_from_earth))
    print("    Output: {}".format(outp_dust))
    print("    {}".format(showDifference(cost_dust_from_earth,outp_dust)))

    
    print("  from Air altar")
    print("    Cost:   {}".format(cost_dust_from_air))
    print("    Output: {}".format(outp_dust))
    print("    {}".format(showDifference(cost_dust_from_air,outp_dust)))


    # mud
    print("\nMud runes...")

    cost_mud_from_water = calcRunCost(essence_pure, talisman_earth,rune_earth, necklace_binding)
    cost_mud_from_earth = calcRunCost(essence_pure, talisman_water,rune_water, necklace_binding)
    outp_mud = calcRunOutput(rune_mud)

    print("  from Water altar")
    print("    Cost: {}".format(cost_mud_from_water))
    print("    Output: {}".format(outp_mud))
    print("    {}".format(showDifference(cost_mud_from_water,outp_mud)))

    print("  from Earth altar")
    print("    Cost: {}".format(cost_mud_from_earth))
    print("    Output: {}".format(outp_mud))
    print("    {}".format(showDifference(cost_mud_from_earth,outp_mud)))


    # smoke


    # steam

    # lava

    print("\nDone.")
    

main()