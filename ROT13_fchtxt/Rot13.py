# -*- coding: utf-8 -*-
from module import crypting

##Initialize list_c

list_c = list()
list_c = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","1","2","3","4","5","6","7","8","9",",","'","-","_",".",":",";","?","\n","(",")","!"]

##Initialize the crypting list

final = 0
final = list()
rank_sentence = 0                         
rank_sentence = list()

##Incrementation variable

n = 0
u = 0

with open("Crypting.txt", "r") as sentence:

	sentence = sentence.read()
	print(sentence)

	##Numbers of characters in the input
          
	i = len(sentence)

	##Turn input into list

	sentence = list(sentence)
	print(list(sentence))

	##Crypt input

	crypting(list_c,sentence,i,n,rank_sentence,final)

	print(rank_sentence)

	##Turn the encrypted list into string characters

	print("Your message has been encrypted :\n\n=","".join(final),"=")

	##Write in file_text with crypting/uncrypting

	sentence = open("Crypting.txt","w")
	sentence = sentence.write("".join(final))
