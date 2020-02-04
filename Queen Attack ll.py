n , k = list(map(int,input().split()))
a , b = list(map(int,input().split()))
lis = []
for i in range(k):
    lis.append(list(map(int,input().split())))


t = abs( a - n)
bot = abs(a-1)
l = abs(b-1)
right = abs(b-n)

b_r = min(bot,right)
t_l = min(t,l)
b_l = min(bot,l)
t_r = min (t,right)
r = a+1
c = b-1

count_t_l = []
count_t_r = []
count_b_l = []
count_b_r = []
count_t = []
count_b = []
count_r = []
count_l = []
r =  a+1
for i in range(t):
    if [r,b] in lis:
        break
    count_t.append([r,b])
    r = r+1
    
r = a-1
for i in range(bot):
    if [r,b] in lis:
        break
    count_b.append([r,b])
    r  = r-1
r = b-1
for i in range(l):
    if [a,r] in lis:
        break
    count_l.append([a,r])
    r = r-1
r = b+1
for i in range(right):
    if [a,r] in lis:
        break
    count_r.append([a,r])
    r = r-1
    
    
    
    
    
    
r =  a+1
c = b-1
for i in range(t_l):
    if [r,c] in lis:
        break
    count_t_l.append([r,c])
    r = r+1
    c = c-1
r = a-1
c = b+1
for i in range(b_r):
    if [r,c] in lis:
        break
    count_b_r.append([r,c])
    r = r-1
    c  = c+1
r = a-1
c = b-1
for i in range(b_l):
    if [r,c] in lis:
        break
    count_b_l.append([r,c])
    r -= 1
    c -= 1
r = a+1
c = b+1
for i in range(t_r):
    if [r,c] in lis:
        break
    count_t_r.append([r,c])
    r += 1
    c += 1
print(sum([len(count_t_l),len(count_t_r),len(count_b_r),len(count_b_l),len(count_t),len(count_b),len(count_r),len(count_l)]))
