print("TAKE-HOME PAY CALCULATOR 2022-23")
calc = True
while calc == True: #allows user to go again at the end if they want.
    #determine icome, including basic salary, bonuses, overtime, minus pension contributions
    gross_income = round(float(input("Please enter your gross annual salary: (E.G. For £30000 enter 30000.) ")), 2)
    contract_hrs = float(input("Please enter your weekly contract hours: (E.G. 20, 37.5, 40) "))

    if type(contract_hrs) != float:
        print("Please enter a number of contract hours.")

    if type(gross_income) != float:
        print("Please enter a valid salary.")
        gross_income = float(input("Please enter your gross annual salary: "))
    else:
        print(f"\nGreat! You have told me your gross salary is £{gross_income}. Let's find out about any additional income you may have, apart from your base salary.\n")

    overtime = input("Do you work overtime? (Y/N) ")
    
    if overtime != 'Y' and overtime != 'N':
        print("Please enter a valid answer.")
        overtime = input("Do you work overtime? (Y/N) ")

    if overtime == "Y":
        overtime_amount = float(input("How much overtime do you do per month in hours? (E.G. For 20 hours, enter 20.) "))
        overtime_pay = float(input("Enter your overtime pay rate. (1.5 or 2) "))
        overtime_tot = round(overtime_amount * 12 * overtime_pay * (gross_income/(52*contract_hrs)),2)
        print(f"\nThe overtime you earn this year has added up to £{overtime_tot}. \n")
    else:
        overtime_tot = 0

    bonus = input("Do you receive a bonus? (Y/N) ")

    if bonus != 'Y' and bonus != 'N':
        print("Please enter a valid answer.")
        bonus = input("Do you receive a bonus? (Y/N) ")

    if bonus == "Y":
        bonus_pay = round(float(input("Enter your annual bonus amount. (E.G. For £2000, enter 2000) ")), 2)
        print(f"\nThe bonus you earn this year is £{bonus_pay}. \n")
    else:
        bonus_pay = 0

    pension = input("Do you make pension contributions? (Y/N) ")

    if pension != 'Y' and pension != 'N':
        print("Please enter a valid answer.")
        pension = input("Do you make pension contributions? (Y/N) ")

    if pension == "Y":
        pens_prc = round(float(input("Enter the % you pay towards your pension. (E.G. Enter '2' for 2%) ")))
        pens_tot = round(((pens_prc/100) * gross_income),2)
        print(f"\nYour pension contributions for this year add up to £{pens_tot}. \n")
    else:
        pens_tot = 0

    #income: gross salary + bonus + overtime - pension contributions.
    pretax_inc_tot = round((gross_income + overtime_tot + bonus_pay - pens_tot),2)
    print(f"\nYour pre-tax income for this year is £{pretax_inc_tot}.\n") 

    #calculating income tax bands (20%, 40%, 45%)
    if pretax_inc_tot <= 12570:
        tax = 0
    elif 12571 <= pretax_inc_tot  and pretax_inc_tot <= 50270:
        tax = 0.2 * (pretax_inc_tot-12571)
    elif 50271 <= pretax_inc_tot and pretax_inc_tot <= 125140:
        tax = (0.2 * (50270-12571)) + (0.4 * (pretax_inc_tot-50271))
    elif 125141 <= pretax_inc_tot and pretax_inc_tot <= 150000:
        tax = (0.2 * (50270)) + (0.4 * (pretax_inc_tot-50271))
    elif pretax_inc_tot > 150000:
        tax = (0.2 * (50270)) + (0.4 * (150,000-50271)) + (0.45 * (pretax_inc_tot - 150000))

    tax = round(tax, 2)

    print(f"Your annual income tax bill is: £{tax}")

    #calculating national insurance
    #national insurance is calculated on monthly income
    monthly_inc = round((pretax_inc_tot/12),2)

    if monthly_inc <= 1048:
        ni = 0
    elif monthly_inc <= 4189:
        ni = 0.1325 * (pretax_inc_tot-1048)
    else:
        ni = (0.1325 * (4189-1048)) + (0.325 * (pretax_inc_tot - 4189))

    ni = round(ni, 2)
    print(f"\nYour National Inurance contribution this year is £{ni}. \n")

    takehomepay_y = round((pretax_inc_tot - ni - tax),2) #annual
    takehomepay_m = round((takehomepay_y/12),2) #monthly
    takehomepay_w = round((takehomepay_y/52),2) #weekly
    takehomepay_d = round((takehomepay_y/365),2) #daily

    print(f"Your take home pay is: \n Annually: £{takehomepay_y} \n Monthly:   £{takehomepay_m} \n Weekly:     £{takehomepay_w} \n Daily:       £{takehomepay_d}")
    repeat = str(input("\nDo you want to calculate take-home pay again? (Y/N) \n"))

    if repeat == "N":
        calc = False
