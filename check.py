all_moves=[]
game_board = {'a': [1,6,0,0,0,0,-6,-1],'b': [2,6,0,0,0,0,-6,-2],'c': [0,-6,0,0,0,0,-6,-3],'d': [4,6,0,0,0,0,-6,-4],'e': [5,6,0,0,0,0,-6,-5],'f': [3,6,0,0,0,0,-6,-3],'g': [2,6,0,0,0,0,-6,-2],'h': [1,6,0,0,0,0,-6,-1]}
all_moves.append(game_board)
a = ['c','1','=','R']
j=1
for element in all_moves:
	for key in element :
		if(key==a[0]):
			for k in range (0,8):
				if(element[key][k]==6 and j==0 and int(a[1])==k+2 and k==6 and element[key][int(a[1])-1]==0):
					element[key][k]=0
					if (a[3]=='Q'):
						element[key][(int(a[1])-1)]=4
					if (a[3]=='B'):
						element[key][(int(a[1])-1)]=3
					if (a[3]=='N'):
						element[key][(int(a[1])-1)]=2
					if (a[3]=='R'):
						element[key][(int(a[1])-1)]=1
					print(element)
				if(element[key][k]==-6 and j==1 and int(a[1])==k and k==1 and element[key][int(a[1])-1]==0):
					element[key][k]=0
					if (a[3]=='Q'):
						element[key][(int(a[1])-1)]=-4
					if (a[3]=='B'):
						element[key][(int(a[1])-1)]=-3
					if (a[3]=='N'):
						element[key][(int(a[1])-1)]=-2
					if (a[3]=='R'):
						element[key][(int(a[1])-1)]=-1
					print(element)
# te=0
# for element in all_moves:
# 	for key in element :
# 		if(key==a[2]):
# 			for k in range (0,8):
# 				if((k+1)==int(a[3]) and j==0 and element[key][k]!=0):
# 					te=1
# 					element[key][k]=6
# 				if((k+1)==int(a[3]) and j==1 and element[key][k]!=0):
# 					te=1
# 					element[key][k]=-6
# for element in all_moves:
# 	for key in element :
# 		if(key==a[0]):
# 			for k in range (0,8):
# 				if(element[key][k]==6 and j==0 and int(a[3]) == k+2 and te==1):
# 					element[key][k]=0
# 					print(element)
# 				if(element[key][k]==-6 and j==1 and int(a[3]) == k and te==1):
# 					element[key][k]=0
# 					print(element)
# # if(element[key][k]==6 and j==0 and (int(a[1])==k+2 or ((int(a[1])==k+3) and (k==1) and (element[key][int(a[1])-2]==0)))):
# 	element[key][k]=0
# 	element[key][(int(a[1])-1)]=6
# 	print(element)
# if(element[key][k]==-6 and j==1 and (int(a[1])==k or ((int(a[1])==k-1) and (k==6) and (element[key][(int(a[1])-1)]!=-6)))):
# 	element[key][k]=0
# 	element[key][(int(a[1])-1)]=-6
# 	print(element)