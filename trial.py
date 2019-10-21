from openpyxl import load_workbook
wb = load_workbook(filename='moves.xlsx')
ws = wb['Sheet']
arr=[]
moves_arr=[]
# for row in ws.rows:
# 	wm=row[0].value
# 	bm=row[1].value
# 	re=row[2].value
# 	if(wm == "1/2-1/2" or wm == "1-0" or wm == "0-1"):
# 		arr = [wm]
# 		moves_arr.append(arr)
# 		continue
# 	if(type(re) != str):
# 		arr = [wm,bm]
# 		moves_arr.append(arr)
# 		continue
# 	if(type(re) == str):
# 		arr = [wm,bm,re]
# 		moves_arr.append(arr)
# 		continue
# print(moves_arr)

for row in ws.rows:
	wm=row[0].value
	bm=row[1].value
	re=row[2].value
	if(type(re) == str or bm == "1/2-1/2" or bm == "1-0" or bm == "0-1" or wm == "1/2-1/2" or wm == "1-0" or wm == "0-1"):
		if(type(re) == str):
			print(2)
			arr = [wm,bm,re]
			moves_arr.append(arr)
		elif(type(re) != str and (bm == "1/2-1/2" or bm == "1-0" or bm == "0-1")):
			print(3)
			arr = [wm,bm]
			moves_arr.append(arr)
		elif(type(re) != str and (wm == "1/2-1/2" or wm == "1-0" or wm == "0-1")):
			print(4)
			arr = [wm]
			moves_arr.append(arr)
		continue
		#games.append(moves_arr)
		# board(moves_arr)
		# moves_arr = []
		# break
	elif(type(re) != str):
		print(1)
		arr = [wm,bm]
		moves_arr.append(arr)
		continue
print(moves_arr)



# for row in ws.rows:
# 	print(type(row))
# 	print(len(row))
# 	print("White Turn : ")
# 	print(row[0].value)
# 	print(type(row[0].value))
# 	print(len(row[0].value))
# 	print("Black Turn : ")
# 	print(row[1].value)
# 	print(type(row[1].value))
# 	print(len(row[1].value))
# print("Result : ")
# print(row[2].value)
# print(type(row[2].value))
# print(len(row[2].value))

# arr=[]
# game_board = {'a': [1,6,0,0,0,0,-6,-1],'b': [2,6,0,0,0,0,-6,-2],'c': [3,6,0,0,0,0,-6,-3],'d': [4,6,0,0,0,0,-6,-4],'e': [5,6,0,0,0,0,-6,-5],'f': [3,6,0,0,0,0,-6,-3],'g': [2,6,0,0,0,0,-6,-2],'h': [1,6,0,0,0,0,-6,-1]}
# for abc in game_board:
# 	for xyz in game_board[abc]:
# 			arr.append(xyz)
# print (arr)

# move_strength=[]
# import csv
# with open('stockfish.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         move_strength.append(row[1].split())
# print(move_strength)
# csvFile.close()