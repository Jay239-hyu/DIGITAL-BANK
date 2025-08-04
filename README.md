# 💳 DIGITAL BANK - Python Bank Account System

A simple yet secure Python-based banking system where users can register, log in using a 4-digit PIN, and perform transactions. All data is stored locally in JSON format, and transaction histories are maintained for each account.

---

## 🚀 Features

- 🔐 **Secure Registration & Login**
  - Create new accounts with a unique account number.
  - 4-digit PIN (hashed using SHA-256 for security).
  - 3 login attempts for security.

- 💰 **Account Operations**
  - Deposit money (unlimited).
  - Withdraw money (limit ₹25,000 per transaction).
  - Transfer money between accounts.

- 📜 **Transaction History**
  - Keeps a record of all deposits, withdrawals, and transfers.

- 💾 **Persistent Storage**
  - Account details and transaction history stored in `accounts.json`.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **JSON** for data storage
- **Hashlib** for secure PIN hashing
- **getpass** for hidden PIN input

---

## 📂 Project Structure
DIGITAL-BANK/
├── 01_program1.py # Main program
├── accounts.json # Stores user data (ignored in public repo)
├── README.md # Project documentation
├── .gitignore # Excludes accounts.json from repo
└── .gitattributes

## ⚙️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/DIGITAL-BANK.git
   cd DIGITAL-BANK
2.**Run the program**
python 01_program1.py

**Demo**
Welcome to the Python Bank!
1. Register
2. Login

Choose option: 1
Enter your name: John
Set 4-digit PIN: ****
Account created! Your account number is: 1001

🔒 Security Notes
PINs are hashed using SHA-256, so raw PINs are never stored.
accounts.json is excluded from the public repository using .gitignore to prevent leaking user data.

🧾 License: This project is licensed under the GNU GPL v3 License.





