n=int(input())
l=list(map(int,input().split()))
n=0
if l.count(max(l))==1:
  l.remove(max(l))
else:
  for i in range(n):
    if l[i]==max(l):
      n=n+1
      if n==3:
        l.pop(i)
print(*l)
