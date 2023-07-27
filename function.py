def consume( drug_amount , time):
    amount =0
    if time <=5:
        amount = drug_amount/5*time
    elif time >5 and time <=33:
        amount = -(time-5)*drug_amount/56+drug_amount
    elif time >33:
        amount =-(drug_amount/(2*(136-33)))*(time-136)         
    if amount>0:
        return amount
    else:
        return 0



def get_index(timetable,time):
    index =0
    for i in range(0,len(timetable),1 ):
        t =  timetable[i]
        if t >time:
            index=i-1
            break
    return index

def on_drug(drug,timetable, time):
    time_left=[]
    for i in range(0, int(time)+1):
        left=0
        index = get_index(timetable,i)
        for k in range(0,index+1):
            left = left+consume(drug[k],i-timetable[k])
        time_left.append((i,left))
    return time_left