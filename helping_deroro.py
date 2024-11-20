T = int(input())
H = int(input())
W = int(input())

rateHeight = (T // H)
rateWidth = (T // W)
flag = 0
for i in range(rateHeight+1) :
    for j in range(rateWidth+1) :
         if i*H + j*W == T :
            flag = 1
           

       
if flag==1:
     print("yes")
else:
    print("no")     
        
