# Data Model

Fake data simulating a benefits platform (like Qwertys): users pay with a benefits card,
a PSP (payment provider) settles the money, and we reconcile both sides.

## programs
**Grain:** one row per bank/insurance client program.

| Column | Type | Description |
|---|---|---|
| program_id | text | Primary key |
| client_name | text | Name of the client (bank, insurer, retailer) |
| cashback_rate | number | Cashback percentage given to users |

## users
**Grain:** one row per user (beneficiary).

| Column | Type | Description |
|---|---|---|
| user_id | text | Primary key |
| program_id | text | Foreign key → programs |
| first_name | text | First name |
| last_name | text | Last name |
| email | text | Personal data (to be masked) |
| iban | text | Personal data (to be masked), used for cashback transfers |
| city | text | City |
| created_at | timestamp | When the user joined |

## transactions (Qwertys ledger)
**Grain:** one row per payment made by a user.

| Column | Type | Description |
|---|---|---|
| transaction_id | text | Primary key |
| user_id | text | Foreign key → users |
| program_id | text | Foreign key → programs |
| merchant_name | text | Shop where the payment happened |
| amount_eur | number | Amount paid |
| status | text | captured / failed |
| psp_reference | text | Join key to psp_settlements |
| created_at | timestamp | When the payment happened |

## psp_settlements (PSP side)
**Grain:** one row per settlement line sent by the PSP (can contain duplicates and orphans).

| Column | Type | Description |
|---|---|---|
| settlement_id | text | Primary key |
| psp_reference | text | Join key to transactions (not enforced: orphans exist) |
| gross_amount_eur | number | Amount paid by the user |
| fee_eur | number | PSP commission |
| net_amount_eur | number | gross - fee, what Qwertys receives |
| status | text | processing / settled |
| settled_at | timestamp | When the money moved |

## Relationships
programs ◄── users ◄── transactions ◄··· psp_settlements (via psp_reference)
