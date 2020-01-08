#!/usr/bin/python
#coded by:dkvizowna
import urllib2

fuser = open('usuarios.txt')
usuarios = fuser.read().split('\n')

fpass = open('senhas.txt')

senhas = fpass.read().split('\n')

for usuario in usuarios:
   for senha senhas:
print "Começando... %s : %s"%(usuario,senha)