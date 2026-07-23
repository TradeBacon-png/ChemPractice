print("------------------------------")
print("-----Molecular Mass Calc------")
print("------------By:JLo------------")
print("------------------------------")
print("-----Comp.Chem-Problem-#1-----")
print("------------------------------")

mass = 0.0
compound = input("Compound?")

from elements import atomweight

def chemparse(compound):
    length = len(compound)
    i = 0
    element_num = {}
    while i < length:
        subtemp = ""
        eltemp = ""
        if compound[i].isupper():
            eltemp = compound[i]
            i += 1
        while i < length and compound[i].islower():
            eltemp += compound[i]
            i += 1
        while i < length and compound[i].isdigit():
            subtemp += compound[i]
            i += 1
        sub = int(subtemp) if subtemp else 1
        if eltemp in element_num:
            element_num[eltemp] += sub
        else: element_num[eltemp]=sub
    return element_num



for element, sub in chemparse(compound).items():
    mass += atomweight[element]*sub
print("------------------------------")
print(f"The mass of your compound is {mass}")
print("------------------------------")