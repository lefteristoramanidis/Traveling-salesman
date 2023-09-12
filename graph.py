import math
import random

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        self.filename = filename
        file = open(filename, "r")
        line_count = 0
        content = file.read()
        content_list = content.splitlines() #list that holds each line
        counter = len(content_list)
        if(content_list[counter-1]==""):
            counter-=1

        file.close()
        self.line = content_list
        if (n==-1):
            self.n= counter
        else:
            self.n=n
        self.dists=[]
        

        
        if n==-1:
            for i in range(self.n):
                b = 0
                c = self.line[i].split(" ")
                while('' in c):
                    c.remove('')
                c[0] = int(c[0])
                c[1] = int(c[1])
                self.line[i] = c
            for i in range(self.n):
                self.dists.append([euclid(self.line[i],self.line[c]) for c in range(self.n)])


        if n!=-1:
            for i in range(self.n):
                row =[]
                for r in range(self.n):
                    row.append(0)
                self.dists.append(row)
            
            for i in range(counter):
                c = self.line[i].split(" ")
                while('' in c):
                    c.remove('')
                
                c[0] = int(c[0])
                c[1] = int(c[1])
                c[2] = int(c[2])

                
                self.line[i] = c
                self.dists[c[0]][c[1]] = c[2]
                self.dists[c[1]][c[0]] = c[2]
        self.perm = [i for i in range(self.n)]        


        
                    
                        
                    
                    
                
                   



      
    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        a=0
        for i in range(self.n):
            a+=self.dists[self.perm[i%self.n]][self.perm[(i+1)%self.n]]
        return a
    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        x = [self.perm[p] for p in range(self.n)] 
        a = x[i]
        x[i] = x[(i+1)%self.n]
        x[(i+1)%self.n] = a
        b = 0
        for k in range(self.n):
            b+=self.dists[x[k]][x[(k+1)%self.n]]
        
        if(b<self.tourValue()):
            
            self.perm = x
            return True
        else:
            
            return False

        
        

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        x = [self.perm[p] for p in range(0,i)]
        u = ([self.perm[p] for p in range(i,j+1)])
        o = u[::-1]
        for a in range(len(o)):
            x.append(o[a])
        for p in range(j+1,self.n):
            x.append(self.perm[p])
        b = 0
        for k in range(self.n):
            b+=self.dists[x[k]][x[(k+1)%self.n]]

        if(b<self.tourValue()):
            self.perm = x
            return True
        else:
            return False

    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True

                        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        x = [self.perm[p] for p in range(self.n)]
        for i in range(self.n-2):
            p=i+1
            
            for k in range(i+1,self.n):
                if(self.dists[x[i]][x[k]]<self.dists[x[i]][x[i+1]]):
                    o = x[i+1]
                    x[i+1] = x[k]
                    x[k] = o
        self.perm = x


    def prototype(self):
        x = [0 for i in range(self.n)]
        s = [0 for i in range(self.n)]
        
        
        averages = [0 for i in range(self.n)]
        for i in range(self.n):
            sum =0
            for k in range(self.n):
                sum+= self.dists[i][k]
            averages[i] = sum/self.n
            
        self.averages = [averages[i] for i in range(self.n)]
        left = True
        right = False
        right_index = self.n -1
        left_index = 0
        for i in range(self.n):
            p = 0
            for k in range(self.n):
                if(averages[k]>averages[p]):
                   p = k
            
            x[i] = p
            
            averages[p]=0

        s[right_index] = x[1]
        s[left_index] = x[0]
        right_index-=1
        left_index+=1
        for i in range(2,self.n):
            if(self.dists[x[i]][s[right_index+1]]<self.dists[x[i]][s[left_index-1]]):
                
                s[right_index] = x[i]
                right_index-=1
                

            elif(self.dists[x[i]][s[right_index+1]]>self.dists[x[i]][s[left_index-1]]):
                
                s[left_index] = x[i]
                left_index+=1
            else:
                if(self.dists[x[i]][s[self.n -1]]>self.dists[x[i]][s[0]]):
                    s[left_index] = x[i]
                    left_index+=1 
                else:
                    s[right_index] = x[i]
                    right_index-=1
        # c = []
        # c.append(x[0])
        # x.remove(x[0])
        # c.append(x[0])
        # x.remove(x[0])

        # for i in range(len(x)):

            
        #     if(self.dists[x[i]][c[len(c)-1]]<self.dists[x[i]][c[0]]):
        #         c.append(x[i])
                
        #     else:
        #         c.insert(0,x[i])
               
        self.perm = s