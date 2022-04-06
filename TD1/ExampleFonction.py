def resolveEquation ( x2 = 0 , x1 = 0 , x0 = 0 ):
    rSolve = None
    discriminant = np.power( x1 ,2 ) - 4 * x2 * x0
    if discriminant == 0 :
       rSolve = -x1 / ( 2.0 * a )
    elif discriminant > 0 :
        rSolve = (( -x1 - np.sqrt( discriminant ))/( 2.0 * a ) ,( - x1 + np.sqrt ( discriminant ))/ ( 2.0 * a ))
    return rSolve
    
print(resolveEquation(2,-1, -9)
