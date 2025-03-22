# NexusBanking Data Dictionary

This document provides detailed specifications for all data elements in the NexusBanking platform. It will be updated as the project evolves to ensure it remains a comprehensive reference for all data attributes.

## PostgreSQL Database

### Table: customers

| Column Name    | Data Type      | Constraints        | Description                                      |
|----------------|----------------|--------------------|-------------------------------------------------|
| customer_id    | SERIAL         | PK, NOT NULL       | Unique identifier for the customer              |
| first_name     | VARCHAR(50)    | NOT NULL           | Customer's legal first name                     |
| last_name      | VARCHAR(50)    | NOT NULL           | Customer's legal last name                      |
| date_of_birth  | DATE           | NOT NULL           | Date of birth for individual customers          |
| email          | VARCHAR(100)   | UNIQUE, NOT NULL   | Primary email address for communications        |
| phone          | VARCHAR(20)    | NOT NULL           | Primary contact phone number                    |
| tax_id         | VARCHAR(20)    | UNIQUE, NOT NULL   | SSN, EIN, or other tax identification number    |
| customer_type  | VARCHAR(20)    | NOT NULL           | Enumeration: 'INDIVIDUAL', 'BUSINESS'           |
| status         | VARCHAR(20)    | NOT NULL           | Enumeration: 'ACTIVE', 'INACTIVE', 'SUSPENDED'  |
| created_at     | TIMESTAMP      | NOT NULL, DEFAULT  | When the customer record was created            |
| updated_at     | TIMESTAMP      | DEFAULT            | When the customer record was last updated       |
| kyc_status     | VARCHAR(20)    | NOT NULL           | Enumeration: 'PENDING', 'VERIFIED', 'REJECTED'  |

### Table: customer_addresses

| Column Name     | Data Type      | Constraints               | Description                                      |
|-----------------|----------------|---------------------------|-------------------------------------------------|
| address_id      | SERIAL         | PK, NOT NULL              | Unique identifier for the address                |
| customer_id     | INTEGER        | FK, NOT NULL              | Reference to customers.customer_id               |
| address_type    | VARCHAR(20)    | NOT NULL                  | Enumeration: 'PRIMARY', 'MAILING', 'BUSINESS'    |
| street_address  | VARCHAR(100)   | NOT NULL                  | Street number and name                           |
| city            | VARCHAR(50)    | NOT NULL                  | City name                                        |
| state           | VARCHAR(50)    | NOT NULL                  | State or province                                |
| postal_code     | VARCHAR(20)    | NOT NULL                  | ZIP or postal code                               |
| country         | VARCHAR(50)    | NOT NULL                  | Country name                                     |
| validated       | BOOLEAN        | NOT NULL, DEFAULT FALSE   | Whether address has been verified                |
| created_at      | TIMESTAMP      | NOT NULL, DEFAULT         | When the address was added                       |
| updated_at      | TIMESTAMP      | DEFAULT                   | When the address was last updated                |

### Table: accounts

| Column Name      | Data Type      | Constraints                | Description                                       |
|------------------|----------------|----------------------------|---------------------------------------------------|
| account_id       | SERIAL         | PK, NOT NULL               | Unique identifier for the account                 |
| account_number   | VARCHAR(20)    | UNIQUE, NOT NULL           | Formatted account number for customer reference   |
| customer_id      | INTEGER        | FK, NOT NULL               | Reference to customers.customer_id                |
| account_type     | VARCHAR(20)    | NOT NULL                   | Enumeration: 'CHECKING', 'SAVINGS', 'INVESTMENT'  |
| balance          | DECIMAL(18,2)  | NOT NULL, DEFAULT 0.00     | Current account balance                           |
| status           | VARCHAR(20)    | NOT NULL                   | Enumeration: 'ACTIVE', 'DORMANT', 'CLOSED', 'SUSPENDED' |
| interest_rate    | DECIMAL(5,4)   | NOT NULL, DEFAULT 0.0000   | Annual interest rate percentage                   |
| currency         | VARCHAR(3)     | NOT NULL, DEFAULT 'USD'    | ISO currency code                                 |
| minimum_balance  | DECIMAL(18,2)  | NOT NULL, DEFAULT 0.00     | Required minimum balance                          |
| created_at       | TIMESTAMP      | NOT NULL, DEFAULT          | When the account was created                      |
| updated_at       | TIMESTAMP      | DEFAULT                    | When the account was last updated                 |

### Table: transactions

| Column Name           | Data Type      | Constraints             | Description                                         |
|-----------------------|----------------|-------------------------|-----------------------------------------------------|
| transaction_id        | SERIAL         | PK, NOT NULL            | Unique identifier for the transaction               |
| account_id            | INTEGER        | FK, NOT NULL            | Reference to accounts.account_id                    |
| amount                | DECIMAL(18,2)  | NOT NULL                | Transaction amount (positive or negative)           |
| transaction_type      | VARCHAR(20)    | NOT NULL                | Enumeration: 'DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'FEE', 'INTEREST' |
| status                | VARCHAR(20)    | NOT NULL                | Enumeration: 'PENDING', 'COMPLETED', 'FAILED', 'CANCELLED' |
| timestamp             | TIMESTAMP      | NOT NULL, DEFAULT       | When the transaction occurred                       |
| description           | VARCHAR(200)   | NOT NULL                | Description of the transaction                      |
| reference_number      | VARCHAR(50)    |                         | External reference number                           |
| related_transaction_id| INTEGER        | FK                      | Reference to a related transaction (for transfers)  |
| location              | VARCHAR(100)   |                         | Where transaction originated from                   |
| balance_after         | DECIMAL(18,2)  | NOT NULL                | Account balance after this transaction              |

### Table: transfer_transactions

| Column Name             | Data Type      | Constraints            | Description                                         |
|-------------------------|----------------|------------------------|-----------------------------------------------------|
| transaction_id          | INTEGER        | PK, FK, NOT NULL       | Reference to transactions.transaction_id            |
| source_account_id       | INTEGER        | FK, NOT NULL           | Account funds are transferred from                  |
| destination_account_id  | INTEGER        | FK, NOT NULL           | Account funds are transferred to                    |
| transfer_type           | VARCHAR(20)    | NOT NULL               | Enumeration: 'INTERNAL', 'EXTERNAL'                 |
| routing_number          | VARCHAR(20)    |                         | For external bank transfers                         |
| recipient_name          | VARCHAR(100)   |                         | For external transfers                              |
| memo                    | VARCHAR(200)   |                         | Notes regarding the transfer                        |
