import math
import graph
import random
from graph import *
pointsChoice = input("Please enter the number of points you wish in the graph here: ") #choose the number of points you want to store in a .txt file
graphChoice = input("Please enter -1 if you want to create a Euclidian graph and a different number if want to create a metric graph here: ") # choose if you want a Euclid with x and y by inputing -1, or a different value if you want the metric
improvementEuclid = [False for i in range(100)] # this array aims to hold Boolean values that if they are true that means that the algorithm offered an improvement to the existing order of the graph
improvementMetric = [False for i in range(100)]
def creationEuclid():
    fe = open("randomExampleEuclid.txt" , "a")
    fe.truncate(0) 
    fe = open("randomExampleEuclid.txt" , "r+")
    for i in range(int(pointsChoice)):
        fe.write(str(random.randint(0,5000)) +" " + str(random.randint(0,5000)) + "\n")
    fe.close()


def creationDistances():
    f = open("randomExample.txt" , "a")
    f.truncate(0) #empty the file 
    f = open("randomExample.txt" , "r+")
    for i in range(int(pointsChoice)-1):
        for k in range(i+1,int(pointsChoice)):
            f.write(str(i) + " "+str(k)+ str(random.randint(0,500))+"\n")

    f.close()

if(int(graphChoice)==-1):
    c=0
    for i in range(100):
        
        creationEuclid()
        g = Graph(int(graphChoice),"randomExampleEuclid.txt")
        a = g.tourValue()
        g.prototype()
        b = g.tourValue()
        improvementEuclid[i] = b<a
        if(b<a):
            c+=1
    print(f"the improvements from starting order of points are: {improvementEuclid}\n And the precentageis: "+str(c)+"%")
else:
    c=0
    for i in range(100):
        
        creationDistances()
        g = Graph(int(graphChoice) , "randomExample.txt")
        a = g.tourValue() #hold the tour value upon creation
        g.prototype()
        b = g.tourValue() # hold the value after trying prototype algorithm
        improvementMetric[i] = b<a # compare and check if the algorithm improves the tour value
        if(b<a):
            c+=1
    print(f"the improvements are: {improvementMetric}\n And the precentage is : ",str(c)+"%")


if(int(graphChoice)==-1):
    c=0
    for i in range(100):
        creationEuclid()
        g = Graph(int(graphChoice),"randomExampleEuclid.txt")
        g.Greedy()
        a = g.tourValue()
        g.prototype()
        b = g.tourValue()
        improvementEuclid[i] = b<a
        if(b<a):
            c+=1
    print(f"the improvements COMPARED TO GREEDY: {improvementEuclid}\n And the precentage is: " +str(c)+"%")
else:
    c=0
    
    for i in range(100):
        creationDistances()
        g = Graph(int(graphChoice) , "randomExample.txt")
        g.Greedy()
        a = g.tourValue() #hold the tour value upon creation
        g.prototype()
        b = g.tourValue() # hold the value after trying prototype algorithm
        improvementMetric[i] = b<a # compare and check if the algorithm improves the tour value
        if(b<a):
            c+=1
    print(f"the improvements compaired to Greedy are: {improvementMetric}\n And the precentage: " +str(c)+"%")
