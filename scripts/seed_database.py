from app.database.session import SessionLocal

from app.models.branch import Branch
from app.models.country import Country

from app.seeds.branches import BRANCHES
from app.seeds.countries import COUNTRIES
from app.seeds.seeder import Seeder
from app.models.device import Device

from app.seeds.devices import DEVICES


def main():

    db = SessionLocal()

    try:

        seeder = Seeder(db)

        seeder.seed(
            Country,
            COUNTRIES,
        )

        seeder.seed(
            Branch,
            BRANCHES,
        )
        seeder.seed(
            Device,
            DEVICES,
        )

    finally:
        db.close()


if __name__ == "__main__":
    main()