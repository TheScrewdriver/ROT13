# -*- coding: utf-8 -*-

def crypting(liste,sentence,i,n,rank_sentence,final):

	 while n < i :

		half = int(len("".join(liste))/2)

		##Attribute to every single character of the input a rank in the list

		sentence[n] = liste.index(sentence[n])+1
		rank_sentence.append(sentence[n])

	if sentence[n]+half < (2*half) or sentence[n]+half == (2*half):
 
		##Add half to the rank of the input

		final.append(liste[sentence[n]+(half-1)])     
		n+=1
	
	elif sentence[n]+half > (2*half):

		##Modulo 2half : rank can't be greater than 2half

		sentence[n] = (sentence[n]+half) % (2*half)
		final.append(liste[sentence[n]-1])
		n+=1

	print("Your message contain",i,"characters\n")

def put(sentence):

	sentence = input("What's your message ?\n")
	return sentence
