# Nitika was once reading a history book and wanted to analyze it. So she asked her brother to create a list of names of the various famous personalities in the book. Her brother gave Nitika the list. Nitika was furious when she saw the list. The names of the people were not properly formatted. She doesn't like this and would like to properly format it.

# A name can have at most three parts: first name, middle name and last name. It will have at least one part. The last name is always present. The rules of formatting a name are very simple:

#     Only the first letter of each part of the name should be capital.
#     All the parts of the name except the last part should be represented by only two characters. The first character should be the first letter of the part and should be capitalized. The second character should be ".".

# Let us look at some examples of formatting according to these rules:

#     gandhi -> Gandhi
#     mahatma gandhI -> M. Gandhi
#     Mohndas KaramChand ganDhi -> M. K. Gandhi



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
















