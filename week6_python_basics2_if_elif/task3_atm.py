from time import sleep
#This module has been imported so the sleep function can be used. The sleep function
#has been used to create a small delay where necessary to ensure the correct message
#is displayed to the user prior to input being requested.

class BankAccount:
    '''
    Create a BankAccount object with a name, account number, password and balance
    attributes.
    
    Attributes:
    name: str - the account holders name.
    account_no: int - the bank accounts number
    password: int - the password needed to access the account.
    balance: int - the starting balance of the acccount. Defaults to 0 if no value
    entered.
    
    Methods:
    There are currently no methods attached to this class.
    '''

    def __init__(self, name, account_no, password, balance=0):
        self.name = name
        self.account_no = account_no
        self.password = password
        self.balance = balance

bens_account = BankAccount('Ben', 1234, 1111, 10000)
toms_account = BankAccount('Tom', 9876, 2222, 5005)


def use_atm(my_account):
    '''
    This function mimics an atm. It requires a bank account class to be passed into it.
    The user then can view the balance, withdraw funds or deposit funds into the account.
    
    :param my_account: class - a BankAccount class object should be passed into this function.
    :return: there is no explict return. The outcome of this function is dependant on what
    input the user gives. Menus guide the options available.
    '''

    print('Please enter your password.')
    password = int(input('Please enter your password'))
    if password != my_account.password:
        return 'Incorrect password. Please take your card.'
    elif password == my_account.password:
        print('Welcome to Northern Frock - Please select an option. \n1 - Displace Balance\
        \n2 - Withdraw Funds \n3 - Deposit funds \n9 - Return Card')
        sleep(0.5)
        #this ensures the menu is printed to the console before input is requested.
    
        option = input('Please select an option from the menu')
        max_withdrawl  = my_account.balance - (my_account.balance % 10)
    
        if option == '1':
            print('Your current balance is £' + str(my_account.balance))
            if my_account.balance % 10 == 0:
                print('Your maxium withdrawl amount is £' + str(my_account.balance))
            else:
                print('Your maxium withdrawl amount is ' + str(max_withdrawl))

        elif option == '2':
            print('Please select an amount to withdraw. \n1 - £10 \n2 - £20 \n3 - £40\
                \n4 - £60 \n5 - £80 \n6 - £100 \n7 - Other amount \n8 - Return to main menu')
            withdrawl_option = input('Please select how much you would like to withdraw')
    
            if withdrawl_option == '1':
                if my_account.balance - 10 >= 0:
                    my_account.balance = my_account.balance - 10
                    print('You have withdrawn £10, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 10 < 0:
                    print('Sorry, there is not enough in your account to withdraw £10.')
                    sleep(1)
                    #This ensures the user can read the message before being asked to reinput
                    #their password.
                    use_atm(my_account)

            elif withdrawl_option == '2':
                if my_account.balance - 20 >= 0:
                    my_account.balance = my_account.balance - 20
                    print('You have withdrawn £20, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 20 < 0:
                    print('Sorry, there is not enough in your account to withdraw £20.')
                    sleep(1)
                    use_atm(my_account)

            elif withdrawl_option == '3':
                if my_account.balance - 40 >= 0:
                    my_account.balance = my_account.balance - 40
                    print('You have withdrawn £40, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 40 < 0:
                    print('Sorry, there is not enough in your account to withdraw £40.')
                    sleep(1)
                    use_atm(my_account)

            elif withdrawl_option == '4':
                if my_account.balance - 60 >= 0:
                    my_account.balance = my_account.balance - 60
                    print('You have withdrawn £60, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 60 < 0:
                    print('Sorry, there is not enough in your account to withdraw £60.')
                    sleep(1)
                    use_atm(my_account)

            elif withdrawl_option == '5':
                if my_account.balance - 80 >= 0:
                    my_account.balance = my_account.balance - 80
                    print('You have withdrawn £80, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 80 < 0:
                   print('Sorry, there is not enough in your account to withdraw £80.')
                   sleep(1)
                   use_atm(my_account)

            elif withdrawl_option == '6':
                if my_account.balance - 100 >= 0:
                    my_account.balance = my_account.balance - 100
                    print('You have withdrawn £100, your new balance is £' + str(my_account.balance))
                elif my_account.balance - 100 < 0:
                    print('Sorry, there is not enough in your account to withdraw £100.')
                    sleep(1)
                    use_atm(my_account)

            elif withdrawl_option == '7':
                requested_withdrawl = int(input('How much would you like to withdraw? Must be a \
                    multiple of 10'))
                if requested_withdrawl % 10 != 0:
                    print('Invalid amount requested. Returning to main menu')
                    sleep(1)
                    use_atm(my_account)
                elif requested_withdrawl % 10 == 0:
                    if my_account.balance - requested_withdrawl >= 0:
                        my_account.balance = my_account.balance - requested_withdrawl
                        print('You have withdrawn £' + str(requested_withdrawl), \
                            'your new balance is £' + str(my_account.balance))
                    elif my_account.balance - requested_withdrawl < 0:
                        print('Sorry, there is not enough in your account to withdraw £' \
                            + str(requested_withdrawl))
                        sleep(1)
                        use_atm(my_account)

            elif withdrawl_option == '8':
                use_atm(my_account)

            else:
                print('Invalid selection. Returning to main menu.')
                sleep(0.5)
                use_atm(my_account)

        elif option == '3':
            print('You have requested to deposit funds. if this is correct enter 1.\
                \nPress any other key to return to the main menu')
            confirm = input('Would you like to despoit funds?')

            if confirm == '1':
                print('How much would you like to deposit?')
                deposit = int(input('Please input the amount you would like to deposit.'))
                my_account.balance = deposit + my_account.balance
                print('Your new balance is £' + str(my_account.balance))
            else:
                use_atm(my_account)

        elif option == '9':
            return 'Here is your card. Have a good day.'

        else:
            print('Please select a valid option.')
            sleep(0.5)
            use_atm(my_account)

use_atm(bens_account)
