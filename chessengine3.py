
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sys


def feedforward(X,parameters):
    parameters['a'+str(0)]=X
    parameters['z'+str(1)]=np.dot(parameters['Theta'+str(1)],X)+ parameters['bias'+str(1)]
    maximum=np.amax(parameters['z'+str(1)],axis=0)
    avrg=np.mean( parameters['z'+str(1)],axis=0)
    parameters['a'+str(1)]=(parameters['z'+str(1)]-avrg)/maximum
    for i in range(2,100):
        parameters['z'+str(i)]=np.dot(parameters['Theta'+str(i)],parameters['a'+str(i-1)])+parameters['bias'+str(i)]
        maximum=np.amax(parameters['z'+str(i)],axis=0)
        avrg=np.mean(parameters['z'+str(i)],axis=0)
        parameters['a'+str(i)]=(parameters['z'+str(i)]-avrg)/maximum
    parameters['z'+str(100)]=np.dot(parameters['Theta'+str(100)],parameters['a'+str(99)])+parameters['bias'+str(100)]
    parameters['a'+str(100)]=(parameters['z'+str(100)])
    
    return 0

def cost_function(X,Y,parameters,m,lamda):
    
    sqsum=0
    for i in range(1,101):
        sqsum+=np.sum(np.square(parameters['Theta'+str(i)]))
    J = (1 /(2*m))*np.sum(np.square(parameters['a'+str(100)]-Y))  + ((1/(2*m))*sqsum)    
   
    return J

def back_prop(X,Y,parameters,lamda):
    m=(a,m)=np.shape(X)
    derivatives={ }
    derivatives['dz'+str(100)]=parameters['a'+str(100)]-Y 
    derivatives['dtheta'+str(100)]=(1/m)*np.dot((derivatives['dz'+str(100)]),((parameters['a'+str(99)]).T)) + (lamda/m)*parameters['Theta'+str(100)]
    derivatives['dbias'+str(100)]=(1/m)*(np.sum( derivatives['dtheta'+str(100)],axis=1,keepdims=True))
    for i in range(99,0,-1):
       
        derivatives['dz'+str(i)] =np.dot(((parameters['Theta'+str(i+1)]).T),((derivatives['dz'+str(i+1)])))/np.amax(parameters['z'+str(i)],axis=0)
        derivatives['dtheta'+str(i)]=(1/m)*(np.dot(derivatives['dz'+str(i)],( parameters['a'+str(i-1)].T))) + (lamda/m)*parameters['Theta'+str(i)]
        derivatives['dbias'+str(i)]=(1/m)*np.sum( derivatives['dz'+str(i)],axis=1,keepdims=True)
    return derivatives

def train(A,B,learning_rate,parameters,lamda):
    
    (a,m)=np.shape(A)
    p=(int)(m/64)
    lamda=lamda/p
    for n in range(1,10000):
        cost=0
        for t in range(1,p+1):
            lower=(t-1)*64
            upper=t*64
            X=A[:,lower:upper]
            Y=B[:,lower:upper]
            
            dervatives = { }
            feedforward(X,parameters)
            derivatives=back_prop(X,Y,parameters,lamda)
            for i in range(1,101):
                parameters['Theta'+str(i)]=parameters['Theta'+str(i)]- (learning_rate)*derivatives['dtheta'+str(i)]
                parameters['bias'+str(i)]=parameters['bias'+str(i)]- (learning_rate)*derivatives['dbias'+str(i)]
            cost+=cost_function(X,Y,parameters,m,lamda)
        print('Iteration ',end='')
        print(n,end='')
        print(' ',end=' ')
        print(cost)
    return 0

def predict_func(x,parameters):
    
    predict= { }
    predict['z'+str(1)]=np.dot(parameters['Theta'+str(1)],x)+ parameters['bias'+str(1)]
    maximum=np.amax(predict['z'+str(1)],axis=0)
    avrg=np.mean(predict['z'+str(1)],axis=0)
    predict['a'+str(1)]=(predict['z'+str(1)]-avrg)/maximum
    for i in range(2,100):
        predict['z'+str(i)]=np.dot(parameters['Theta'+str(i)],predict['a'+str(i-1)])+parameters['bias'+str(i)]
        maximum=np.max(predict['z'+str(i)],axis=0)
        avrg=np.mean(predict['z'+str(i)],axis=0)
        predict['a'+str(i)]=(predict['z'+str(i)]-avrg)/maximum
    predict['z'+str(100)]=np.dot(parameters['Theta'+str(100)],predict['a'+str(99)])+ parameters['bias'+str(100)]
    predict['a'+str(100)]=(predict['z'+str(100)])
    return  predict['a'+str(100)]
    
    
    
    
parameters = { }
dervatives = { }
predict = { }

parameters['Theta'+str(1)]= np.random.randn(100,65)
parameters['bias'+str(1)]=np.random.randn(100,1)

for i in range(2,101):
    parameters['Theta'+str(i)]= np.random.randn(100-i+1,100-i+2)
    parameters['bias'+str(i)]=np.random.randn(100-i+1,1)

lamda=0.5
learning_rate=0.01
A= np.random.randn(65,10000)
maximum=np.amax(A,axis=0)
avrg=np.mean(A)
A=A-avrg
A/=maximum


B=np.random.randn(1,10000)
#B/=np.amax(B,axis=0)

x=np.random.randn(65,1)
maximum=np.amax(x,axis=0)
avrg=np.mean(x)
x=x-avrg
x/=maximum

train(A,B,learning_rate,parameters,lamda)
predict_func(x,parameters)

   
    
    

