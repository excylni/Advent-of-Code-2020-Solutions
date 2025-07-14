with open('Boarding Passes.txt','r') as file:
    combinations = file.read()
    combinations = combinations.split()

rows = 128
columns = 8


def encoder(boarding_pass):
    row_start, row_end = 0, rows - 1
    col_start, col_end = 0, columns - 1
    for letter in boarding_pass[:7]:
        mid = (row_start + row_end)//2
        if letter == 'F':
            row_end = mid 
        else:
            row_start = mid + 1
                
    for letter in boarding_pass[7:]:
        mid = (col_start + col_end)//2 
        if letter == 'L':
            col_end = mid
        else:
            col_start = mid +1


    row = row_start
    column = col_start
    Board_ID =  row * 8 + column
   
    return Board_ID