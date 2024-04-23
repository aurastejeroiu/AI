# -*- coding: utf-8 -*-
"""
In this file your task is to write the solver function!
"""

from fuzzy_sets import *


def fuzzy_triangle(value, left, right, mean=None):
    # print(value, left, right, mean)

    if mean is None:
        mean = (left + right) / 2

    if left is not None and left < value < mean:
        return (value - left) / (mean - left)

    if right is not None and mean <= value < right:
        return (right - value) / (right - mean)

    return 0


def fuzzy_value(value, ranges):
    # result = {}
    #
    # for r in ranges:
    #     membership_degree = fuzzy_triangle(value, *ranges[r])
    #     result[r] = membership_degree
    #
    # return result

    return {r: fuzzy_triangle(value, *ranges[r]) for r in ranges}


def solver(t, w):
    """
    Parameters
    ----------
    t : TYPE: float
        DESCRIPTION: the angle theta
    w : TYPE: float
        DESCRIPTION: the angular speed omega

    Returns
    -------
    F : TYPE: float
        DESCRIPTION: the force that must be applied to the cart
    or
    
    None: if we have a division by zero

    """

    # these values are from the example and are used for debugging
    # t = 7
    # w = -0.5

    # Steps #

    #   ● compute the membership degrees for θ and ω to each set using the data from
    #     Figures 2 and 3, and using the formula for triangles from the lecture.

    theta_membership = fuzzy_value(t, theta_ranges)
    omega_membership = fuzzy_value(w, omega_ranges)

    # print(theta_membership, omega_membership)
    # time.sleep(1)

    #   ● compute according to Table 1 the membership degree of F to each set. Look in the table and
    #     for each cell we take the minimum of the membership values of the index set.

    degree_of_force = {}

    for theta_set in rules_table:
        for omega_set, value in rules_table[theta_set].items():
            minimum = min(theta_membership[theta_set], omega_membership[omega_set])
            if value not in degree_of_force:
                degree_of_force[value] = minimum
            else:
                degree_of_force[value] = max(minimum, degree_of_force[value])

    #    ● defuzzify the results for F using a weighted average of the membership degrees
    #     and the b values of the sets.

    total = sum(degree_of_force.values())
    if total == 0:
        return None

    result = 0
    for value in degree_of_force.keys():
        result += degree_of_force[value] * weights[value]

    result /= total

    return result
























