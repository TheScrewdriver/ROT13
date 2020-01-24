# -*- coding: utf-8 -*-

def crypting(liste,sentence,i,n,rank_sentence,final):
     
     while n < i:                            
          
          half = int(len("".join(liste))/2)                 ##half correspond a la moitie de liste
          sentence[n] = liste.index(sentence[n])+1          ##Attribue a chaque caractere de l'input un rang dans la liste
          rank_sentence.append(sentence[n])           
          
          if sentence[n]+half < (2*half) or sentence[n]+half == (2*half):
               
               final.append(liste[sentence[n]+(half-1)])      ##Ajoute half au rang de l'input
               n+=1
          
          elif sentence[n]+half > (2*half):                   ##Modulo 2half pour que le rang ne soit pas superieur a 2half
               
               sentence[n] = (sentence[n]+half) % (2*half)
               final.append(liste[sentence[n]-1])
               n+=1
     
     print("Your message contain",i,"characters\n")
     
def put(sentence):
        sentence = input("What's your message ?\n")
        return sentence
       