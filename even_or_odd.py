# def even_or_odd():
#     sayi = input()
#     if int(sayi[-1]) % 2 == 0 and int(sayi[0]) % 2 == 0 :
#         print("Even")
#     elif int(sayi[-1]) % 2 == 0 and int(sayi[0]) % 2 != 0 :
#         print("Even Odd")
#     elif int(sayi[-1]) % 2 != 0 and int(sayi[0]) % 2 == 0 :
#         print("Odd Even")
#     else:
#         print("Odd")
# even_or_odd()
    
M, N = len(G), len(G[0])    # dimensions of matrix
max_row_index = 0
max_row_sum = 0

for r in range(M):
    collum_sum = 0
    for c in range(N):
        collum_sum += G[c][r]

    if row_sum > max_row_sum:
        max_row_sum = row_sum
        max_row_index = r

max_row = G[max_row_index]
print(max_row)
        
