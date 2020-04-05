The code is in Pyhton3

from itertools import combinations
import numpy as np
import sys

def complement(bits): return [
    '_' if b is '_' else 
    '1' if b=='0' else '0' 
    for b in bits
]

class Quantum():
    def __init__(self, A):
        self.bits = ['_'] * A
        self.unkowns = list(range(A))
        self.reads(10)
        self.run()

    def reads(self, n):
        for _ in range(n):
            i = self.unkowns.pop()
            self.bits[i] = self.read_bits(i+1)
            self.unkowns = self.unkowns[::-1]
        self.update_state()

    def read_bits(self, i):
        print(i, flush=True)
        return input()

    def update_state(self):
        self.bits_c  = complement(self.bits)
        self.bits_cr = self.bits_c[::-1]
        self.bits_r  = complement(self.bits_cr)
        self.states = [self.bits, self.bits_c, self.bits_cr, self.bits_r]

    def get_test_idxe(self):
        candidates = list(set(range(B)) - set(self.unkowns))
        max_states = len(set(map(tuple, self.states)))
        for idx in combinations(candidates, 2):
            num_states = len(set(
                tuple(np.take(state, idx))
                for state in self.states
            ))
            if num_states == max_states: return idx

    def collapses(self):        
        test_idx = self.get_test_idxe()
        test = [self.read_bit(i+1) for i in test_idx]
                
        self.bits = next(state
            for state in self.states
            if test == list(np.take(state, test_idx))
        )

    def run(self):
        while True:
            self.collapses()
            try: self.reads(8)
            except IndexError: break
    

Test,A = map(int, input().split())
print('A:', A, file=sys.stderr)
for _ in range(Test): 
    array = Quantum(A)
    print('guess:', ''.join(array.bits), file=sys.stderr)
    print(''.join(array.bits), flush=True)
    if input() == 'N': sys.exit()