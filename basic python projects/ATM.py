# ATM Simulator

import os, sys, time, logging
from datetime import datetime


### To Do List ###

# Insert your card
# Authentication (PIN verification)
# Choose from Menus (Check Balance, Transfer, Withdraw)
# Repeat if yes else exit


# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')


# Current day and Time
DT = datetime.now()
print(DT)
time.sleep(0.6)
print('Please insert in Your Card...')
time.sleep(2)
print('Please wait Loading Card...')
time.sleep(1)
print("""
============================================
======= Welcome to TN ATM center ========
======= Author : SNEHA R   ============
============================================
""")
time.sleep(2)


def transactions():
     confirm = True
     money = 25000
     def check_balance():
          print(f"Your Balance is: {money}")
          while confirm:
               again = input("Do you want to perform another transaction? (yes/no) : ").lower()
               if again == "yes":
                    time.sleep(1)
                    transactions()
               elif again == "no":
                    break
               else:
                    print("Type either yes/no.")
     def withdraw():
          amnt = int(input("Enter the amount to withdraw: "))
          time.sleep(1)
          print("Transaction processing...")
          time.sleep(0.8)
          print(f"Withdrawing {amnt}.")
          time.sleep(1)
          print("Done! Please take your cash.")
          while confirm:
               again = input("Do you want to perform another transaction? (yes/no) : ").lower()
               if again == "yes":
                    time.sleep(1)
                    transactions()
               elif again == "no":
                    break
               else:
                    print("Type either yes/no.")
     def transfer():
          while confirm:
               receiver = input("Enter the account Number: ")
               amnt = input("Enter the amount to Transfer: ")
               if len(receiver) == 10:
                    time.sleep(1)
                    print(f"You Transfered {amnt} to {receiver}")
                    time.sleep(1)
                    print("Transfer is Successfull.")
                    time.sleep(1)
                    again = input("Do you want to perform another transaction? (yes/no) : ").lower()
                    if again == "yes":
                         time.sleep(1)
                         transactions()
                    elif again == "no":
                         break
                    else:
                         print("Type either yes/no.")
               else:
                    print("Incorrect Account Details")

     print("""
What would you Like to Perform?
1. Check Balance
2. Withdraw
3. Transfer
4. Exit
""")
     transaction = int(input("Choose 1/2/3/4: "))
     time.sleep(1)
     
     logging.basicConfig(filename='reference.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')

     if transaction == 1:
          TT = 'CHECK BALANCE'
          logging.debug('Transaction Type: {}'.format(TT))
          time.sleep(1)
          check_balance()
     elif transaction == 2:
          TT = 'WITHDRAW'
          logging.debug('Transaction Type: {}'.format(TT))
          time.sleep(1)
          withdraw()
     elif transaction == 3:
          TT = 'TRANSFER'
          logging.debug('Transaction Type: {}'.format(TT))
          time.sleep(1)
          transfer()
     else:
          print('Thankyou..')
          sys.exit()
     #logging.basicConfig(filename='reference.log', level=logging.DEBUG, format='%(asctime)s:%(message)s')
     #logging.debug('Transaction Type: %(TT)s')
     # if transaction == 1:
     #      TT = 'CHECK BALANCE'
     # elif transaction == 2:
     #      TT = 'WITHDRAW'
     # elif transaction == 3:
     #      TT = 'TRANSFER'
     


def get_pin():
     #for j in range(0,4):
          #pin = int(input("Enter you PIN: "))
          #with open('pins.txt', 'r') as p:
               #check_pin = p.read()
     pins = [1234, 4565, 8789, 1635, 5855, 1180, 6666]
     for i in pins:
          try:
               for j in range(1,4):
                    try:
                         pin = int(input("Enter you PIN: "))
                         if pin in pins:
                              print('Welcome To Your Account')
                              time.sleep(2)
                              transactions()
                              sys.exit()
                         else:
                              print('Incorrect PIN')
                    except Exception as e:
                         print('Use Numbers Only')
                         break
               break
          except Exception as e:
               print("Choose the correct pin")

get_pin()