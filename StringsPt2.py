fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it!')

"""
if word == 'banana' :
    print('All right, bananas.')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana' :
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
"""

#
greet = 'Hello Bob'
zap = greet.lower() #devuelve una copia en minusculas
print(zap)

print(greet)

print('Hi There' .lower())

#
stuff = 'Hello World'
type(stuff)
dir(stuff) #metodos en clases str

#
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

#
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)

www = greet.lower()
print(www)

#
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane') #metodo para remplazar un valor -- remplaza el nombre
print(nstr)

nstr = greet.replace('o', 'X') #remplaza caracteres especificos
print(nstr)

#
greet = '   Hello Bob   '
greet.lstrip()
greet.rsplit()
greet.strip()

#
line = 'Please have a nice day'
line.startswith('Please')

line.startswith('p')

#
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
"""PARCING AND EXTRACTING, Calcula la posicion donde se encuentra el caracter que solicitamos"""
sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos] #Rango de caracteres
print(host)