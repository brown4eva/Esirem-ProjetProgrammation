class Complex :
# Initialisation de la classse
    def __init__ ( self, real=0 , im=0 ):
        self.r = real
        self.i = im
# Representation de la classe
    def __repr__ ( self ):
        return " Nombre complexe : " + str ( self.r ) + " + " + str ( self.i ) + " i . "
# Addition entre nombre complexe
    def __add__ ( self , other ):
        return Complex ( self.r + other.r , self.i + other.i )
    # Retourne le module du nombre complexe
    def module ( self ):
        return np.sqrt ( np.power ( self.i , 2 ) + np . power ( self.r , 2 ))
        
 
varA = Complex( 2 ,2 )
varB = Complex( real = 4 , im = 3 )
print ( varA + varB )
print(f"Le module du nombre complexe est { varA . module ()}")
