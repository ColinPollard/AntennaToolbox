# Author: Colin Pollard
# Date: 11/4/2020
# Calculates the width of a microstrip line given a height, impedance, and relative permittivity.
from Core.Microstrip import estimateS

print("Enter effective permittivity (Epsilon_R)")
EpsilonR = float(input())

print("Enter the height of the microstrip (mm)")
height = float(input()) / 1000

print("Enter the desired characteristic impedance (Z_0)")
Z_0 = float(input())

s = estimateS(EpsilonR, Z_0)
print("Estimated width / height ratio: " + str(s))

width = s * height * 1000
print("Width = " + str(width) + " (mm)")
