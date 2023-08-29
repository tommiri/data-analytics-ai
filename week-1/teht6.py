import math

class Murtoluku:
    def __init__(self, os, nim):
        self.os = os
        self.nim = nim
        
    def tulosta(self):
        print(f'{self.os} / {self.nim}')
        
    def sievenna(self):
        syt = math.gcd(self.os, self.nim)
        self.os //= syt
        self.nim //= syt
        

ml = Murtoluku(1024, 512)

ml.tulosta()
ml.sievenna()
ml.tulosta()

