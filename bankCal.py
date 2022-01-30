print("\n\t\t\t\t\t\tWelcome to the Calonia Bank of Commerce !!\n")
print("@"*160, "\n\n")

BankRecords = {}

def OpenAcc():
    print()
    nm = input("Enter Person's name to open account for :- ").capitalize()
    age = int(input(f"Enter {nm}'s age :- "))
    aadhar = input(f"Enter the correct Aadhar No. of {nm} for verification : ")
    pas = input("Set a STRONG PASSWORD, in order to keep your account protected : ")
    bal = 0
    BankRecords[nm] = [pas, bal, age, aadhar]
    print(f"\nAccount have been successfully created for {nm}\n")
    print("\t\tYour ID is same as your Name - ", nm)
    print("\t\tYour PassWord is - ", pas)
    print("\nRemember Not to share this confidential infromation with anyone!\n")
    
def afterInterest(amnt, prd):
    final_amnt = amnt * (pow((1 + 7 / 100), prd))
    return round(final_amnt, 2)

def afterInterestForSC(amnt, prd):
    final_amnt = amnt * (pow((1 + 10 / 100), prd))
    return round(final_amnt, 2)


def main_func():
    print()
    print("Welcome to the Portal: ")
    print("Please Login to Continue - ")
    inp1 = input("Enter LOGIN ID : ")
    inp2 = input("Enter PASSWORD : ")

    for i in BankRecords:
        if inp1 == i and inp2 == (BankRecords[i])[0]:
            print("LOGIN SUCCESFUL!")
            while True:
                print()
                print("Press 0 to View Account Balance.")
                print("Press 1 to DEPOSIT money.")
                print("Press 2 to WITHDRAW money.")
                print("Press 3 to LOG OUT.")
                print("\tOur Compound interest rate is 7% P.A. for a savings account")
                print("\tInterest rate is 10% P.A. for a Senior Citizen (aged 60 or above!)")
                print("\tAnd minimun Balance required is ₹2000")
                ch = int(input("\t\tEnter your choice : "))

                if ch==0:
                    print(f"{i}'s Account Current Balance is ₹{(BankRecords[i])[1]}")

                elif ch==1:
                    amnt = int(input("Enter the AMOUNT you want to deposit (in INR) : "))
                    prd = float(input("Enter No. of Years for this amount : "))
                    if (BankRecords[i])[2] >= 60:
                        (BankRecords[i])[1] += afterInterestForSC(amnt, prd)
                    else:
                        (BankRecords[i])[1] += afterInterest(amnt, prd)

                    print("You have deposited money.")
                    print(f"After {prd} years, your balance is now ₹{(BankRecords[i])[1]} (including interest given)")

                elif ch==2:
                    print(f"Your current Balance is ₹{(BankRecords[i])[1]}")
                    with_amnt = int(input("Enter the AMOUNT you want to withdrawl (in INR) : "))

                    if with_amnt > (BankRecords[i])[1]-2000:
                        print("Insufficient Balnce or you need to maintain a minimum balance of ₹2000 ! Transaction failed ")
                        print("Till the balance reaches more than ₹2000, then only a withdrawl can be performed!")
                    else:
                        (BankRecords[i])[1] -= with_amnt
                        print(f"You have successfully withdrawn money. Current balance - ₹{(BankRecords[i])[1]}")

                elif ch==3:
                    print("SUCCESSFULLY LOGGED OUT !")
                    break
                else:
                    print("Invalid choice.")


while True:
    print("\nType - LOGIN to login into your account and perform further actions!")
    print("Don't have an account? Open Now by typing - OPEN ")
    print("Type EXIT to leave this Service.\n")
    inp = input("Enter your Action HERE : ").upper()

    if inp == "LOGIN":
        main_func()

    elif inp == "OPEN":
        OpenAcc()
        cont = input("Continue Login in ? (Y/N) : ").upper()
        if cont == "Y" or cont == "YES":
            main_func()
        else:
            print("Thank you for creating account!")


    elif inp == "EXIT":
        print("Hope to see you back Again !\nThank You!")
        break

    else:
        print("Invalid Input Given!! Try Again")
