import matplotlib.pyplot as plt
import function

drug_amount1 =[0.5 ,0.5, 0.5, 0.5,0.5,0.5,0.5,0.5,0.5,0.5]
drug_amount2 =[0.25 ,0.25, 0.25, 0.25,0.25,0.25,0.25,0.25,0.25,0.25]
drug_amount3 =[0.5 ,0.25, 0.5, 0.25,0.5,0.25,0.5,0.25,0.5,0.25]
T=[0,24,48,72,96,120,144,168,192,216]

m1=function.on_drug(drug_amount1,T,230)
m2=function.on_drug(drug_amount2,T,230)
m3=function.on_drug(drug_amount3,T,230)


x_1,y_1 =zip(*m1)
x_2,y_2=zip(*m2)
x_3,y_3=zip(*m3)



plt.figure()
plt.plot(x_1, y_1,  color='red',label=1)
plt.plot(x_2, y_2,  color='blue',label=2)
plt.plot(x_3, y_3,  color='green',label=3)
plt.xlabel("h")
plt.ylabel("amount")
plt.legend()
plt.show()