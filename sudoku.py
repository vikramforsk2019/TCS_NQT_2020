sudoku =[[8, 1, 0, 0, 3, 0, 0, 2, 7], [0, 6, 2, 0, 5, 0, 0, 9, 0],[0, 7, 0, 0, 0, 0, 0, 0, 0], [0, 9, 0, 6, 0, 0, 1, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 4],[0, 0, 8, 0, 0, 5, 0, 7, 0],[0, 0, 0, 0, 0, 0, 0, 8, 0],[0, 2, 0, 0, 1, 0, 7, 5, 0],[3, 8, 0, 0, 7, 0, 0, 4, 2]]
for i in range(len(sudoku)):
	if i==3 or i==6:
		print("---------------------")
	for j in range(len(sudoku)):
		if j==3 or j==6:
			print('|',end=" ")
		print(sudoku[i][j],end=" ")
	print('\n')