import Sboxes
import numpy as np
from operator import xor

INT_BITS = 32


def leftRotate(n, d):
    return ((n << d) | (n >> (INT_BITS - d))) & 0xFFFFFFFF


def rightRotate(n, d):
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF


def key_expansion():

    R = 11


def Sbox_fct(word):
    mask = 0X0000000F
    word_return = 0X00000000
    for i in range(4):
        index_ligne = word & mask
        mask = mask << 4
        index_colonne = word & mask
        mask = mask << 4
        word_return | (Sboxes.Sbox(index_ligne * 16 + index_colonne) << i * 8)
    return


def compute_W():
    N = 4
    K = [0X00000000, 0X00000000, 0X00000000, 0X00000000]
    rcon = [0X01000000, 0X02000000, 0X04000000, 0X08000000, 0X10000000,
            0X20000000, 0X40000000, 0X80000000, 0X1B000000, 0X36000000]
    W = [0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
         0X00000000, 0X00000000, 0X00000000]
    for i in range(len(W)):
        if(i < N):
            W[i] = K[i]
        elif(i >= N and i % N == 0):
            xor(xor(W[i-N], Sbox_fct(leftRotate(W[i-1], 16))), rcon[i/N])
        elif(i >= N and N > 6 and i % N == 4):
            xor(W[i-N],Sbox_fct(W[i-1]))
        else:
            xor(W[i-N],W[i-1])
