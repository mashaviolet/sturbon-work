#witi academy is proposing a sacco to help students save their money.
#Design a platform that will tha will do the following
#welcome to witi academy sacco
# 1. Deposit money
# 2. withdraw money
# 3. Check balance
#Ensure if the student selects 1, Money is deposited and the minimum diposit should be 1000
#If the student selects 2 , money should be withdrawn and the minimum withdraw is 500
#if the student selects 3, the balance should be displayed
# solution

def students_sacco():
    account_balance = 0
    run = 1
    print('Welcome to, WITIAcademy Sacco.')

    print('1. Deposit money')
    print('2. withdraw money')
    print('3. Check balance')

    student_choice = int(input('Enter your selection ( 1,2 or 3): '))
    if student_choice ==1:
        print("\n ...processing a deposit trasaction...")
        deposit_amount =int(input('Enter amount to be deposited : '))
    
        if deposit_amount < 1000:
           
           print('\n Minimum deposite is 1000')

        else :
            account_balance+=deposit_amount
            print(f'Dear student, you have deposited {deposit_amount:,} and your new account balance is {account_balance}.')
    elif student_choice == 2:
              print("\n ...processing a withdraw trasaction...")
              withdraw_amount =int(input('Enter amount to be withdrawn : '))  
              if account_balance == 0:
                   print("Your balance is 0")
              elif withdraw_amount < 500:
                   print('Minimum withdraw amount is 500')
              elif withdraw_amount > account_balance:
                   print(f'Withdraw failed, insufficient funds')
              else:
                   account_balance-=withdraw_amount
                   print(f'Dear student, you have withdrawn {withdraw_amount:,} and your new account balance is {account_balance}.')
    elif student_choice ==3:
        print(f'your account balance is {account_balance:,}')
        run = int(input("Enter 1 to continue or any number to exit : "))
        if run!=1:
             print('Thank you for joining our sacco')
                        
           


students_sacco()    