# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:

# gross salary

def calc_grosssalary(a,b):
    gross=a+b
    return gross


basic_salary = float(input("enter basic salary: "))
benefits = float(input("enter benefits: "))

gross_salary=calc_grosssalary(basic_salary,benefits)
print(gross_salary)

def calc_nhif(sal):
    if sal<=5999 and sal>0:
        nhif_contribution=150
    elif sal>=6000 and sal<=7999:
        nhif_contribution=300
    elif sal>=8000 and sal<=11999:
        nhif_contribution=400
        
    return nhif_contribution

nhif=calc_nhif(gross_salary)
print(nhif)

# 16
def calc_nssf(gross,rate=0.06):
    if gross_salary<=18000:
        nssf_contribution=rate*gross_salary
    else:
        nssf_contribution=rate*18000
    return nssf_contribution

NSSF=calc_nssf(gross_salary)
print(NSSF)
# 17

def calc_nhdf(a,b=0.015):
    nhdf=a*b
    return nhdf

NHDF=calc_nhdf(gross_salary)
print(NHDF)
# 18
def calc_tax(a,b,c,d):
    tax=a-(b+c+d)
    return tax

taxable_income=calc_tax(gross_salary,nhif,NSSF,NHDF)
print(taxable_income)
# 19


def calc_payee(tax,relief=2400):
    if tax<=24000:
        payee=0
    elif tax>24000 and tax<=32333:
        payee=(0.1*24000)+(0.25 * (tax-24000))-relief
    elif tax>32333 and tax<=500000:
        payee=(0.1*24000)+(0.25*8333)+(0.3*(tax-32333))-relief
    elif tax>500000 and tax<=800000:
        payee=(0.1*24000)+(0.25*8333)+(0.3*467667)+(0.325*(tax-500000))-relief
    else:
        payee=(0.1*24000)+(0.25*8333)+(0.3*467667)+(0.325*300000)+(0.35*(tax-800000))-relief
    return payee

Payee=calc_payee(taxable_income)

print(Payee)

def calc_net(gross,nssf,nhdf,nhif,payee):
    net_pay=gross-(nssf+nhdf+nhif+payee)
    return net_pay

net_salary=calc_net(gross_salary,nhif,NSSF,NHDF,Payee)
print(net_salary)