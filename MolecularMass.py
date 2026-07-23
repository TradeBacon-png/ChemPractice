from elements import chemparse, atomweight
print("------------------------------")
print("-----Molecular Mass Calc------")
print("------------By:JLo------------")
print("------------------------------")
print("-----Comp.Chem-Problem-#1-----")
print("------------------------------")

mass = 0.0
compound = input("Compound?")







for element, sub in chemparse(compound).items():
    mass += atomweight[element]*sub
print("------------------------------")
print(f"The mass of your compound is {mass}")
print("------------------------------")