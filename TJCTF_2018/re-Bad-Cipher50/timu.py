message = "123456789"
key = "abc"

r,o,u,x,h=range,ord,chr,"".join,hex
def e(m,k):
 l=len(k);s=[m[i::l]for i in r(l)]
 for i in r(l):
  a,e=0,""
  for c in s[i]:
   a=o(c)^o(k[i])^(a>>2)
   e+=u(a)
  s[i]=e
 print s
 return x(h((1<<8)+o(f))[3:]for f in x(x(y)for y in zip(*s)))

print(e(message,key))
