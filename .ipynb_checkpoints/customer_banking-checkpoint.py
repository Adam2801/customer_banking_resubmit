# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("what is your savings account balance?"))
    savings_interest_rate = float(input("what is your interest rate?"))
    savings_maturity = int(input("what is the maturity of your account?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("interest earned", interest_earned)
    print("savings maturity", savings_maturity)
    print ("updated_savings_balance", updated_savings_balance)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("what is your cd balance?"))
    cd_interest_rate = float(input("what is your interest rate?"))
    cd_maturity = int(input("what is the maturity of your account?"))


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("interest earned", interest_earned)
    print("cd maturity", cd_maturity)
    print("updated_cd_balance", updated_cd_balance)

if __name__ == "__main__":
    main()
