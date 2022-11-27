import socket, math, scipy
from scipy import stats
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt



def multi():
    zink = [0, 1, 2, 3, 4, 5, 6, 71, 10, 11, 12, 13, 80, 20, 21, 22, 23, 100, 90, 70]
    Fmean = [[0]*6]*len(zink)
    Fvar = [[0]*6]*len(zink)
    prob = [[0]*6]*len(zink)
    
    for roll in range(len(zink)):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect(('localhost', 56701))

        message = ('throw '+ '1000' + ' '+ str(zink[roll]) +' \r\n').encode("utf-8")
        #message = ('throw '+input('anzahl der Würfe:')+' '+input('Kennzahl der Zinkung des Würfels:' )+'\r\n').encode("utf-8")
        s.send(message)
        data=s.recv(1024).decode()
        data=data.strip()
        print(roll)
        print(data)
        Fmean[roll], Fvar[roll], prob[roll] = save(data)
        print(Fvar[roll])
        plot(prob, zink)

        

#save throws in array and calc probability
def save(data):
    throws = [0,0,0,0,0,0]
    probability = [0,0,0,0,0,0]
    for i in data:
        i = int(i)
        if i == 1:
            throws[0]+=1
        if i == 2:
            throws[1]+=1
        if i == 3:
            throws[2]+=1
        if i == 4:
            throws[3]+=1
        if i== 5:
            throws[4]+=1
        if i == 6:
            throws[5]+=1
    for i in range(len(throws)):
        probability[i] = throws[i]/1000
    
    #print("probability: ", probability)
    
    #print("entropy: ", stats.entropy(throws, base=2))

    #binom = scipy.stats.binom.pmf(range(1,1000+1,1),len(data), probability[0])
    #print(binom)
    #print(sum(binom))
    mean = [0]*6
    var = [0]*6
    for i in range(6):
        mean[i], var[i] = binom.stats(len(data), probability[i], moments="mv")
        #print("mean und sdev", mean,math.sqrt(var))
    return mean, var, probability

def plot(prob, zink):
    control_y=binom.pmf(range(100,250,1),1000,1/6)
    for i in range(len(zink)):
        y=binom.pmf(range(100,250,1),1000,prob[i][0])
        plt.plot(range(100,250,1),y)
        plt.legend('s')
    plt.plot(range(100,250,1),control_y)
    plt.legend(['idealer Würfel'])
    plt.savefig('plot.png')

multi()