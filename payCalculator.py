def calculatePay():
    
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input('Enter pay per hour:'))
   
    if hrs <= 40:
        pay = hrs*rate
    else:
        pay = hrs*rate + (hrs-40)*rate*.5   
    print('Pay:', pay)    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()