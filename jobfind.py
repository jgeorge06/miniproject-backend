import csv
import math

class Job:    
    def __init__(self,name,value):
        self.name=name
        self.value=value
        
    def __str__(self):
        return f"{self.name}({self.value})"
        
def ED(riasec):
    jobs=[]
    with open("riasec.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for job in csvreader:
            euclidianDistance=0
            for i in range (6):
                euclidianDistance+=(riasec[i]-float(job[i+1]))*(riasec[i]-float(job[i+1]))
            euclidianDistance=math.sqrt(euclidianDistance)
            jobs.append(Job(job[0],euclidianDistance))
            jobs.sort(key=sort)
    return (jobs)

def CR(riasec):
    jobs=[]
    with open("riasec.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for job in csvreader:
            dotProduct=0
            normUser=0
            normJob=0
            for i in range (6):
                dotProduct+=riasec[i]*float(job[i+1])
                normUser+=riasec[i]*riasec[i]
                normJob+=float(job[i+1])*float(job[i+1])
            normUser=math.sqrt(normUser)
            normJob=math.sqrt(normJob)
            profileCorelation=(dotProduct/(normUser*normJob))
            jobs.append(Job(job[0],profileCorelation))
            jobs.sort(key=sort,reverse=1)
    return (jobs)

def PC(riasec):
    jobs=[]
    with open("riasec.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for job in csvreader:
            numerator=0
            denominator1=0
            denominator2=0
            X=0
            Y=0
            for i in range (6):
                X+=riasec[i]
                Y+=float(job[i+1])
            X/=6
            Y/=6
            for i in range (6):
                numerator+=(riasec[i]-X)*(float(job[i+1])-Y)
                denominator1+=(riasec[i]-X)*(riasec[i]-X)
                denominator2+=(float(job[i+1])-Y)*(float(job[i+1])-Y)
            denominator1=math.sqrt(denominator1)
            denominator2=math.sqrt(denominator2)
            profileCorelation=(numerator/(denominator1*denominator2))
            jobs.append(Job(job[0],profileCorelation))
            jobs.sort(key=sort,reverse=1)
    return (jobs)

def HPHR(riasec):
    high=findHighs(riasec)
    jobs=[]
    with open("riasec.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for job in csvreader:
            for i in range (6):
                job[i+1]=float(job[1+1])
            jhigh=findHighs(job[1:])
            if jhigh==high:
                jobs.append(job[0])
    return jobs

def findHighs(riasec):
    highs=[]
    temp=riasec.copy()
    for i in range(3):
        highs.append(temp.index(max(temp)))
        temp[highs[i]]=0
    return highs
        
def findJob(riasec):
    highcount=0
    midcount=0
    lowcount=0
    temp=riasec.copy()
    high=max(temp)
    temp.pop(temp.index(high))
    tie=False
    if high==max(temp):
        tie=True
    for i in riasec:
        if i>5:
            highcount+=1
        elif i>3:
            midcount+=1
        else:
            lowcount+=1
    if highcount>2:
        return ED(riasec)
    elif tie:
        suited=HPHR(riasec)
        ed=ED(riasec)
        for i in ed:
            if i.name not in suited:
                ed.pop(ed.index(i))
        return ed
    elif lowcount==1:
        return PC(riasec)
    else:
        suited=HPHR(riasec)
        pc=PC(riasec)
        for i in pc:
            if i.name not in suited:
                pc.pop(pc.index(i))
        return pc
    

    
def sort(e):
    return e.value


