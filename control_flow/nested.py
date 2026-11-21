credit_score=input('Enter your credit score:')
annual_income=input('Enter your annual income:')

credit_score=int(credit_score)
annual_income=int(annual_income)

if credit_score>700:
    if annual_income>50000:
     print('loan approved')
    else:
       print('income requirement not met')  
else:
    print('credit score too low')


