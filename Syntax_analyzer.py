f=open('file','r')
data=f.read()
print(data)
data=data.split()
Operations = ['+', '-', '*', '/','%','<','>','==','!=','<=','>=','=','++','--','&&','||','<<','>>']
Words=['cin','cout','for','while','int','if','else','else if','return','do']
Separators=[' ',';','{','}','[',']','(',')']
Digits=['0','1','2','3','4','5','6','7','8','9']
D={}
a,b,c,d,e=1,1,1,1,1
for i in Operations:
    D[i]="O"+str(a)
    a+=1
for i in Words:
    D[i] = "W" + str(b)
    b += 1
for i in Separators:
    D[i] = "S" + str(c)
    c += 1
for i in Digits:
    D[i] = "D" + str(d)
    d += 1
for i in data:
    if not(i in D):
        D[i]="I"+str(e)
        e+=1
for i in data:
    if ((len(i)>1 and i[0]=='1')
            or (len(i)>1 and i[0]=='2')
            or (len(i)>1 and i[0]=='3')
            or (len(i)>1 and i[0]=='4')
            or (len(i)>1 and i[0]=='5')
            or (len(i)>1 and i[0]=='6')
            or (len(i)>1 and i[0]=='7')
            or (len(i)>1 and i[0]=='8')
            or (len(i)>1 and i[0]=='9')):
        D[i] = "D" + str(d)
        d+=1

for i in data:
    h=len(i)
    if(('.' in i) and (i[0]!='.' and i[h-1]!='.')):
        D[i] = "D" + str(d)
        d += 1
listofdata=[]
for i in data:
    if(i in D):
        listofdata.append(D[i])
print(listofdata)

