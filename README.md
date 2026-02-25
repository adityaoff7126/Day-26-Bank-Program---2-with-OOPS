# Bank Management System (CLI-Based)

## Overview

This is a command-line based Bank Management System built using Python. It simulates basic banking operations such as account creation, deposit, withdrawal, transfer, and transaction history tracking. The system uses Object-Oriented Programming concepts and encapsulation for secure handling of user data.

---

## Features

* Create a new bank account
* Secure login using account number and PIN
* Deposit money
* Withdraw money
* Transfer money between accounts
* View account balance
* View transaction history
* Menu-driven interface

---

## Concepts Used

* Classes and Objects
* Encapsulation (private variables using `__pin`)
* Dictionaries for data storage
* Loops and conditional statements
* Basic input/output handling

---

## Class Structure

### 1. BankAccount Class

Handles individual user account operations.

Attributes:

* name: Account holder name
* __pin: Private PIN for security
* account_number: Unique account number
* balance: Current account balance
* history: List of transactions

Methods:

* deposit(amount, pin)
* withdraw(amount, pin)
* transfer(other_account, amount, pin)
* show_history(pin)

---

### 2. Bank Class

Manages multiple accounts.

Attributes:

* accounts: Dictionary storing account_number → BankAccount object

Methods:

* create_account(name, pin, balance)
* get_account(acc_no)

---

## How It Works

1. User runs the program

2. Main menu appears:

   * Create Account
   * Login
   * Exit

3. After login:

   * Deposit
   * Withdraw
   * Transfer
   * Check Balance
   * View History
   * Logout

4. All operations require correct PIN verification

---

## Security

* PIN is stored as a private variable (`__pin`)
* Direct access to PIN is restricted
* All sensitive operations require PIN validation

---

## Limitations

* Data is not saved permanently (no database or file storage)
* PIN is stored in plain format (not encrypted)
* No limit on incorrect PIN attempts
* No user interface (CLI only)

---

## Possible Improvements

* Add file/database storage (JSON, SQLite)
* Encrypt PIN using hashing
* Add login attempt limits
* Add timestamps to transactions
* Convert to GUI (Tkinter/PyQt) or Web App (Flask/Django)

---

## How to Run

1. Make sure Python is installed
2. Run the script:


3. Follow on-screen menu instructions



## Conclusion

This project demonstrates core programming concepts and simulates a real-world banking workflow. It is suitable for beginners transitioning into intermediate-level Python and system design.
