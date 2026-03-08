import sys

amount=float(sys.argv[1]) # сумма кредита (PV)
rate=float(sys.argv[2]) # годовая ставка
months=int(sys.argv[3]) # срок в месяцах

if months<=0 or rate<0 or amount<=0:
    print([])
    sys.exit()

monthly_rate=rate/12

if monthly_rate==0:
    pmt=amount/months
else:
    pmt=amount*monthly_rate/(1-1/((1+monthly_rate)**months))

pmt=round(pmt, 2)

bal=amount
result=[]

if monthly_rate==0:
    for month in range(months):
        base=round(amount/months, 2)
        if month==months-1:
            base=round(bal, 2)
        result.append([pmt, base, 0.0])
        bal-=base
    print(result)
    sys.exit()

for month in range(months):
    percent=bal*monthly_rate
    percent=round(percent, 2)
    
    base=pmt-percent
    base=round(base, 2)
    
    bal-=base

    if month==months-2 and bal<0.01:
        base+=bal
        bal=0
        result.append([pmt, base, percent])
        break
    elif month==months-1:
        if abs(bal)>0.01:
            base+=bal
            percent=pmt-base
            bal=0
        result.append([pmt, base, percent])
    else:
        bal=round(bal, 2)
        result.append([pmt, base, percent])

print(result)