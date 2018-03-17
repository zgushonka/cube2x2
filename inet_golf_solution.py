
import sys

#define permutations for R,U,F
permutation = [[0,7,2,15,4,5,6,21,16,8,3,11,12,13,14,23,17,9,1,19,20,18,22,10],
            [2,0,3,1,6,7,8,9,10,11,4,5,12,13,14,15,16,17,18,19,20,21,22,23],
            [0,1,13,5,4,20,14,6,2,9,10,11,12,21,15,7,3,17,18,19,16,8,22,23]]

def applyMove(state, move):
    return ''.join([state[i] for i in permutation[move]])

scramble = sys.argv[1]
#remove up,front,rigth colors
scramble = ''.join([(' ', x)[x in scramble[12]+scramble[19]+scramble[22]] for x in scramble])
solved = ' '*4+scramble[12]*2+' '*4+scramble[19]*2+scramble[12]*2+' '*4+scramble[19]*2+scramble[22]*4

dict1 = {scramble: ''} #stores states with dist 0,1,2,... from the scramble
dict2 = {solved: ''} #stores states with dist 0,1,2,... from the solved state

moveName = 'RUF'
turnName = " 2'"

for i in range(6):
    tmp = {}
    for state in dict1:
        if state in dict2:
            #solution found
            print dict1[state] + dict2[state]
            exit()
        moveString = dict1[state]
        #do all 9 moves
        for move in range(3):
            for turn in range(3):
                state = applyMove(state, move)
                tmp[state] = moveString + moveName[move] + turnName[turn]
            state = applyMove(state, move)
    dict1 = tmp
    tmp = {}
    for state in dict2:
        if state in dict1:
            #solution found
            print dict1[state] + dict2[state]
            exit()
        moveString = dict2[state]
        #do all 9 moves
        for move in range(3):
            for turn in range(3):
                state = applyMove(state, move)
                tmp[state] = moveName[move] + turnName[2 - turn] + moveString
            state = applyMove(state, move)
    dict2 = tmp


import sys;o=''.join;a=sys.argv[1];d=[{o((' ',x)[x in a[12]+a[19]+a[22]]for x in a):[]},{' '*4+(a[12]*2+' '*4+a[19]*2)*2+a[22]*4:[]}]
for h in[0,1]*6:
 for s,x in d[h].items():
  for y in range(12):
   d[h][s]=x+[y-[1,-1,1,3][h*y%4]];
   if s in d[1-h]:print o('RUF'[x/4]+" 2'"[x%4]for x in d[0][s]+d[1][s][::-1]);exit()
   s=o(s[ord(c)-97]for c in'acahabcdnpbfegefhugiovjgqkciljdeklflmmmnnvoopxphrqdjrrbsstttuuqsviwwwkxx'[y/4::3])

char c[99],t[3][26]={"ZGONFZCPTEZBHUMZ","ZIQPHZRUGAZJWOCZ","ZACB@ZJHFDZKIGEZ"};
r=20;
f(int m,int n){int e,i,j;for(i=4;i--;){for(j=15;j--;)c[t[n][j+1]]=c[t[n][j]];c[m]="FRU"[n],c[m+1]="4'2 "[i],c[m+2]=0;for(e=0,j=68;j<76;j++) e+= (c[j]!=c[j+8]) + (c[j]!=c[j^1]);i&&e&&e<45-m*2&m<r?f(m+2,(n+1)%3),f(m+2,(n+2)%3):e||(puts(c),r=m);}}main(){scanf("%s",c+64);f(0,2),f(0,1),f(0,0);}

