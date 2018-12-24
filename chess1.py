# import pgn
# import sys

# f = open(sys.argv[1])
# pgn_text = f.read()
# f.close()
# games = pgn.loads(pgn_text)
# for game in games:
#     print (game.moves)
import pgn
import re
import json
from openpyxl import Workbook
wb = Workbook()
ws = wb.active


moves_arr = []
temp_arr = []
arr = []
moves = []
ct=0

def Remove(duplicate,dup):
    final_list = []
    for num in duplicate:
        if num != dup:
            final_list.append(num)
    return final_list

ws.append(['White_Moves', 'Black_Moves', 'Result'])
pgn_text = open('data.pgn').read()
s = pgn_text
s=re.sub(r'\[(.*?)\]', '', s)
s=s.replace('[]','')
s=s.replace('\n', " ")
temp_arr = s.split('.')
for word in temp_arr:
	arr=word.split(' ')
	arr=Remove(arr,'')
	arr=Remove(arr,arr[(len(arr)-1)])
	if (len(arr)>=3 or len(arr)<=1):
		ct=ct+1
print (ct)

#	if(arr != []):
#		moves_arr.append(arr)


#for element in moves_arr:
	#print(len(element))
	#print(element[0])
	#print(element[1])
	#if(len(element)==2):
	#	ws.append([element[0],element[1]])
	#if(len(element)==3):
	#	ws.append([element[0],element[1],element[2]])
#wb.save("chess_moves.xlsx")


#print(moves_arr)
#print(ct)
# i=0
# for arr in temp_arr:
# 	arr1=list(arr)
# 	temp1=json.dumps(arr1)
# 	temp2 = temp1.replace(' ', '')
# 	temp3=''.join(temp2)
# 	print(temp3)
# 	arr=Remove(arr1,' ')
# 	moves.append(arr1)
# 	i=i+1
# 	if i==2:
# 		break
# print(moves)
#for arr in temp_arr:
#	if len(arr)!=4 and len(arr)!=13:
#		ct=ct+1
#print(ct)
#print(s)