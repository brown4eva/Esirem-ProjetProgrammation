
import numpy as np
class CryptoRSA():
    def __init__(self):
        self.privateKey = None
        self.publicKey = None

    @staticmethod
    def _pgcd(e, f):
        if e > f:
            while e % f != 0:
                e, f = f, e % f
            return (f)
        else:
            while f % e != 0:
                f, e = e, f % e
            return (e)

    @staticmethod
    def _estPremier(nombre):
        if (not isinstance(nombre, int) or nombre < 0):
            return False
        elif nombre <= 3:
            return True
        elif nombre % 2 == 0:
            return False
        else:
            Racine = np.sqrt(nombre)
            idx = 3
            while idx <= Racine:
                if nombre % idx == 0:
                    return False
                idx += 2
            return True

    def _numIntDigits(self, number):
        digit = 1;
        while number > 10:
            digit += 1
            number = number / 10
        return digit

    def _inputPremier(self, char):
        while (True):
            try:
                value = int(input(f"Veuillez entrer un nombre premier {char}\n"))
                if self._estPremier(value):
                    return value
                else:
                    print("Le nombre n'est pas un premier")
            except:
                print("Le caractère n'est pas un nombre")

    def _inputPGCD(self, char, number):
        while (True):
            try:
                value = int(input(f"Veuillez entrer un nombre premier {char}\n"))
                if self._pgcd(value,number) == 1:
                    return value
                else:
                    print(f"Le nombre {char} n'est pas premier avec {number}")
            except:
                print("Le caractère n'est pas un nombre")

    def generateKey(self):
        p = self._inputPremier("P")
        q = self._inputPremier("Q")
        n = p * q;
        f = (p - 1) * (q - 1)
        e = self._inputPGCD("E", f)
        tm = 1
        d = 1
        while (((d * e) % f) != 1):
            tm = tm + 1
            d = round(tm * f / e)
        d = int(d)
        self.privateKey = (n, d)
        self.publicKey = (n, e)
        print(f"Cle privee: {self.privateKey}")
        print(f"Cle publique:{self.publicKey}")

    def chiffrement(self, text):
        if self.publicKey is None:
            return
        text = text.upper()
        textInAscii = ""
        crypText = ""
        for carac in text:
            ascii = ord(carac)
            textInAscii = textInAscii + str(ascii)
        numDigit = self._numIntDigits(self.publicKey[0])-1
        shift = numDigit - len(textInAscii) % numDigit
        for idx in range(shift):
            textInAscii += "0"
        nBIteration = int(len(textInAscii) / numDigit)
        for idx in range(nBIteration):
            bloc = ""
            for j in range(numDigit):
                bloc += textInAscii[numDigit*idx+j]
            C = (int(bloc)** self.publicKey[1]) % self.publicKey[0]
            crypText = crypText + str(C)
            if(idx != nBIteration -1):
                crypText += " "
        return crypText

    def dechiffrement(self, crypText):
        text = ""
        numList = "";
        crypText = crypText.split(" ")
        for idx in crypText:
            value = (int(idx)** self.privateKey[1]) % self.privateKey[0]
            numList += str(value)
        for idx in range(int(len(numList) / 2)):
            asciiVal = ""
            for j in range(2):
                asciiVal += numList[idx*2 + j]
            text += chr(int(asciiVal))
        return text

a = CryptoRSA()
a.generateKey()
txt = "Hello"
c = a.chiffrement(txt)
print(c, a.dechiffrement(c))
