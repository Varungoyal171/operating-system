# -*- coding: utf-8 -*-
'''
Varun Goel
RR
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
quantum=float(input("Enter the Quantum Time: "))
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
gantt=[]

time=sum(burst)
each=0

while(each<time):
    for every in range(i):
        if(arv[every]<=each):
            chartp.append(array[every])
            charts.append(each)
            if(quantum<=burst[every]):
                charte.append(each+quantum)
                each=each+quantum
                burst[every]=burst[every]-quantum
            else:
                charte.append(each+burst[every])
                each=each+burst[every]
                burst[every]=burst[every]-burst[every]
                        
            if(burst[every]==0):
                burst.remove(burst[every])
                array.remove(array[every])
                arv.remove(arv[every])
                i=i-1
                break

for each in range(len(chartp)):
    gantt.append(str(charts[each])+" - "+str(charte[each]))

    
print("\n Gantt Chart")   
print(tabulate([chartp,gantt],tablefmt="grid"))
print("\n")

end2=[]
wait=[]
turn=[]
      
for each in range(len(prog)):
    z=len(chartp)-(chartp[::-1].index(prog[each]))-1        
    turn.append(charte[z]-arrival[each])
    wait.append(turn[each]-comp[each])
    end2.append(charte[z])


table=zip(prog,arrival,comp,end2,wait,turn)
print(tabulate(table,["Programs","Arrival","Burst time","Completion time","Waiting","TurnAround"],tablefmt="grid"))


print("Average Wait time = "+str(round(sum(wait)/len(wait),2)))
print("Average TurnAround time = "+str(round(sum(turn)/len(turn),2)))
print("Average Throughput time = "+str(round(sum(comp)/len(comp),2)))