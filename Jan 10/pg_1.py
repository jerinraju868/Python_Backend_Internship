''' Python Program to replicate bank transaction: 
        min balance 500, ask user to the amount to withdraw, 
        print the balance amount after withdrawal
        if user enters an amount greater than balance: 
            print:: insufficient balance. 
        if balance is below 500 
            print an alert message : your account balance is "available_balance", 
            Please  keep your account balance above Rs.500 to avoid unwanted charges.
'''

# accepting the withdrawl amount from the user
amnt = int(input('Enter the amount to withdraw : '))

# assigning the account balance
acnt_balance = 10000

# checks for the withdrawal amount is greater than availible balance
if amnt > acnt_balance:

    # if withdrawal amount is greater than balance then print the message insufficent balance
    print('Insufficient balance')

else:
    
    # after withdrawal the avalible balance is printing 
    print('your account balance is ', acnt_balance - amnt)
    print('Please  keep your account balance above Rs.500 to avoid unwanted charges')
