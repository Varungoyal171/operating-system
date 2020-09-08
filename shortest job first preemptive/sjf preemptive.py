# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:02:36 2020

@author: Varun Goel

Varun Goel
fsfs
avg waittime
avg throghput
avg turnaround time
"""


from tabulate import tabulate
array=[]
arv=[]
burst=[]

j=0
i=int(input("Enter no.s of program: "))
prog=int(input("Want to enter program name manually 1 for yes: "))

#input the table

while(j<i):
    if(prog==1):
        a=input(" Enter the programs: ")
    else:
        a="P"+str(j)

    array.append(a)
    print("\n Program "+a,end="")
    a=int(input("Enter the arrival time : "))
    b=int(input("Enter burst time: "))
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
    
    #programs available to execute according to arriavl time
    for every in range(i):
        if(arv[every]<=each):
            program.append(array[every])
            clock.append(arv[every])
            end.append(burst[every])
    
    if(len(end)>0):
        z=end.index(min(end)) #smallest job program out of list
        chartp.append(program[z])
        charts.append(each)
        charte.append(each+1)
        
        #decrease the time according to time
        burst[z]=burst[z]-1
        #remove the programs which have beem executed completely
        if(burst[z]==0):
            array.remove(array[z])
            arv.remove(arv[z])
            burst.remove(burst[z])
            i=i-1
        
    each=each+1

#gantt chart 1
'''
gantt=[]

for each in range(len(chartp)):
    gantt.append(str(charts[each])+"-"+str(charte[each]))
    
print("\n Gantt Chart")   
print(tabulate([chartp,gantt],tablefmt="grid"))
print("\n")
'''

#gantt chart 2
ganttp=[]# gannt array to store program name
#start=[]
#end=[]
gantt=[]#store the time clock
each=0

#program to order the gantt chart
temp=0
while(each<len(chartp)):  
    i=each
    flag=1
    
    #when the previous program and next one are same
    while((i<len(chartp)-1) and chartp[i]==chartp[i+1]):
        i=i+1 #i have the last address of the program in the array
        flag=0
        
    ganttp.append(chartp[each])
    #start.append(charts[each])
    #end.append(charte[i])
    gantt.append(str(charts[each])+"-"+str(charte[i]))

    if(flag==1):#program counter
        each=each+1
    else:
        each=i+1 #skip the counter to the last of counted program


print("\n Gantt Chart ")   
print(tabulate([ganttp,gantt],tablefmt="grid"))
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
