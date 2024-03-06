import numpy as np

class CryptoRSA():
    def __init__(self):
        # Initialize private and public keys
        self.privateKey = None
        self.publicKey = None

    @staticmethod
    def _pgcd(a, b):
        """
        Computes the greatest common divisor (GCD) of two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Greatest common divisor of a and b
        """
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _estPremier(number):
        """
        Check if the provided number is prime.
        
        :param number: The number to check
        :return: True if number is prime, False otherwise
        """
        if (not isinstance(number, int) or number < 2):
            return False
        if number <= 3:
            return number > 1
        if number % 2 == 0:
            return False
        sqrt_n = int(np.sqrt(number))
        for i in range(3, sqrt_n + 1, 2):
            if number % i == 0:
                return False
        return True

    def _numIntDigits(self, number):
        """
        Count the number of digits in an integer.
        
        :param number: The number to count digits of
        :return: Number of digits
        """
        digit = 1
        while number >= 10:
            digit += 1
            number /= 10
        return digit

    def _inputPremier(self, char):
        """
        for user to input a prime number with error checking.
        
        :param char: The character representation for the input prompt
        :return: A prime number entered by the user
        """
        while True:
            try:
                value = int(input(f"Please enter a prime number {char}:\n"))
                if self._estPremier(value):
                    return value
                else:
                    print("The number is not prime.")
            except ValueError:
                print("That is not a valid number.")

    def _inputPGCD(self, char, number):
        """
        for user input a number that is coprime with another.
        
        :param char: The character representation for the input prompt
        :param number: The number to be coprime with
        :return: A number entered by the user that is coprime with 'number'
        """
        while True:
            try:
                value = int(input(f"Please enter a coprime number for {char}:\n"))
                if self._pgcd(value, number) == 1:
                    return value
                else:
                    print(f"The number {value} is not coprime with {number}.")
            except ValueError:
                print("That is not a valid number.")

    def generateKey(self):
        p = self._inputPremier("P")
        q = self._inputPremier("Q")
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self._inputPGCD("E", phi)
        d = pow(e, -1, phi)
        self.privateKey = (n, d)
        self.publicKey = (n, e)
        print(f"Private key: {self.privateKey}")
        print(f"Public key: {self.publicKey}")

    def chiffrement(self, text):

        if self.publicKey is None:
            return "Public key is not generated."
        
        # Convert text to uppercase and to ASCII
        text = text.upper()
        textInAscii = ''.join(str(ord(char)) for char in text)
        
        # Determine the size of blocks
        numDigit = self._numIntDigits(self.publicKey[0]) - 1
        textInAscii += "0" * ((numDigit - len(textInAscii) % numDigit) % numDigit)
        
        # Encrypt text in blocks
        crypText = ''
        for i in range(0, len(textInAscii), numDigit):
            block = int(textInAscii[i:i + numDigit])
            encryptedBlock = pow(block, self.publicKey[1], self.publicKey[0])
            crypText += str(encryptedBlock) + ' ' if i + numDigit < len(textInAscii) else str(encryptedBlock)
        
        return crypText.strip()

    def dechiffrement(self, crypText):
        if self.privateKey is None:
            return "Private key is not generated."
        
        decryptedText = ''
        for num in crypText.split():
            decryptedBlock = str(pow(int(num), self.privateKey[1], self.privateKey[0]))
            # Assuming two digits for each character
            decryptedText += ''.join(chr(int(decryptedBlock[i:i + 2])) for i in range(0, len(decryptedBlock), 2))
            
        return decryptedText

# Example usage
crypto_rsa = CryptoRSA()
crypto_rsa.generateKey()
txt = "Hello"
encrypted_txt = crypto_rsa.chiffrement(txt)
print(encrypted_txt, crypto_rsa.dechiffrement(encrypted_txt))