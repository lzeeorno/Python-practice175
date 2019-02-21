
# Setup:
accounts = {}
input_file_exists = False
    
# Open the input file:
try:
    input_file = open("lab2q1_input_accounts.txt", "r")
    input_file_exists = True
except:
    print("Input file not found, program will exit")
    
# Read in the accounts:
if input_file_exists:
    for line in input_file:
        line_contents = line.split(":")
        
        name = line_contents[0]
        try:
            balance = float(line_contents[1])
        except:
            print("Account for", line_contents[0], "not added: illegal value for balance")
            continue
        accounts[name] = balance
        
    input_file.close()

        
# Loop, allowing the user to enter transactions:
while input_file_exists:
    account = input("Enter account name, or 'Stop' to exit: ")
    
    if (account == "Stop"):
        break
    
    if account in accounts:
        try:
            change = float(input("Enter transaction amount: "))
            accounts[account] = accounts[account] + change
            print("New balance for account " + account + ":", accounts[account])
        except:
            print("Illegal value for transaction, transaction canceled")
        
    else:
        print("Account does not exist, transaction canceled")