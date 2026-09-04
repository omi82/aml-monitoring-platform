import random

import pandas as pd

from faker import Faker

from app.core.constants import CUSTOMER_COUNT
from app.data_generator.reference_data import (
    GENDERS,
    GENDER_WEIGHTS,
    OCCUPATIONS,
)

from app.core.constants import RAW_DATA_DIR
from app.data_generator.export import CSVExporter

fake = Faker("en_IN")

def generate_customer_id(index: int) ->str:
    return f"CUST{index:06d}"

class CustomerGenerator:

    def __init__(self):
        self.customers = []

    def _generate_customer(self, index: int):
        gender = random.choices(
            GENDERS,
            weights=GENDER_WEIGHTS,
            k=1,
        )[0]

        occupation = random.choice(
            list(OCCUPATIONS.keys())
        )

        minimum, maximum = OCCUPATIONS[occupation]

        customer = {
            "customer_id": generate_customer_id(index),
            "full_name": fake.name(),
            "gender": gender,
            "age": random.randint(18, 80),
            "occupation": occupation,
            "annual_income": random.randint(minimum, maximum),
            "kyc_status": random.choices(
                [True, False],
                weights=[95, 5],
                k=1,
            )[0],
            "risk_category": random.choices(
                ["LOW", "MEDIUM", "HIGH"],
                weights=[75, 20, 5],
                k=1,
            )[0],
        }

        return customer

    def generate(self):
        for index in range(1, CUSTOMER_COUNT + 1):
            customer = self._generate_customer(index)
            self.customers.append(customer)

        print(f"Generated {len(self.customers):,} customers.")


    def save(self):
        """
        Save generated customers to CSV.
        """

        df = pd.DataFrame(self.customers)

        CSVExporter.export(
            df,
            RAW_DATA_DIR / "customers.csv",
        )