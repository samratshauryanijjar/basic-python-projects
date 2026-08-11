# ATM Machine Simulator 🏦

A simple ATM-style banking simulator built in Python.

The program allows the user to log in, check their balance, deposit money, withdraw money, and exit the program.

## Features

- 🔐 Username and password login
- 💰 Check account balance
- 💵 Deposit money
- 💸 Withdraw money
- 💾 Saves the balance to a text file
- 🔄 Menu keeps running until the user chooses to exit

## How It Works

The program starts by loading the current balance from `balance.txt`.

The user then logs in using their credentials.

After a successful login, the ATM menu provides four options:

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Whenever money is deposited or withdrawn, the updated balance is saved back to `balance.txt`, so the balance remains available when the program is run again.

## What I Learned

- Functions
- `if`, `elif`, and `else`
- `while` loops
- User input
- File handling
- Reading and writing text files
- Variables and arithmetic operations
- Basic login validation
- Using a separate file to store data

## How to Run

Make sure Python is installed.

Keep both files in the same folder:

```text
atm-simulator/
├── main.py
└── balance.txt

Username: admin
Password: 1234


Your actual program loads the starting balance from `balance.txt`, currently stores `500`, and updates that file after deposits and withdrawals. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

I'd **definitely keep `balance.txt` in the repo for this project**, because it's part of how your simulator works. And the README makes it clear that the login is just for learning, because `admin / 1234` is about as secure as putting the bank vault key under the doormat. 😂
