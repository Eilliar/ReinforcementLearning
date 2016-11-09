################################################################################
# Dynamic Programing 101
#
# Author: Bruno G. Eilliar
#
# Notes:
# - Given a list of N coins, their values (V1, V2, ..., VN) and the total sum S,
# find the minimum number of coins int the sum of wich is S.
#
# Source: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
################################################################################

import numpy as np

S = 30
Min = np.inf*np.ones((30, 1))
