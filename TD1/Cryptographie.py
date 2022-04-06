
class CryptoRSA ():
    def __init__ ( self ):
        self.privateKey = None
        self.publicKey = None
        ...
    def generateKey ( self ):
        ...
        self.privateKey = (e , d )
        self.publicKey = (n , d )

    def chiffrement ( self , text ):
        if self.publicKey is None:
            print(f"Public key is None")
            return
        text = text.upper()

        return crypText


    def dechiffrement ( self , crypText ):
        text = " "
        numList = " " ;
        crypText = crypText . split ( " " )
        for idx in crypText :
            value = ( int ( idx )** self . privateKey [ 1 ]) % self . privateKey [ 0 ]
            numList += str ( value )
        for idx in range ( int ( len ( numList ) / 2 )):
            asciiVal = " "
        for j in range ( 2 ):
            asciiVal += numList [ idx * 2 + j ]
        text += chr ( int ( asciiVal ))
        return text
