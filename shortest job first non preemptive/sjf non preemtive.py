# -*- coding: utf-8 -*-
'''
Varun Goel
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
    a=float(input("Enter the arrival time : "))
    b=float(input("Enter burst time: "))
    arv.append(a)
    burst.append(b)
    
    j=j+1

prog=array.copy()
arrival=arv.copy()
comp=burst.copy()  #for latter use
   
headers=["Programs","Arival Time","Burst time "]
table=zip(array,arv,burst)
print(tabulate(table,headers,tablefmt="grid"))


chartp=[] #program schedules
charts=[] #starting time of program
charte=[] #ending time of programs

time=sum(burst)
each=0

while(each<time):
    program=[]
    clock=[]
    end=[]
    for every in range(i):
        if(arv[every]<=each):
            program.append(array[every])
            clock.append(arv[every])
            end.append(burst[every])
    
    if(len(end)>0):
        z=end.index(min(end))
        chartp.append(program[z])
        charts.append(each)
        charte.append(each+end[z])
        each=each+end[z]-1
        
        i=i-1
        
        array.remove(program[z])
        arv.remove(clock[z])
        burst.remove(end[z])    
        
    each=each+1

wait=[]
gantt=[]
turn=[]
for each in range(len(chartp)):
    gantt.append(str(charts[each])+" - "+str(charte[each]))
    wait.append(charts[each]-arrival[prog.index(chartp[each])])
    turn.append(wait[each]+comp[prog.index(chartp[each])])
    
print("\n Gantt Chart")   
print(tabulate([chartp,gantt],tablefmt="grid"))
print("\n")


table=zip(chartp,charts,charte,wait,turn)
print(tabulate(table,["Programs","Start","Arrival","Completion time","Waiting","TurnAround"],tablefmt="grid"))


print("Average Wait time = "+str(round(sum(wait)/len(wait),2)))
print("Average TurnAround time = "+str(round(sum(turn)/len(turn),2)))
print("Average Throughput time = "+str(round(sum(comp)/len(comp),2)))
