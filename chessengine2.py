
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import sys

#assumption: i have a 65xm numpy array with each colmun representing a training example
# m:no.of training examples
# X: Training set.
#using 100 layers to learn the sufficient complexity of a game like chess. the number of nodes decreases by 1 in every layer.

#def sigmoid(matrix):
 #   return 1 / (1 + np.exp(-1*matrix))
def feedforward(X,parameters):
    parameters['a'+str(0)]=X
    parameters['z'+str(1)]=np.dot(parameters['Theta'+str(1)],X)+ parameters['bias'+str(1)]
    maximum=max(parameters['z'+str(1)])
    avrg=np.mean( parameters['z'+str(1)])
    parameters['a'+str(1)]=(parameters['z'+str(1)]-avrg)/maximum
    for i in range(2,100):
        parameters['z'+str(i)]=np.dot(parameters['Theta'+str(i)],parameters['a'+str(i-1)])+parameters['bias'+str(i)]
        maximum=max(parameters['z'+str(i)])
        avrg=np.mean(parameters['z'+str(i)])
        parameters['a'+str(i)]=(parameters['z'+str(i)]-avrg)/maximum
    parameters['z'+str(100)]=np.dot(parameters['Theta'+str(100)],parameters['a'+str(99)])+parameters['bias'+str(100)]
    parameters['a'+str(100)]=(parameters['z'+str(100)])

    return 0

def cost_function(X,Y,parameters,m,lamda):

    sqsum=0
    for i in range(1,101):
        sqsum+=np.sum(np.square(parameters['Theta'+str(i)]))
        #sqsum+=np.sum(parameters['Theta'+str(i)]**2)
    J = (1 /(2*m))*np.sum(np.square(parameters['a'+str(100)]-Y))  + ((1/(2*m))*sqsum)
   # J = (1 /(2*m))*np.sum((parameters['a'+str(100)]-Y)**2)  + ((1/(2*m))*sqsum)
    return J

def back_prop(X,Y,parameters,lamda):
    m=1
    derivatives={ }
    derivatives['dz'+str(100)]=parameters['a'+str(100)]-Y
    derivatives['dtheta'+str(100)]=(1/m)*np.dot((derivatives['dz'+str(100)]),((parameters['a'+str(99)]).T)) + (lamda/m)*parameters['Theta'+str(100)]
    derivatives['dbias'+str(100)]=(1/m)*(np.sum( derivatives['dtheta'+str(100)],axis=1,keepdims=True))
    for i in range(99,0,-1):
       # sig_der= parameters['a'+str(i)]*(1- parameters['a'+str(i)])
        derivatives['dz'+str(i)] =np.dot(((parameters['Theta'+str(i+1)]).T),((derivatives['dz'+str(i+1)])))/max(parameters['z'+str(i)])
        derivatives['dtheta'+str(i)]=(1/m)*(np.dot(derivatives['dz'+str(i)],( parameters['a'+str(i-1)].T))) + (lamda/m)*parameters['Theta'+str(i)]
        derivatives['dbias'+str(i)]=(1/m)*np.sum( derivatives['dz'+str(i)],axis=1,keepdims=True)
    return derivatives

def train(X,Y,learning_rate,parameters,lamda):
    m=1
    for n in range(1,1000):
        dervatives = { }
        feedforward(X,parameters)
        derivatives=back_prop(X,Y,parameters,lamda)
        for i in range(1,101):
            parameters['Theta'+str(i)]=parameters['Theta'+str(i)]- (learning_rate)*derivatives['dtheta'+str(i)]
            parameters['bias'+str(i)]=parameters['bias'+str(i)]- (learning_rate)*derivatives['dbias'+str(i)]
        print('Iteration ',end='')
        print(n,end='')
        print(' ',end=' ')
        print(cost_function(X,Y,parameters,m,lamda))
    return 0

def predict_func(x,parameters):

    predict= { }
    predict['z'+str(1)]=np.dot(parameters['Theta'+str(1)],x)+ parameters['bias'+str(1)]
    maximum=max(predict['z'+str(1)])
    avrg=np.mean(predict['z'+str(1)])
    predict['a'+str(1)]=(predict['z'+str(1)]-avrg)/maximum
    for i in range(2,100):
        predict['z'+str(i)]=np.dot(parameters['Theta'+str(i)],predict['a'+str(i-1)])+parameters['bias'+str(i)]
        maximum=max(predict['z'+str(i)])
        avrg=np.mean(predict['z'+str(i)])
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

lamda=0.01
learning_rate=0.01
X= np.random.randn(65,1)


#a=max(x)
#avrg=np.mean(X)

Y=4.8
x=np.random.randn(65,1)
train(X,Y,learning_rate,parameters,lamda)
predict_func(x,parameters)
#feedforward(X,parameters)
#print(parameters['a'+str(100)])
#print(cost_function(X,Y,parameters,1,lamda))
#print(max(X))












