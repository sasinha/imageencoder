from modules import modulo_inverse_matrix as mim
import numpy as np


def trip_mod_dot(m1, m2, mod):
    return np.mod(np.dot(m1[0], m2[0]), mod), np.mod(np.dot(m1[1], m2[1]), mod), np.mod(np.dot(m1[2], m2[2]), mod)


def inv_color_matrix(rgb, mod):
    return mim.inverse_matrix(rgb[0], mod), mim.inverse_matrix(rgb[1], mod), mim.inverse_matrix(rgb[2], mod)


def random_color_matrix(n, mod):
    return mim.random_mod_matrix(0, mod, (n,n)), mim.random_mod_matrix(0, mod, (n,n)), \
           mim.random_mod_matrix(0, mod, (n,n))
