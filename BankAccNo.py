#Write a Program to Accept Bank AccNo and Balance.
#Calculate interest as following
#if the Balnace is >= 1000000 then interest is 10%
#if the Balance is >= 500000 then interest is 7%
#if the Balance is >= 100000 then interest is 5%
#else no Interest is given.
#Display AccNo, Balance and Interest Amount.

acc_no = int(input("Enter Bank Account Number: "))
balance = float(input("Enter Balance: "))

if balance >= 1000000:
    rate = 10
elif balance >= 500000:
    rate = 7
elif balance >= 100000:
    rate = 5
else:
    rate = 0

interest = (balance * rate) / 100

print("Account Number:", acc_no)
print("Balance:", balance)
print("Interest:", interest)

