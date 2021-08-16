# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from distutils.util import strtobool
from src.accounts import User
from src.transaction import Transaction
import sys
import pandas as pd

accountsData = pd.read_csv("./data/client_accounts.csv", dtype={"locked": bool})
transactionsData = pd.read_csv(sys.argv[1])


transactions = [(Transaction(row.type, row.client, row.tx, row.amount)) for index, row in transactionsData.iterrows()]
accounts = [(User(row.clientId, row.available, row.held, row.total, row.locked)) for index, row in accountsData.iterrows()]

#
def accountById(id):
    for index, x in enumerate(accounts):
        if x.userID == id:
            return index

def createAccount(id):
    #create new account with default values (available, held, total = 0)
        return accounts.append(User(id, 0, 0, 0, False))

tempTransaction = {}
processedAccounts = []
for item in transactions:
    userID = accountById(item.clientID)

    if (userID is None):
        createAccount(item.clientID)
        userID = accountById(item.clientID)

    accounts[userID].transactions.append(item.__dict__)

for account in accounts:
    for trans in account.transactions:
        user = accountById(trans['clientID'])
        if trans['type'] == "deposit":
            accounts[user].deposit(trans['amount'])
            tempTransaction = trans
        elif trans['type'] == "withdrawal":
            accounts[user].withdraw(trans['amount'])
        elif trans['type'] == "dispute":
            if (tempTransaction['clientID'] == trans['clientID']):
                accounts[user].dispute(tempTransaction['amount'])
        elif trans['type'] == "resolve":
            if (tempTransaction['clientID'] == trans['clientID']):
                accounts[user].resolve(tempTransaction['amount'])
        elif trans['type'] == "chargeback":
            if (tempTransaction['clientID'] == trans['clientID']):
                accounts[user].chargeback(tempTransaction['amount'])

for account in accounts:
    processedAccounts.append([account.userID,account.available,account.held,account.total,account.locked])

finalState = pd.DataFrame(processedAccounts)
finalState.columns= ['client','available','held','total','locked']

finalState.to_csv(sys.stdout, index=False)
