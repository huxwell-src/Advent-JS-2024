'''
Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, 
pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. 
Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.

Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados)
y devuelva una nueva lista sin duplicados, ordenada en orden ascendente.
'''

from typing import List, Union

def prepare_gifts(gifts: List[Union[int, float]]) -> List[Union[int, float]]:
    return sorted(set(gifts))