#!/usr/bin/python3
l=[]
board={}
val=0
while(val<1):						#allowing only integers using exception handiling 
	try:
		row=int(input("enter how many rows you want to choose for playing game:"))
		col=int(input("enter how many columns you want to choose for playing game:"))
		val+=1
		
	except ValueError:						
		print("\n\t\t\033[1;33m ENTER ONLY INTEGERS \033[0m\n")	


if((row!=1 and col!=1) and ((row<3 and col>=3 ) or (col<3 and row>=3)) or (row>=3 and col>=3)):	
	print("\t\t\t\t\033[1;31;43m  GAME RULES ARE    \033[0m")
	print("\t\t----------------------------------------")
	print("\033[1;33;1m 1.player can able to enter S OR O according to their wish based on input of rows and columns")
	print("\033[1;33;1m 2.players can play game on any board based on their input of rows and columns")
	print("\033[1;33;1m 3.player has chance to play another time when player get point")
	print("\033[0m")	
	print("\t\t------------------------------------------\n")
	i=0
	j=0
	while(i<row):
		while(j<col):
			l=l+["%d%d"%(i,j)]
			board["%d%d"%(i,j)]="%d%d"%(i,j)
			j=j+1
		j=0
		i=i+1
	def prin(board):					#function
		i=0
		j=0
		k=0
		while(i<row):
			while(j<col):
				print("|",board["%d%d"%( i,j)] if(board["%d%d"%(i,j)]!="%d%d"%(i,j)) else " ",end=" ") 					
				j=j+1
			print("|")
			while(k<col):
				if(i!=row-1):
					print("+---",end="")
				k=k+1
				if(k==col and i<row-1):
					print("+")
			k=0
			j=0
			i=i+1

	a=" "
	b=" "
	cv=0
	v=0
	list1=[" "]
	list2=[" ."]
	doop=[ ]
	player1=input("enter player 1 name:")
	player2=input("enter player 2 name:")
	player1_score=0
	player2_score=0
	i=0
	j=0
	k=0
	k1=0
	k2=0
	k3=0
	k4=0
	k5=0
	check=0
	check1=0
	check2=0
	count=0
	while(i<row):
		while(j<col):
			print("|",i,j,end=" ")
			j=j+1
		print("|")
		while(k<col):
			if(i!=row-1):
				print("+-----",end="")
			k=k+1
			if(k==col and i<row-1):
				print("+")
		k=0
		j=0
		i=i+1
	i=0
	j=0
	print("\n\n\t* * * GAME STARTS * * * ")
	prin(board)
	while(cv<(row*col)):
		cv=v
		if(cv%2==0):												#for knowing whether it is player1 or player2 based on cv. cv values are  even for player2 and odd for player1 										
			print("\n",player1,"enter S or O :")									
			a=input()
		else:
			print("\n",player2,"enter S or O :")
			a=input()
		if(a=="s" or a=="o" or a=="S" or a=="O"):
			print("enter a place to insert S or O which are shown on board:")
			b=input()
			if(b in l):
				if(board[b]!="s" and board[b]!="o" and board[b]!="S" and board[b]!="O"):
					board[b]=a						
					cv+=1
					prin(board)														#function call
					print("\n")
				else:
					print("\033[1;33m ENTERED BLOCK IS ALREADY FILLED TRY TO ENTER NEW ONE \033[0m")
					check=1
			else:
				print("\033[1;33m PLEASE ENTER CORRECT BLOCK\033[0m")
				check1=1
		else:
			print("\033[1;33m PLEASE ENTER CORRECT INPUT \033[0m")
			check2=1
		v=cv
		while(i<row):
			while(j<col):
				if("%d%d"%(i,j)==b):
					k1=i
					k2=j
				j=j+1
			j=0
			i=i+1
		i=k1
		j=k2
		if(cv>2 and check==0 and check1==0 and check2==0):
			if(j+2<col and j-2>=0):							#for finding whether horizontal sos is occured or not 
				print(cv)
				if(((board["%d%d"%(i,j)]=="s") or(board["%d%d"%(i,j)]==" S")) and ((board["%d%d"%(i,j+1)]=="o")  or (board["%d%d"%(i,j+1)]=="O")) and ((board["%d%d"%(i,j+2)]=="s") or (board["%d%d"%(i,j+2)]=="S"))):
					print(cv)
					if(cv%2==0):
						list2.append(["%d%d"%(i,j),"%d%d"%(i,j+1),"%d%d"%(i,j+2)])		#appending that blocks
						print("1")												#to know the curser movement
						k3=1
					else:
						list1.append(["%d%d"%(i,j),"%d%d"%(i,j+1),"%d%d"%(i,j+2)])
						print("2")
						k3=1	
				elif(((board["%d%d"%(i,j-1)]=="s") or(board["%d%d"%(i,j-1)]=="S")) and ((board["%d%d"%(i,j)]=="o") or (board["%d%d"%(i,j)]=="O")) and ((board["%d%d"%(i,j+1)]=="s") or (board["%d%d"%(i,j-2)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(i,j-1),"%d%d"%(i,j),"%d%d"%(i,j+1)])
						print("3")
						k3=1
					else:
						list1.append(["%d%d"%(i,j-1),"%d%d"%(i,j),"%d%d"%(i,j+1)])
						print("4")
						k3=1
				elif(((board["%d%d"%(i,j-2)]=="s") or (board["%d%d"%(i,j-2)]=="S")) and ((board["%d%d"%(i,j-1)]=="o") or (board["%d%d"%(i,j-1)]=="O")) and ((board["%d%d"%(i,j)]=="s") or (board["%d%d"%(i,j)]=="S"))):			
					if(cv%2==0):
						list2.append(["%d%d"%(i,j-2),"%d%d"%(i,j-1),"%d%d"%(i,j)])
						print("5")
						k3=1
					else:
						list1.append(["%d%d"%(i,j-2),"%d%d"%(i,j-1),"%d%d"%(i,j)])
						print("6")
						k3=1

				m=0
				n=0
				if(k3==1):			#for checking whether  above condition is true or not. when we not given this the player score is increased although the conditions are satisfied 
					if(cv%2==0):
						while(m<len(list2)):			#for knowing whether the elements are in doop or not. 
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):					#increasing player_score when  it hits the SOS in new boxex.that means it does not allows to increse player_score when already player has hit the SOS in that boxex 
							player2_score+=1
							doop=doop+list2				#doop contains all the blocks which are filled.
							print("7")
							if(cv<row*col and v==cv): 				#v==cv is given to reducing of execution of printf statement multiple times.that means if player got two marks for one input then this print statement does not execute two times.
								print(player2,"you got point so you have another chance to play")
							v=cv-1							#for controlling cv when player get a point
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("8")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0

			if(((j==0) or (j==1) or (j==col-1) or (j==col-2)) and (col>=3)):    #horizontal sos for the values which are present at horizontal boudaries
				if(((board["%d%d"%(i,0)]=="s") or (board["%d%d"%(i,0)]=="S")) and ((board["%d%d"%(i,1)]=="o") or (board["%d%d"%(i,1)]=="O")) and ((board["%d%d"%(i,2)]=="s") or (board["%d%d"%(i,2)]=="S"))):															#checking conditions for horizontal sos accessing
					if(cv%2==0):
						list2.append(["%d%d"%(i,0),"%d%d"%(i,1),"%d%d"%(i,2)])
						k3=1
						print("9")
					else:
						list1.append(["%d%d"%(i,0),"%d%d"%(i,1),"%d%d"%(i,2)])
						k3=1
						print("10")
				if(row>3 and col>3):
					if(((board["%d%d"%(i,1)]=="s") or (board["%d%d"%(i,1)]=="S")) and ((board["%d%d"%(i,2)]=="o") or (board["%d%d"%(i,2)]=="O")) and ((board["%d%d"%(i,3)]=="s") or (board["%d%d"%(i,3)]=="S"))):
						if(cv%2==0):
							list2.append(["%d%d"%(i,1),"%d%d"%(i,2),"%d%d"%(i,3)])
							k3=1
							print("11")
						else:
							list1.append(["%d%d"%(i,1),"%d%d"%(i,2),"%d%d"%(i,3)])
							k3=1
							print("12")

				if(((board["%d%d"%(i,col-3)]=="s") or (board["%d%d"%(i,col-3)]=="S")) and ((board["%d%d"%(i,col-2)]=="o") or (board["%d%d"%(i,col-2)]=="o")) and ((board["%d%d"%(i,col-1)]=="s") or (board["%d%d"%(i,col-1)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(i,col-3),"%d%d"%(i,col-2),"%d%d"%(i,col-1)])
						k3=1
						print("13")
					else:
						list1.append(["%d%d"%(i,col-3),"%d%d"%(i,col-2),"%d%d"%(i,col-1)])
						k3=1
						print("14")
				m=0					
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):	
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):	
							player2_score+=1
							doop=doop+list2
							print("15")
							print
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("16")	
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0



			if(i+2<row and i-2>=0):  						#for finding whether vertical sos is occured or not 
				if(((board["%d%d"%(i,j)]=="s") or(board["%d%d"%(i,j)]=="S")) and ((board["%d%d"%(i+1,j)]=="o")  or (board["%d%d"%(i+1,j)]=="O")) and ((board["%d%d"%(i+2,j)]=="s") or (board["%d%d"%(i+2,j)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(i,j),"%d%d"%(i+1,j),"%d%d"%(i+2,j)])
						print("17")
						k3=1
					else:
						list1.append(["%d%d"%(i,j),"%d%d"%(i+1,j),"%d%d"%(i+2,j)])
						print("18")
						k3=1
				elif(((board["%d%d"%(i-1,j)]=="s") or(board["%d%d"%(i-1,j)]=="S")) and ((board["%d%d"%(i,j)]=="o") or (board["%d%d"%(i,j)]=="O")) and ((board["%d%d"%(i+1,j)]=="s") or (board["%d%d"%(i+1,j)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(i-1,j),"%d%d"%(i,j),"%d%d"%(i+1,j)])
						print("19")
						print(i,j)
						k3=1
					else:
						list1.append(["%d%d"%(i-1,j),"%d%d"%(i,j),"%d%d"%(i+1,j)])
						print("20")
						k3=1
				elif(((board["%d%d"%(i-2,j)]=="s") or (board["%d%d"%(i-2,j)]=="S")) and ((board["%d%d"%(i-1,j)]=="o") or (board["%d%d"%(i-1,j)]=="O")) and ((board["%d%d"%(i,j)]=="s") or (board["%d%d"%(i,j)]=="S"))):			
					if(cv%2==0):
						list2.append(["%d%d"%(i-2,j),"%d%d"%(i-1,j),"%d%d"%(i,j)])
						print("21")
						k3=1
					else:
						list1.append(["%d%d"%(i-2,j),"%d%d"%(i-1,j),"%d%d"%(i,j)])
						print("22")
						k3=1

				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("23")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("24")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0


			if(((i==0) or (i==1) or (i==row-1) or (i==row-2)) and (row>=3)):   #vertical sos for the values which are present at vertical boudaries
				if(((board["%d%d"%(0,j)]=="s") or (board["%d%d"%(0,j)]=="S")) and ((board["%d%d"%(1,j)]=="o") or (board["%d%d"%(1,j)]=="O")) and ((board["%d%d"%(2,j)]=="s") or (board["%d%d"%(2,j)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(0,j),"%d%d"%(1,j),"%d%d"%(2,j)])
						k3=1
						print("25")
					else:
						list1.append(["%d%d"%(0,j),"%d%d"%(1,j),"%d%d"%(2,j)])
						k3=1
						print("26")

				if(row>3 and col>3):
					if(((board["%d%d"%(1,j)]=="s") or (board["%d%d"%(1,j)]=="S")) and ((board["%d%d"%(2,j)]=="o") or (board["%d%d"%(2,j)]=="O")) and ((board["%d%d"%(3,j)]=="s") or (board["%d%d"%(3,j)]=="S"))):
						if(cv%2==0):
							list2.append(["%d%d"%(1,j),"%d%d"%(2,j),"%d%d"%(3,j)])
							k3=1
							print("27")
						else:
							list1.append(["%d%d"%(1,j),"%d%d"%(2,j),"%d%d"%(3,j)])
							k3=1
							print("28")

				if(((board["%d%d"%(row-3,j)]=="s") or (board["%d%d"%(row-3,j)]=="S")) and ((board["%d%d"%(row-2,j)]=="o") or (board["%d%d"%(row-2,j)]=="o")) and ((board["%d%d"%(row-1,j)]=="s") or (board["%d%d"%(row-1,j)]=="S"))):
					if(cv%2==0):
						list2.append(["%d%d"%(row-3,j),"%d%d"%(row-2,j),"%d%d"%(row-1,j)])
						k3=1
						print("29")
					else:
						list1.append(["%d%d"%(row-3,j),"%d%d"%(row-2,j),"%d%d"%(row-1,j)])
						k3=1
						print("30")
				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("31")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("32")	
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0


			if(row>3 or col>3):														#for accessing crossed elements(right to left)
				if(i!=row-2 and i!=row-1 and j!=0 and j!=1):
					if(((board["%d%d"%(i,j)]=="s") or(board["%d%d"%(i,j)]=="S")) and ((board["%d%d"%(i+1,j-1)]=="o")  or (board["%d%d"%(i+1,j-1)]=="O")) and ((board["%d%d"%(i+2,j-2)]=="s") or (board["%d%d"%(i+2,j-2)]=="S")) and i!=5 and i!=6 and j!=0 and j!=1):
						if(cv%2==0):
							list2.append(["%d%d"%(i,j),"%d%d"%(i+1,j-1),"%d%d"%(i+2,j-2)])
							print("33")
							k3=1
						else:
							list1.append(["%d%d"%(i,j),"%d%d"%(i+1,j-1),"%d%d"%(i+2,j-2)])
							print("34")
							k3=1
				if(i!=0 and i!=row-1 and j!=0 and j!=col-1):
					if(((board["%d%d"%(i-1,j+1)]=="s") or(board["%d%d"%(i-1,j+1)]=="S")) and ((board["%d%d"%(i,j)]=="o") or (board["%d%d"%(i,j)]=="O")) and ((board["%d%d"%(i+1,j-1)]=="s") or (board["%d%d"%(i+1,j-1)]=="S"))):
						if(cv%2==0):
							list2.append(["%d%d"%(i-1,j+1),"%d%d"%(i,j),"%d%d"%(i+1,j-1)])
							print("35")
							print(i,j)
							k3=1
						else:
							list1.append(["%d%d"%(i-1,j+1),"%d%d"%(i,j),"%d%d"%(i+1,j-1)])
							print("36")
							k3=1
				if(i!=0 and i!=1 and j!=col-2 and j!=col-1):
					if(((board["%d%d"%(i-2,j+2)]=="s") or (board["%d%d"%(i-2,j+2)]=="S")) and ((board["%d%d"%(i-1,j+1)]=="o") or (board["%d%d"%(i-1,j+1)]=="O")) and ((board["%d%d"%(i,j)]=="s") or (board["%d%d"%(i,j)]=="S"))):			
						if(cv%2==0):
							list2.append(["%d%d"%(i-2,j+2),"%d%d"%(i-1,j+1),"%d%d"%(i,j)])
							print("37")
							k3=1
						else:
							list1.append(["%d%d"%(i-2,j+2),"%d%d"%(i-1,j+1),"%d%d"%(i,j)])
							print("38")
							k3=1

				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("39")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("40")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0
 			   														


			if(row>3 or col>3): 													#for accessing crossed elements(left to right)
				if(i!=row-2 and i!=row-1 and j!=col-2 and j!=col-1):		
					if(((board["%d%d"%(i,j)]=="s") or(board["%d%d"%(i,j)]=="S")) and ((board["%d%d"%(i+1,j+1)]=="o")  or (board["%d%d"%(i+1,j+1)]=="O")) and ((board["%d%d"%(i+2,j+2)]=="s") or (board["%d%d"%(i+2,j+2)]=="S"))):
						if(cv%2==0):
							list2.append(["%d%d"%(i,j),"%d%d"%(i+1,j+1),"%d%d"%(i+2,j+2)])
							print("41")
							k3=1
						else:
							list1.append(["%d%d"%(i,j),"%d%d"%(i+1,j+1),"%d%d"%(i+2,j+2)])
							print("42")
							k3=1
				if(i!=0 and i!=row-1 and j!=0 and j!=col-1):
					if(((board["%d%d"%(i-1,j-1)]=="s") or(board["%d%d"%(i-1,j-1)]=="S")) and ((board["%d%d"%(i,j)]=="o") or (board["%d%d"%(i,j)]=="O")) and ((board["%d%d"%(i+1,j+1)]=="s") or (board["%d%d"%(i+1,j+1)]=="S"))):
						if(cv%2==0):
							list2.append(["%d%d"%(i-1,j-1),"%d%d"%(i,j),"%d%d"%(i+1,j+1)])
							print("43")
							print(i,j)
							k3=1
						else:
							list1.append(["%d%d"%(i-1,j-1),"%d%d"%(i,j),"%d%d"%(i+1,j+1)])
							print("44")
							k3=1
				if(i!=0 and i!=1 and j!=0 and j!=1):
					if(((board["%d%d"%(i-2,j-2)]=="s") or (board["%d%d"%(i-2,j-2)]=="S")) and ((board["%d%d"%(i-1,j-1)]=="o") or (board["%d%d"%(i-1,j-1)]=="O")) and ((board["%d%d"%(i,j)]=="s") or (board["%d%d"%(i,j)]=="S"))):			
						if(cv%2==0):
							list2.append(["%d%d"%(i-2,j-2),"%d%d"%(i-1,j-1),"%d%d"%(i,j)])
							print("45")
							k3=1
						else:
							list1.append(["%d%d"%(i-2,j-2),"%d%d"%(i-1,j-1),"%d%d"%(i,j)])
							print("46")
							k3=1

				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("47")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("48")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0

			if(row==3 and col==3):												#for accessing crossed(left-right) elements in 3*3 matrix
				if(((board["00"]=="s") or(board["00"]=="S")) and ((board["11"]=="o")  or (board["11"]=="O")) and ((board["22"]=="s") or (board["22"]=="S"))):
					if(cv%2==0):
						list2.append(["00","11","22"])
						print("49")
						k3=1
					else:
						list1.append(["00","11","22"])
						print("50")
						k3=1

				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("51")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("52")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0

			if(row==3 and col==3):										#for accessing crossed(right-left) elements in 3*3 matrix
				if(((board["02"]=="s") or(board["02"]=="S")) and ((board["11"]=="o")  or (board["11"]=="O")) and ((board["20"]=="s") or (board["20"]=="S"))):
					if(cv%2==0):
						list2.append(["02","11","20"])
						print("53")
						k3=1
					else:
						list1.append(["02","11","20"])
						print("54")
						k3=1

				m=0
				n=0
				if(k3==1):
					if(cv%2==0):
						while(m<len(list2)):
							if(list2[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player2_score+=1
							doop=doop+list2	
							print("55")
							if(cv<row*col and v==cv):
								print(player2,"you got point so you have another chance to play")
							v=cv-1	
						list2=[]
					else:
						while(m<len(list1)):
							if(list1[m] in doop):
								n=1
							m=m+1
						if(n==0):
							player1_score+=1
							doop=doop+list1	
							print("56")
							if(cv<row*col and v==cv):
								print(player1,"you got point so you have another chance to play")
							v=cv-1	
						list1=[]
					k3=0


			while(k4<row):				#for knowing whether total boxex are filled or not
				while(k5<col):
					if(board["%d%d"%(k4,k5)]=="s"  or board["%d%d"%(k4,k5)]=="S" or board["%d%d"%(k4,k5)]=="o" or board["%d%d"%(k4,k5)]=="O"):
						count=count+1
					k5=k5+1
				if(count==(row*col)):			
					print("\n\t*** GAME IS OVER ***\n")
					print("\033[1;31m the final scores of two players are:\n")
					print("\033[1;36m ",player1,"score = ",player1_score)		
					print("\033[1;36m ",player2,"score = ",player2_score)
					cv=(row*col)
				k5=0
				k4=k4+1
			if(cv<(row*col)):
				print(player1,"score = ",player1_score)			#printing scores of players
				print(player2,"score = ",player2_score)
			if(cv==(row*col)):							#giving comment to their scores
				if(player1_score>player2_score):
					print("\033[1;36m 😃️",player1,"is the winner😃️🎉️🎉️")
					print("congratulations to u",player1,"👏️✌️👏️")
				elif(player2_score>player1_score):
					print("😃️",player2,"is the winner😃️🎉️🎉️")
					print("congratulations to u ",player2,"👏️✌️👏️")
				elif(player1_score==0 and player2_score==0):
					print("no one won the game😟️☹️")		
				elif(player1_score==player2_score):
					print(player1,player2,"scores are equal😁️😁️")			
				
		i=0					#these variables are incresed in above programming.but it is important to intialize with 0.so here for that we do like this
		j=0
		count=0
		k4=0
		k5=0
		check=0
		check1=0
		check2=0
		
else:
	if(row==1 and col==1):
		print("\n\033[0;33m SOS GAME IS NOT POSSIBLE WITH",   row  ,"ROW AND",   col   ,"COLUMN😟️😞️😟️\n")
	elif(row==1 and col!=1):
		print("\n\033[0;33m SOS GAME IS NOT POSSIBLE WITH",   row  ,"ROW AND",   col   ,"COLUMNS😟️😞️😟️\n")
	elif(row!=1 and col==1):
		print("\n\033[0;33m SOS GAME IS NOT POSSIBLE WITH",   row  ,"ROWS AND",   col   ,"COLUMN😟️😞️😟️\n")
	else:
		print("\n\033[0;33m SOS GAME IS NOT POSSIBLE WITH",   row  ,"ROWS AND",   col   ,"COLUMNS😟️😞️😟️\n")




















