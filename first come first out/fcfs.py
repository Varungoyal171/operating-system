# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:54:00 2020

@author: HP
"""
'''
fsfs
avg waittime
avg throghput
avg turnaround time
'''
from tabulate import tabulate
array=[]
arv=[]
burst=[]

j=0
i=int(input("Enter no.s of program: "))

prog=int(input("Want to enter program name manually 1 for yes: "))

while(j<i):
    if(prog==1):
        a=input(" Enter the programs: ")
    else:
        a="P"+str(j)

    array.append(a)
    print("\n Program "+a,end="")
    a=int(input("Enter the arival time : "))
    b=int(input("Enter burst time: "))
    arv.append(a)
    burst.append(b)
    
    j=j+1


    
headers=["Programs","Arival Time","Burst time "]
table=zip(array,arv,burst)
print(tabulate(table,headers,tablefmt="grid"))


begin=[0]
end=[]
wait=[]
turn=[]
a=0
b=0
gantt=[]
for each in range(len(array)):
    
    a=a+burst[each]
    begin.append(a)
    
    b=b+burst[each]
    end.append(b)
    
    wait.append(begin[each]-arv[each])
    
    turn.append(wait[each]+burst[each])
    
    gantt.append(str(begin[each])+" - "+str(end[each]))
    
begin.pop()
    
print("\n Gantt Chart")   
print(tabulate([array,gantt],tablefmt="grid"))
print("\n")
table=zip(array,begin,end,wait,turn)
print(tabulate(table,["Programs","Start","End","Waiting","TurnAround"],tablefmt="grid"))


print("Average Wait time = "+str(round(sum(wait)/len(wait),2)))
print("Average TurnAround time = "+str(round(sum(turn)/len(turn),2)))
print("Average Throughput time = "+str(round(sum(burst)/len(burst),2)))
