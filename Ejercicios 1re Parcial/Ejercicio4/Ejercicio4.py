from kanren import run, var, Relation, facts
a = var() 
b = var()
#Relacion padres
padres = Relation()
facts(padres, ("Renan","Ivan"),("Renan","Jesus"),("Renan","Yessamin"),("Renan","Yoshua"),
              ("Maria","Ivan"),("Maria","Jesus"),("Maria","Yessamin"),("Maria","Yoshua"),
              ("Maximo","Renan"),("Maximo","Mauro"),("Maximo","Javier"),("Maximo","Carminia"),("Maximo","Nayda"),("Maximo","Malena"),
              ("Jesusa","Monica")
             )
#Relacion hijos
hijos = Relation()
facts(hijos,  ("Ivan","Renan"),("Jesus","Renan"),("Yessamin","Renan"),("Yoshua","Renan"),
              ("Ivan","Maria"),("Jesus","Maria"),("Yessamin","Maria"),("Yoshua","Maria"), 
              ("Renan","Maximo"),("Mauro","Maximo"),("Javier","Maximo"),("Carminia","Maximo"),("Nayda","Maximo"),("Malena","Maximo"),
              ("Monica","Jesusa")
              )
#Relacion abuelos
abuelos = Relation()
facts(abuelos, ("Maximo","Ivan"),("Maximo","Jesus"),("Maximo","Yessamin"),("Maximo","Yoshua"),              
               ("Jesusa","Ivan"),("Jesusa","Jesus"),("Jesusa","Yessamin"),("Jesusa","Yoshua"),              
               )
#Relacion Tios
tios = Relation()
facts(tios,   ("Mauro","Ivan"),    ("Javier","Ivan"),    ("Carminia","Ivan"),    ("Malena","Ivan"),    ("Nayda","Ivan"),    ("Monica","Ivan"),
              ("Mauro","Jesus"),   ("Javier","Jesus"),   ("Carminia","Jesus"),   ("Malena","Jesus"),   ("Nayda","Jesus"),   ("Monica","Jesus"),
              ("Mauro","Yessamin"),("Javier","Yessamin"),("Carminia","Yessamin"),("Malena","Yessamin"),("Nayda","Yessamin"),("Monica","Yessamin"),
              ("Mauro","Yoshua"),  ("Javier","Yoshua"),  ("Carminia","Yoshua"),  ("Malena","Yoshua"),  ("Nayda","Yoshua"),  ("Monica","Yoshua"),
              )

primos = Relation()
facts(primos, ("Sebastian","Ivan"),    ("Joel","Ivan"),    ("Damaris","Ivan"),    ("Belen","Ivan"),    ("Danilo","Ivan"),                         
              ("Sebastian","Jesus"),   ("Joel","Jesus"),   ("Damaris","Jesus"),   ("Belen","Jesus"),   ("Danilo","Jesus"),                           
              ("Sebastian","Jesus"),   ("Joel","Jesus"),   ("Damaris","Jesus"),   ("Belen","Jesus"),   ("Danilo","Jesus"),                            
              ("Sebastian","Yessamin"),("Joel","Yessamin"),("Damaris","Yessamin"),("Belen","Yessamin"),("Danilo","Yessamin"),              
              ("Sebastian","Yoshua"),  ("Joel","Yoshua"),  ("Damaris","Yoshua"),  ("Belen","Yoshua"),  ("Danilo","Yoshua"),
              )

hermanos = Relation()
facts(hermanos,("Ivan","Jesus"),("Ivan","Yessamin"),("Ivan","Yoshua"),
               ("Jesus","Ivan"),("Jesus","Yessamin"),("Jesus","Yoshua"),
               ("Yessamin","Ivan"),("Yessamin","Jesus"),("Yessamin","Yoshua"),
               ("Yoshua","Ivan"),("Yoshua","Jesus"),("Yoshua","Yessamin"),
               ("Renan","Mauro"),("Renan","Javier"),("Renan","Carminia"),("Renan","Nayda"),("Renan","Malena"),
               ("Javier","Renan"),("Javier","Mauro"),("Javier","Carminia"),("Javier","Nayda"),("Javier","Malena"),
               ("Carminia","Renan"),("Carminia","Javier"),("Carminia","Mauro"),("Carminia","Nayda"),("Carminia","Malena"),
               ("Nayda","Renan"),("Nayda","Javier"),("Nayda","Carminia"),("Nayda","Mauro"),("Nayda","Malena"),
               ("Malena","Mauro"),("Malena","Javier"),("Malena","Carminia"),("Malena","Nayda"),("Malena","Renan"),
               ("Joel","Damaris"),("Joel","Belen"),
               ("Damaris","Joel"),("Damaris","Belen"),
               ("Belen","Damaris"),("Belen","Joel"),   
               )

print("\n ---------------------------------------------------------- \n")
print("Ini Relación---> PADRES \n")
print("¿Quien es padre de Ivan(hijo)?")
print(run(1,a,padres(a,"Ivan")))
print("")
print("2 hijos de Maria(padre)")
print(run(2,b,padres("Maria",b)))
print("\nFin Relación---> PADRES")

print("\n ---------------------------------------------------------- \n")

print("Ini Relación---> HIJOS \n")
print("3 hijos del padre X")
print("Padre X: Renan")
print(run(3,a,hijos(a,"Renan")))
print("")
print("Padres del hijo Y")
print("Hijo Y: Jesus")
print(run(2,b,hijos("Jesus",b)))
print("\nFin Relación---> HIJOS")

print("\n ---------------------------------------------------------- \n")

print("Ini Relación---> ABUELOS \n")
print("Un abuelo del nieto X")
print("Nieto X: Yoshua")
print(run(1,a,abuelos(a,"Yoshua")))
print("")
print("nietos del abuelo Y")
print("Abuelo Y: Maximo")
print(run(2,b,abuelos("Maximo",b)))
print("\nFin Relación---> ABUELOS")

print("\n ---------------------------------------------------------- \n")

print("Ini Relación---> TIOS \n")
print("4 Tios del sobrino X")
print("sobrino X: Jesus")
print(run(4,a,tios(a,"Jesus")))
print("")
print("2 sobrinos del Tio Y")
print("Tio Y: Javier")
print(run(2,b,tios("Javier",b)))
print("\nFin Relación---> TIOS")

print("\n ---------------------------------------------------------- \n")

print("Ini Relación---> PRIMOS \n")
print("3 Primos del primo X")
print("Primo X: Yoshua")
print(run(3,a,primos(a,"Jesus")))
print("")
print("2 primos del primo Z")
print("Primo Z: Danilo")
print(run(2,b,primos("Danilo",b)))
print("\nFin Relación---> PRIMOS")

print("\n ---------------------------------------------------------- \n")

print("Ini Relación---> HERMANOS \n")
print("1 Hermano del hermano X")
print("Hermano X: Ivan")
print(run(1,a,hermanos(a,"Ivan")))
print("")
print("2 hermanos del hermano Z")
print("hermano Z: Yoshua")
print(run(2,b,hermanos("Yoshua",b)))
print("\nFin Relación---> HERMANOS")

print("\n ---------------------------------------------------------- \n")
