class BankAccount:
    '''
    '''

    def __init__(self, name, account_no, password, balance=0):
        self.name = name
        self.account_no = account_no
        self.password = password
        self.balance = balance

my_account = BankAccount('Ben', 1234, 1111, 10000)

print(my_account.balance)

def use_atm():
    print('Welcome to Northern Frock - Please select an option. \n1 - Displace Balance\
          \n2 - Withdraw Funds \n3 - Deposit funds \n9 - Return Card')
    
    option = input('Please select an option')
    max_withdrawl  = my_account.balance - (my_account.balance % 10)
    
    if option == '1':
        print('Your current balance is £' + str(my_account.balance))
        if my_account.balance % 10 == 0:
            print('Your maxium withdrawl amount is £' + str(my_account.balance))
        else:
            print('Your maxium withdrawl amount is ' + str(max_withdrawl))

    if option == '2':
        print('Please select an amount to withdraw. \n1 - £10 \n2 - £20 \n3 - £40\
            \n4 - £60 \n5 - £80 \n6 - £100 \n7 - Other amount \n8 - Return to main menu')
        withdrawl_option = input('Please select an option')
    
        if withdrawl_option == '1':
            if my_account.balance - 10 >= 0:
                new_balance = my_account.balance - 10
                print('You have withdrawn £10, your new balance is £' + str(new_balance))
            elif my_account.balance - 10 < 0:
                print('Sorry, there is not enough in your account to withdraw £10.')
                use_atm()

        if withdrawl_option == '2':
            if my_account.balance - 20 >= 0:
                new_balance = my_account.balance - 20
                print('You have withdrawn £20, your new balance is £' + str(new_balance))
            elif my_account.balance - 20 < 0:
                print('Sorry, there is not enough in your account to withdraw £20.')
                use_atm()

        if withdrawl_option == '3':
            if my_account.balance - 40 >= 0:
                new_balance = my_account.balance - 40
                print('You have withdrawn £40, your new balance is £' + str(new_balance))
            elif my_account.balance - 40 < 0:
                print('Sorry, there is not enough in your account to withdraw £40.')
                use_atm()

        if withdrawl_option == '4':
            if my_account.balance - 60 >= 0:
                new_balance = my_account.balance - 60
                print('You have withdrawn £60, your new balance is £' + str(new_balance))
            elif my_account.balance - 60 < 0:
                print('Sorry, there is not enough in your account to withdraw £60.')
                use_atm()

        if withdrawl_option == '5':
            if my_account.balance - 80 >= 0:
                new_balance = my_account.balance - 80
                print('You have withdrawn £80, your new balance is £' + str(new_balance))
            elif my_account.balance - 80 < 0:
                print('Sorry, there is not enough in your account to withdraw £80.')
                use_atm()

        if withdrawl_option == '6':
            if my_account.balance - 100 >= 0:
                new_balance = my_account.balance - 100
                print('You have withdrawn £100, your new balance is £' + str(new_balance))
            elif my_account.balance - 100 < 0:
                print('Sorry, there is not enough in your account to withdraw £100.')
                use_atm()

        if withdrawl_option == '7':
            requested_withdrawl = int(input('How much would you like to withdraw? Must be a \
                multiple of 10'))
            if requested_withdrawl % 10 != 0:
                print('Invalid amount requested. Returning to main menu')
                use_atm()
            elif requested_withdrawl % 10 == 0:
                if my_account.balance - requested_withdrawl >= 0:
                    new_balance = my_account.balance - requested_withdrawl
                    print('You have withdrawn £' + str(requested_withdrawl), \
                        'your new balance is £' + str(new_balance))
                elif my_account.balance - requested_withdrawl < 0:
                    print('Sorry, there is not enough in your account to withdraw £' \
                        + str(requested_withdrawl))
                    use_atm()

        if withdrawl_option == '8':
            use_atm()

    if option == '3':
        print('You have requested to deposit funds. if this is correct enter 1. Press any other key to return to the main menu')
        confirm = input('Would you like to despoit funds?')

        if confirm == '1':
            print('How much would you like to deposit?')
            deposit = int(input('Please input the amount you would like to deposit.'))
            new_balance = deposit + my_account.balance
            print('Your new balance is £' + str(new_balance))
        else:
            use_atm()

    if option == '9':
        return 'Here is your card. Have a good day.'

    else:
        print('Please select a valid option.')
        use_atm()

use_atm()
