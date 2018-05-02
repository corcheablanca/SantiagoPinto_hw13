import numpy as np
from random import shuffle

def sort_doors():
	lista=["goat","goat","car"]
	np.random.shuffle(lista)
	return lista

def choose_door():
	lista2=[0,1,2]

	return (np.random.choice(lista2))



def reveal_door(lista, choice):
	i=0
	t=0
	while(i==0):
		if(t!=choice):
			if(lista[t]=="goat"):
				lista[t]="GOAT_MONTY"
				i=i+1	
		t=t+1	


def finish_game(lista,choice,change):
	if(change==False):
		return (lista[choice])
		
	else:
		for i in range (3):
			if(lista[i]!="GOAT_MONTY" and i!=choice):
				return lista[i]



print (finish_game(sort_doors(),choose_door(),True))





