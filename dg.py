import matplotlib.pyplot as plt

class take_drugs():
    def __init__(self,drug,time) :
        self.drug =drug
        self.time =time

    def consume(self,t):
        amount =0
        if t>=0 and t <=5:
            amount = self.drug/5*t
        elif t>5 and t<=33:
            amount = -(t-5)*self.drug/56+self.drug
        elif t >33:
            amount =-(self.drug/(2*(136-33)))*(t-136)         
        if amount>0:
            return amount
        else:
            return 0
        
def get_drug_amount(drug_list,t):
    drugleft_time=[]
    for i in range(0,t+1):
        amount=0
        for drug in drug_list:
            if drug.time > i:
                break
            amount = amount+drug.consume(i-drug.time)
        drugleft_time.append((i,amount))
    return drugleft_time


drug_list1=[take_drugs(0.5,24*i) for i in range(0,10)]
drug_list2=[take_drugs(0.25,24*i) for i in range(0,10)]

d_a= [0.5, 0.25]
time = [y for y in range(0, 24 * 10 ,24)]
drug_list3= [take_drugs(d_a[i % len(d_a)], y) for i, y in enumerate(time)]





m1=get_drug_amount(drug_list1,220)
m2=get_drug_amount(drug_list2,220)
m3=get_drug_amount(drug_list3,220)



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