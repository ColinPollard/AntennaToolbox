# Author: Colin Pollard
# Date: 11/4/2020
# This program calculates the characteristic impedance of microstrip antenna lines.
import math


def propogationSpeed(epsilonEff):
    """
    Calculates the effective propagation speed mu_p.
    Source: Equation 2.35 Ulaby

    :param epsilonEff: Effective permittivity between the air and dielectric substrate.
    :return: mu_p
    """

    return 3E8 / math.sqrt(epsilonEff)


def widthRatio(width, height):
    """
    Calculates the width-to-height ratio, s.
    Source: Equation 2.37 Ulaby

    :param width: Width of the microstrip line
    :param height: Height of the microstrip line
    :return: S
    """

    return width / height


def effectivePermitivitty(epsilonR, s):
    """
    Calculates epsilon effective - the effective permittivity of the system.
    Source: Equation 2.38 Ulaby

    :param epsilonR: Dielectric relative permittivity.
    :param s: Width-to-thickness ratio w/h.
    :return: Relative permittivity, epsilon_r
    """

    # Create intermediate variables
    x = 0.56 * (((epsilonR - 0.9) / (epsilonR + 3)) ** 0.05)
    y = 1 + 0.02 * math.log((s ** 4 + 3.7E-4 * s ** 2) / (s ** 4 + 0.43))

    # Calculate final value
    epsilonEff = ((epsilonR + 1) / 2) + ((epsilonR - 1) / 2) * ((1 + (10 / s)) ** (-x * y))
    return epsilonEff


def characteristicImpedance(epsilonEff, s):
    """
    Calculates the more exact impedance Z_0 of a microstrip line.

    :param epsilonEff: Effective permittivity
    :param s: Width-to-height ratio
    :return: Characteristic impedance Z_0
    """

    # Calculate intermediate
    t = (30.67 / s) ** 0.75

    # Calculate final value
    Z_0 = (60 / math.sqrt(epsilonEff)) * math.log(((6 + (2 * math.pi - 6) * math.exp(-t)) / s) + math.sqrt(1 + (4/(s ** 2))))
    return Z_0


def estimateS(epsilonR, Z_0):
    """
    Estimates the width-to-height ratio S for a given relative permittivity epsilonR.
    Has an error of less than 2%.
    Source: Equation 2.42 / 2.43 Ulaby

    :param epsilonR: Relative permittivity
    :param Z_0: Desired characteristic impedance
    :return: Width to height ratio s
    """

    # Need to calculate based on the desired impedance
    if Z_0 <= (44 - 2*epsilonR):
        # Equation 2.42
        # Calculate intermediates
        q = (60 * (math.pi ** 2)) / (Z_0 * math.sqrt(epsilonR))
        # Calculate final value
        s = (2 / math.pi) * ((q - 1) - math.log((2 * q) - 1) + (((epsilonR - 1) / (2 * epsilonR)) * (math.log(q - 1) + 0.29 - (0.52 / epsilonR))))

    else:
        # Equation 2.43
        # Calculate intermediates
        p = math.sqrt((epsilonR + 1) / 2) * (Z_0 / 60) + ((epsilonR - 1) / (epsilonR + 1)) * (0.23 + (0.12 / epsilonR))
        # Calculate final value
        s = (8 * math.exp(p)) / (math.exp(2 * p) - 2)

    return s