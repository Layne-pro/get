import matplotlib.pyplot as plt
n=sorted([2,255,127,64,32,5,0])
k=sorted([0.08, 3.25, 1.67, 0.87, 0.46, 0.118, 0.054])
plt.plot(n,k, marker='o')
plt.xlabel('число')
plt.ylabel('напряжение, В')
plt.show()