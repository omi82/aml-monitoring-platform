# Enterprise AML Data Warehouse

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

Customer → Transaction

Account → Transaction

Branch → Transaction

Country → Transaction

Device → Transaction

Transaction → Alert