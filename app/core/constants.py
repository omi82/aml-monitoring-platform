from pathlib import Path


# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

PROCESSED_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# ==============================
# Data Volume
# ==============================

CUSTOMER_COUNT = 20_000

TRANSACTION_COUNT = 100_000


# ==============================
# Risk Distribution
# ==============================

HIGH_RISK_PERCENT = 5

MEDIUM_RISK_PERCENT = 20

LOW_RISK_PERCENT = 75


# ==============================
# Random Seed
# ==============================

RANDOM_SEED = 42


# ==============================
# ETL Configuration
# ==============================

ETL_BATCH_SIZE = 5_000


# ==============================
# Raw Data Files
# ==============================

RAW_CUSTOMERS_FILE = (
    RAW_DATA_DIR / "customers.csv"
)

RAW_ACCOUNTS_FILE = (
    RAW_DATA_DIR / "accounts.csv"
)

RAW_TRANSACTIONS_FILE = (
    RAW_DATA_DIR / "transactions.csv"
)


# ==============================
# Processed Data Files
# ==============================

PROCESSED_CUSTOMERS_FILE = (
    PROCESSED_DATA_DIR / "customers.csv"
)

PROCESSED_ACCOUNTS_FILE = (
    PROCESSED_DATA_DIR / "accounts.csv"
)

PROCESSED_TRANSACTIONS_FILE = (
    PROCESSED_DATA_DIR / "transactions.csv"
)


# ==============================
# Logging
# ==============================

LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ==============================
# Pagination
# ==============================

DEFAULT_PAGE = 1

DEFAULT_PAGE_SIZE = 20

MAX_PAGE_SIZE = 100


# ==============================
# Sorting
# ==============================

DEFAULT_SORT_ORDER = "desc"