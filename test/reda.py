# import time
# import sys 




def printBar(total,current):
    width_of_bar = 50
    x = int((current / total)  * width_of_bar)
    printed_string = "".join([('█' if i < x else ' ') for i in range(width_of_bar)])
    
    out = "status : [" + printed_string + "] " + str(int((current / total) * 100)) + "%\r"
    sys.stdout.write(out)
    sys.stdout.flush()
            
# current  = 0

# while current < 100 :
#     time.sleep(0.1)
#     current += 1
#     printBar(100,current)

# print('\n')
# print('download Finished')



# def status_bar(total,downloaded):
#     finished_percentage = (downloaded*100)/total
#     finished = finished_percentage // 3
#     blocks = ''
#     spaces = '                              '
#     for a in range(int(finished)) :
#         blocks += '█'
#         spaces = ''
#         for b in range(30-a):
#             spaces += ' '
#     bar = blocks + spaces
#     out = "status : ["+str(bar)+"]"+" "+str(int(finished_percentage))+"%\r"
#     sys.stdout.write(out)
#     sys.stdout.flush()


n = input()
while len(n) > 1:
    n = str(sum([int(i) for i in n]))
print(n)


a = str(float(input().replace(',','.'))).replace('.',',')
b = str(float(input().replace(',','.'))).replace('.',',')
al,ar = a.split(",")
bl,br = b.split(",")
print( "".join(" " for i in range(max(len(al),len(bl)) - len(al))) + al + "," + ar + "".join("0" for i in range(max(len(ar),len(br)) - len(ar))))
print( "".join(" " for i in range(max(len(al),len(bl)) - len(bl))) + bl + "," + br + "".join("0" for i in range(max(len(ar),len(br)) - len(br))))
