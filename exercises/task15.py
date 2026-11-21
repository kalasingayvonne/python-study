#TASK 15: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK:
#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
#Write a normal program but use functions if you feel comfortable.








def calculate_gross(basic, benefits):
    return basic + benefits

def calculate_nhif(gross):
    if gross < 6000:
        return 150
    elif gross < 8000:
        return 300
    elif gross < 12000:
        return 400
    elif gross < 15000:
        return 500
    elif gross < 20000:
        return 600
    elif gross < 25000:
        return 750
    elif gross < 30000:
        return 850
    elif gross < 35000:
        return 900
    elif gross < 40000:
        return 950
    elif gross < 45000:
        return 1000
    elif gross < 50000:
        return 1100
    elif gross < 60000:
        return 1200
    elif gross < 70000:
        return 1300
    elif gross < 80000:
        return 1400
    elif gross < 90000:
        return 1500
    elif gross < 100000:
        return 1600
    else:
        return 1700
def calculate_nssf(gross):
    nssf_base = min(gross, 18000)   # only up to 18,000 is used
    return nssf_base * 0.06

#Task 17: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s NHDF using:
 #i.e NHDF = gross_salary *  0.015
#Write a normal program but use functions if you feel comfortable.

def calculate_nhdf(gross):
    return gross * 0.015

#Task 18: Using Python or PHP or Java or Ruby or JavaScript
#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
#Write a normal program but use functions if you feel comfortable.

def calculate_taxable_income(gross, nssf, nhdf, nhif):
    return gross - (nssf + nhdf + nhif)

#TASK 19: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK
#Write a normal program but use functions if you feel comfortable.

def calculate_paye(taxable_income):
    bands = [(24000, 0.10), (8333, 0.25), (467667, 0.30), (300000, 0.325)]
    personal_relief = 2400

    tax = 0
    remaining = taxable_income

    for band_size, rate in bands:
        portion = min(remaining, band_size)
        tax += portion * rate
        remaining -= portion

    tax += remaining * 0.35          # anything above 800,000

    tax -= personal_relief
    return max(tax, 0)

#Task 20: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s Net Salary using:
 #net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

def calculate_net_salary(gross, nhif, nhdf, nssf, paye):
     return gross - (nhif + nhdf + nssf + paye)

# ----- main program -----
basic = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

gross = calculate_gross(basic, benefits)
nhif = calculate_nhif(gross)
nssf = calculate_nssf(gross)
nhdf = calculate_nhdf(gross)
taxable = calculate_taxable_income(gross, nssf, nhdf, nhif)
paye = calculate_paye(taxable)
net = calculate_net_salary(gross, nhif, nhdf, nssf, paye)

print(f"Gross salary:   {gross:.2f}")
print(f"NHIF:           {nhif:.2f}")
print(f"NSSF:           {nssf:.2f}")
print(f"NHDF:           {nhdf:.2f}")
print(f"Taxable income: {taxable:.2f}")
print(f"PAYE:           {paye:.2f}")
print(f"Net salary:     {net:.2f}")