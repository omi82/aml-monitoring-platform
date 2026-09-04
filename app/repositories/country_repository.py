from sqlalchemy import select

from app.models.country import Country


class CountryRepository:

    def __init__(self, db):
        self.db = db

    def get_high_risk_countries(self) -> set[str]:
        countries = self.db.scalars(
            select(Country.country_name).where(
                Country.is_high_risk.is_(True)
            )
        ).all()

        return set(countries)