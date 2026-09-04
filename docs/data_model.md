# AML Data Warehouse

## Dimension Tables

- dim_customer
- dim_account
- dim_branch
- dim_country
- dim_device
- dim_date

## Fact Tables

- fact_transaction
- fact_alert

## Relationships

Customer (1) ---- (N) Account

Customer (1) ---- (N) Transaction

Branch (1) ---- (N) Transaction

Country (1) ---- (N) Transaction

Device (1) ---- (N) Transaction

Date (1) ---- (N) Transaction

Transaction (1) ---- (N) Alert