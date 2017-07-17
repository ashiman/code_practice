# Chef found a strange string yesterday - a string of signs s, where each sign is either a '<', '=' or a '>'. Let N be the length of this string. Chef wants to insert N + 1 positive integers into this sequence and make it valid. A valid sequence is a sequence where every sign is preceded and followed by an integer, and the signs are correct. That is, if a sign '<' is preceded by the integer a and followed by an integer b, then a should be less than b. Likewise for the other two signs as well.

# Chef can take some positive integers in the range [1, P] and use a number in the range as many times as he wants.

# Help Chef find the minimum possible P with which he can create a valid sequence.
# Input

# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

# The only line of each test case contains the string of signs s, where each sign is either '<', '=' or a '>'.
# Output

# For each test case, output a single line containing an integer corresponding to the minimum possible P. 

import re
t=input('Enter the test cases')
st=[]
fudu=0


for i in range(t):
    s=raw_input('enter the string')
    st.append(s)
c=0
z=0
max=0
for signs in st:


    for z in range(len(signs)):


        if signs[z]=='>':
            if signs[z]==signs[z-1]:

                c=c+1
                if max<c:
                    max=c
    max=max+1
    print max






    j=0
    news=''
    for i in range(len(signs)):
        if i==0:

            if signs[i]=='=':

                news=news+'2=2'
                # news[j]='1'
                # j=j+1
                # news[j]='='
                # j = j + 1
                # news[j]='1'
            elif signs[i]=='>':
                news = news + str(max)+'>'+str(max-1)

                # news[j] ='2'
                # j = j + 1
                # news[j] ='>'
                # j = j + 1
                # news[j] ='1'
                # j = j + 1
            else:
                news = news + '2<3'
                # news[j] ='1'
                # j = j + 1
                # news[j] ='<'
                # j = j + 1
                # news[j] ='2'
                # j = j + 1
        else:
            if signs[i]=='=':
                news = news + '='+news[len(news)-1]
                # news[j]='='
                # news[j+1]=news[j-1]
                # j=j+2
            elif signs[i]=='>':
                if int(news[len(news) - 1])<max:
                    temp=max

                else:

                    temp=(int(news[len(news) - 1]) - 1)
                news = news + '>'+str(temp)
                max=max-1
                # news[j]='>'
                # news[j+1]=news[j-1]-1
                # j=j+2
            else:
                temp=(int(news[len(news) - 1]) +1)
                news = news + '<' + str(temp)
                # news[j]='<'
                # news[j+1]=news[j-1]+1
                # j=j+2

    tempo=''
    count=0
    print news
    for i in range(len(news)):
        if news[i].isdigit():
            if news[i] not in tempo:
                tempo=tempo+news[i]
                count=count+1
    print count












