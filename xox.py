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

def win(board,gamer):
	player1_score=0
	player2_score=0	
	if(board["a"]==board["b"]==board["c"]):
		if(board["a"]=="x"):
			player2_score+=1	
		else:
			player2_score+=1	
			

	if( board["a"]==board["d"]==board["g"]):
		if(board["a"]=="x"):
			player1_score+=1			
		else:
			player2_score+=1	
		

	if(board["a"]==board["e"]==board["i"] ):
		if(board["a"]=="x"):
			player1_score+=1				
		else:
			player2_score+=1		


	if(board["b"]==board["e"]==board["h"] ):
		if(board["b"]=="x"):
			player1_score+=1			
		else:
			player2_score+=1
	
	if(board["c"]==board["f"]==board["i"]):
		if(board["c"]=="x"):
			player1_score+=1
		else:
			player2_score+=1	

	if(board["c"]==board["e"]==board["g"]):
		if(board["c"]=="x"):
			player1_score+=1	
		else:
			player2_score+=1			
	

	if(board["d"]==board["e"]==board["f"] ):
		if(board["d"]=="x"):
			player1_score+=1			
		else:
			player2_score+=1	

	if(board["g"]==board["h"]==board["i"] ):
		if(board["g"]=="x"):
			player1_score+=1	
		else:
			player2_score+=1	

	if(gamer=="player1"):
		return player1_score
	elif(gamer=="player2"):
		return player2_score	

a="x"
cv=0
value=0
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
			if(a=="x"):
				a="o"
			else:
				a="x"
	
	if(cv==9):
		player1_score=win(board,"player1")
		player2_score=win(board,"player2")
		print(player1,"score = ",player1_score)
		print(player2,"score = ",player2_score)
	if(cv==9 and player1_score==0 and player2_score==0):
		print("no one won the game")
	prin(board)













