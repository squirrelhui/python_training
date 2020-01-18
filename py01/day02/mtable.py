# 1*1=1
# 2*1=2 2*2=4
# 3*1=3 3*2=6 3*3=9
# alist = []

# for i in range(1, 10):
#     for k in range(1, i+1):
#         print('%d*%d=%d' % (i, k, i*k) , end = ' ')
#     print()

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, i*j) , end = ' ')
        j += 1
    print("")
    i += 1