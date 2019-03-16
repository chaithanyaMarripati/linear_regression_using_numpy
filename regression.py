import numpy as np 
import matplotlib.pyplot as plt 
x=np.array([1,2,3,4,5,6,7,8,9,10,12,16])
y=np.array([1,5,3,5,8,6,9,7,10,12,16,18])
plt.ion()
n=len(x)
def error(m,b):
	sum=0
	for i in range(n):
		sum=sum+((((m*x[i])+b)-y[i])**2)
	sum=sum/n
	return sum
def m_grad(m,b):
	sum=0
	for i in range(n):
		sum=sum+((m*x[i]+b-y[i])*x[i])
	sum=sum*(0.2)
	return sum
def b_grad(m,b):
	sum=0
	for i in range(n):
		sum=sum+(m*x[i]+b-y[i])
	sum=sum*(0.2)
	return sum
learning_rate=0.001
m=0
b=1
epochs=50
def plot_fun(m,b):
	x=[0,20]
	y=[b,(20*m)+b]
	plt.plot(x,y)
	return 0
for i in range(epochs):
	print("error--"+str(error(m,b)))
	m=m-(learning_rate*m_grad(m,b))
	b=b-(learning_rate*b_grad(m,b))
	plt.title("epoch-"+str(i))
	plt.axis([0,20,0,20])
	plt.scatter(x,y)
	plot_fun(m,b)
	plt.draw()
	plt.pause(0.0001)
	plt.clf()
print("final error in this regression is"+str(error(m,b)))
