from cd_account import create_cd_account
from savings_account import create_savings_account

# This method sets the balance of the account.
def set_balance(self, balance):
    """Sets the balance for the for the account"""
    self.balance = balance

# The method sets the interest gained for the account.
def set_interest(self, interest):
    """Sets the interest gained for the the account"""
    self.interest = interest

    # Import the create_cd_account and create_savings_account functions# Call the create_savings_account function and pass the variables from the user.
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
