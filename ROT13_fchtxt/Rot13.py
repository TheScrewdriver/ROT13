# -*- coding: utf-8 -*- 
from module import crypting

liste = list()
liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","1","2","3","4","5","6","7","8","9",",","'","-","_",".",":",";","?","\n","(",")","!"]
                                                       
                                                        ##Initialisation de la liste
final = 0                                              ##Initialisation de la liste du cryptage 
final = list()
rank_sentence = 0                         
rank_sentence = list()
n = 0                                                  ##Variable d'incrementation
u = 0
with open("Crypting.txt", "r") as sentence:
     
     sentence = sentence.read()
     print(sentence)                                   
     i = len(sentence)                                          ## Nombre de caracteres dans l'input
     sentence = list(sentence)                                  ##Transformation de l'input en une liste
     print(list(sentence))
     
     crypting(liste,sentence,i,n,rank_sentence,final)           ##Crypte l'input
     
     print(rank_sentence)
     print("Your message has been encrypted :\n\n=","".join(final),"=")            ##Transforme la liste cryptee en chaine de caracteres, puis l'affiche 
     sentence = open("Crypting.txt","w")                                   ##Modifie le fichier texte en le cryptant/decryptant
     sentence = sentence.write("".join(final))                   
