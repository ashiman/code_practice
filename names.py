t=input('Enter the no of tet cases')
name=[]
p=[]
c=0
for i in range(t):
    s=raw_input('enter the names')

    name.append(s)

print name
for n in name:
    p=n.split()
    if len(p)==1:
       p[0]= p[0][0].upper()+p[0][1:].lower()
       sub=p[0]
       print sub
    elif len(p)==2:
        p[0]=p[0][0].upper()+'.'
        p[1]=p[1][0].upper()+p[1][1:].lower()
        sub=p[0]+' '+p[1]
        print sub
    else:
        p[0] = p[0][0].upper() + '.'
        p[1] = p[1][0].upper() + '.'
        p[2]=p[2][0].upper()+p[2][1:].lower()
        sub=p[0]+' '+p[1]+' '+p[2]
        print sub
















