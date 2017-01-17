from __future__ import with_statement
import os, glob, argparse, filecmp, timeit 
import hashlib

# bardzo wazny import trzeba go

# ARGUMENTY ###################
###############################

parser_argumentow = argparse.ArgumentParser()
parser_argumentow.add_argument("-s", dest='sciezka',
                    const=sum, default="testy", nargs='?', 
                    help='sciezka zawierajace pliki testow(.in) oraz oczekiwane wyniki(.out)')
parser_argumentow.add_argument("-e", dest='plik',
                    const=sum, default="bin", nargs='?', 
                    help='pelna nazwa pliku wykonywalnego znajdujacego sie w tym samym folderze co sprawdzarka')

argumenty = parser_argumentow.parse_args()

###############################

pliki_wejsciowe = argumenty.sciezka+"/*.in"
plik_wykonywalny = argumenty.plik

###############################

oczekiwany_wynik = "test1.in"
wynikowy_plik = argumenty.sciezka+"/wynik"
przeszlo = True

###############################

poprawne = 0
wszystkie = 0

###############################

# glowna petla
for file in glob.glob(pliki_wejsciowe):
	wszystkie = wszystkie+1
	oczekiwany_wynik = os.path.splitext(file)[0]
	os.system("./"+plik_wykonywalny +" < " +file +" > "+ oczekiwany_wynik+"U.out")
	with open(oczekiwany_wynik+".out", "r") as text, open(oczekiwany_wynik+"U.out", "r") as exc:
		exclusions = [line.rstrip('\n') for line in exc]
		for line in text:
			if not any(exclusion in line for exclusion in exclusions):
				if line!='\n' or line!="":
					przeszlo = False
	if przeszlo:
		print file+" przeszlo poprawnie [ OK ]"
		poprawne = poprawne+1
	else:
		print file+" dal zly wynik [ FAILED ]"
	przeszlo = True
procent = przeszlo/float(wszystkie)*100
print "Ogolem udalo ci sie " + str(int(przeszlo)) + " / " + str(int(wszystkie)) + " razy(" + str(procent) + "%)"
				
