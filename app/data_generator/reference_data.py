from faker import Faker

fake = Faker("en_IN")

GENDERS = [
    "Male",
    "Female",
    "Other"
]

GENDER_WEIGHTS = [
    0.52,
    0.47,
    0.01
]

OCCUPATIONS = {
    "Software Engineer": (600000, 3000000),
    "Doctor": (1000000, 8000000),
    "Teacher": (400000, 1000000),
    "Lawyer": (800000, 5000000),
    "Business Owner": (500000, 20000000),
    "Student": (0, 300000),
    "Government Employee": (500000, 1800000),
    "Farmer": (250000, 1000000),
    "Retired": (200000, 1000000),
    "Freelancer": (300000, 2500000),
}

RISK_DISTRIBUTION = {
    "LOW": 75,
    "MEDIUM": 20,
    "HIGH": 5,
}

ACCOUNT_TYPES = [
    "Savings",
    "Current",
    "Salary",
    "Fixed Deposit",
]

ACCOUNT_TYPE_WEIGHTS = [
    70,
    15,
    10,
    5,
]

ACCOUNT_STATUS = [
    "ACTIVE",
    "INACTIVE",
    "BLOCKED",
]

ACCOUNT_STATUS_WEIGHTS = [
    92,
    5,
    3,
]

CURRENCIES = [
    "INR",
    "USD",
    "EUR",
]


TRANSACTION_TYPES = [
    "DEBIT",
    "CREDIT",
]

TRANSACTION_TYPE_WEIGHTS = [
    70,
    30,
]

TRANSACTION_CHANNELS = [
    "UPI",
    "NEFT",
    "RTGS",
    "IMPS",
    "ATM",
    "Cash",
    "Card",
]

TRANSACTION_CHANNEL_WEIGHTS = [
    45,
    12,
    5,
    10,
    8,
    5,
    15,
]

TRANSACTION_STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING",
]

TRANSACTION_STATUS_WEIGHTS = [
    95,
    3,
    2,
]

MERCHANT_CATEGORIES = [
    "Grocery",
    "Restaurant",
    "Fuel",
    "Hospital",
    "Pharmacy",
    "Shopping",
    "Travel",
    "Salary",
    "Investment",
    "Utilities",
]

COUNTRIES = [
    "India",
    "UAE",
    "Singapore",
    "United States",
    "United Kingdom",
    "Hong Kong",
]

HIGH_RISK_COUNTRIES = [
    "North Korea",
    "Iran",
    "Syria",
]