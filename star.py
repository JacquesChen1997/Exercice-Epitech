n=int(input("Quel chiffre ?:"))
espace = " "
etoile = "*"
retour= ""

def repeter(variable,nombre):
	return variable*nombre;

for i in range (n) :
#le chapeau
	retour+=repeter(espace,2*n)
	if (n==1) :
		retour+=espace
	retour+=repeter(espace,((n-1)-i)) + etoile
	if (i>0) :
		retour+=repeter(espace,((i-1)*2+1)) + etoile
	retour+="\n"

#le bras gauche	
retour+=repeter(etoile,2*n+1)

#le vide
if (n==1) :
	retour+=espace	
else : 
	retour+=repeter(espace,(n+2))
	
#le bras droit
retour+= repeter(etoile,2*n+1) + "\n"

for i in range (1,n+1) :
#Le bras gauche qui descend
	retour+=repeter(espace,i) + etoile
	retour+=repeter(espace,2*n)
	if (n==1) :
		retour+=espace
		
#le bras droit qui descend
	else :
		retour+=repeter(espace,2*(n-2)+1)	
	retour+=repeter(espace,2*n-2*i)		
	retour+= etoile + "\n"
	
#le bras gauche qui remonte
for i in range (n-1,0,-1) :
	retour+=repeter(espace,i) + etoile
	retour+=repeter(espace,2*n-1)
	if (n==1) :
		retour+=espace
	
	else :
		retour+=repeter(espace,2*(n-2)+1)	
	retour+=repeter(espace,2*n-2*i+1)		
	retour+= etoile + "\n"

#le bras gauche	
retour+=repeter(etoile,2*n+1)

#le vide
if (n==1) :
	retour+=espace	
else : 
	retour+=repeter(espace,(n+2))
	
#le bras droit
retour+= repeter(etoile,2*n+1) + "\n"

#le chapeau inversé
for i in range (n) :
	if (n==1) :
		retour+=espace
	retour+=repeter(espace,2*n+i) + etoile
	
	if (i < n-1) :
		retour+=repeter(espace,2*(n-i)-3) + "*\n"
	
print(retour)	

