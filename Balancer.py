import numpy as np
import sympy as sp
import math
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("------------------------------")
print("-------Reaction Balancer------")
print("------------By:JLo------------")
print("------------------------------")
print("-----Comp.Chem-Problem-#2-----")
print("------------------------------")

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

x = input("Enter the reaction you wish to be balanced:")
equation = x.split(">")
react = equation[0].split("+")
prod = equation[1].split("+")
allreact = [chemparse(comp) for comp in react]
allprod = [chemparse(comp) for comp in prod]
masterlist = set()
for thing in allreact + allprod:
    for smallthing in thing.keys():
        masterlist.add(smallthing)
masterlist = list(masterlist)
matrix = sp.zeros(len(masterlist),len(react)+len(prod))
for i, element in enumerate(masterlist):
    for j, dict in enumerate(allreact):
        if element in dict:
            matrix[i,j]=dict[element]
    for j, dict2 in enumerate(allprod):
        if element in dict2:
            matrix[i, j+len(allreact)] = -dict2[element]
coeff = matrix.nullspace()
denoms = coeff[0].tolist()
denominators = []
for obj in denoms:
    denominators.append(obj[0].q)
least = math.lcm(*denominators)
finalco = [num[0]*least for num in denoms]
equation = ""
for item in react:
    co=str(finalco[react.index(item)])
    if co == "1":
        co = ""
    co += item
    equation += co
    if react.index(item) < (len(react)-1):
        equation +=" + "
equation += " -> "
for item in prod:
    co=str(finalco[prod.index(item) + len(react)])
    if co == "1":
        co = ""
    co += item
    equation += co
    if prod.index(item) < (len(prod)-1):
        equation +=" + "
print(equation)
input("--------Enter to quit--------")