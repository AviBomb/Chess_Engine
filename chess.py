import pgn
import re
import json
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
temp_arr = []
arr = []

def Remove(duplicate,dup):
    final_list = []
    for num in duplicate:
        if num != dup:
            final_list.append(num)
    return final_list

def hello(temp_arr):
	for word in temp_arr:
		arr=word.split(' ')
		arr=Remove(arr,'')
		arr=Remove(arr,arr[(len(arr)-1)])
		if(arr != []):
			if(len(arr)==2):
				ws.append([arr[0],arr[1]])
			if(len(arr)==3):
				ws.append([arr[0],arr[1],arr[2]])

pgn_text = open('data.pgn').read()
s = pgn_text
s=re.sub(r'\[(.*?)\]', '', s)
s=s.replace('[]','')
s=s.replace('\n', " ")
temp_arr = s.split('.')
hello(temp_arr[1500000:2000000])
wb.save("chess_moves6.xlsx")