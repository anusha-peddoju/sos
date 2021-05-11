#!/usr/bin/python3
l="abcdefghi"
board={"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i"}
def prin(board):
	print("\n",board["a"] if(board["a"]!="a") else " ",end=" ")
	print("|",board["b"] if(board["b"]!="b") else " ",end=" ")
	print("|",board["c"] if(board["c"]!="c") else " ",end=" ")

	print("\n---+---+---")	
	
	print(board["d"] if(board["d"]!="d") else " ",end=" ")
	print(" |",board["e"] if(board["e"]!="e") else " ",end=" ")
	print("|",board["f"] if(board["f"]!="f") else " ",end=" ")

	print("\n---+---+---")

	print(board["g"] if(board["g"]!="g") else " ",end=" ")
	print(" |",board["h"] if(board["h"]!="h") else " ",end=" ")
	print("|",board["i"] if(board["i"]!="i") else " ",end=" ")

def win(board,cv):

	player1_score=0
	player2_score=0
	if(board["a"]==board["b"]==board["c"] or board["a"]==board["d"]==board["g"] or board["a"]==board["e"]==board["i"] ):
		if(board["a"]=="x"):
			player1_score+=1
		else:
			player2_score+=1
		if(cv==9):
			print("\nthe final board is:")
			prin(board)
			print("\n")
			print(player1,"score = ",player1_score)
			print(player2,"score = ",player2_score)
		



	elif(board["b"]==board["e"]==board["h"] ):
		if(board["b"]=="x"):
			player1_score+=1
		else:
			player2_score+=1
		if(cv==9):
			print("\nthe final board is:")
			prin(board)
			print("\n")
			print(player1,"score = ",player1_score)
			print(player2,"score = ",player2_score)
		


	elif(board["c"]==board["f"]==board["i"] or board["c"]==board["e"]==board["g"]):
		if(board["c"]=="x"):
			player1_score+=1
		else:
			player2_score+=1
		if(cv==9):
			print("\nthe final board is:")
			prin(board)
			print("\n")
			print(player1,"score = ",player1_score)
			print(player2,"score = ",player2_score)
		



	elif(board["d"]==board["e"]==board["f"] ):
		if(board["d"]=="x"):
			player1_score+=1
		else:
			player2_score+=1
		if(cv==9):
			print("\nthe final board is:")
			prin(board)
			print("\n")
			print(player1,"score = ",player1_score)
			print(player2,"score =  ",player2_score)
		



	elif(board["g"]==board["h"]==board["i"] ):
		if(board["g"]=="x"):
			player1_score+=1
		else:
			player2_score+=1
		if(cv==9):
			print("\nthe final board is:\n")
			prin(board)
			print("\n")
			print(player1,"score = ",player1_score)
			print(player2,"score = ",player2_score)
	else:
		if(cv==9 and player1_score==0 and player2_score==0):
			print("no one is the winner")
		

a="x"
cv=0
player1=input("enter player 1 name:")
player2=input("enter player 2 name:")
print("\n a | b | c\n---+---+---\n d | e | f \n---+---+---\n g | h | i ")
print("\n\n\t* * * GAME STARTS * * * ")
prin(board)
while(cv<9):
	print("\nenter the place for \"",a,"\"and enter only character between a-i:")
	b=input()
	if(b in l):
		if(board[b]!="x" and board[b]!="o"):
			board[b]=a
			cv+=1
			if(cv>2):
				rc=win(board,cv)
					
		
	prin(board)
	if(b in l):
		if(a=="x"):
			a="o"
		else:
			a="x"
			













