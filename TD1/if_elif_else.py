import datetime
birthOfYear = 2022
currentYear = datetime . datetime . now (). year
diff = currentYear - birthOfYear
if diff >= 18 :
    print ( " La personne est majeure " )
elif diff < 18 and diff >= 0 :
    print ( " La personne est mineure " )
else :
    print ( " Back to the futur " )
