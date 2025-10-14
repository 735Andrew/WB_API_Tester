from typing import Dict
from fastapi import APIRouter, HTTPException
import sqlalchemy as sa
from .models import Sales
import app

router = APIRouter(prefix="/sales")


@router.get("/all")
def all_sales() -> Dict:

    report = dict()

    with app.engine.connect() as connection:
        query = sa.text("""SELECT * FROM sales;""")
        rows = connection.execute(query).mappings()

        for row in rows:
            date = row["date"]
            nmId = row["nmId"]
            price = row["price"]

            report[date] = {f"nmId_{nmId}": {"price": price}}

        connection.commit()

    return report


@router.get("/{date}")
def sales_per_day(date: str) -> Dict:

    with app.engine.connect() as connection:
        query = sa.select(Sales).where(Sales.date == date)
        row = connection.execute(query).fetchone()

        if row is not None:
            report = {row[1]: {f"nmId_{row[2]}": {"price": row[3]}}}
        else:
            raise HTTPException(
                status_code=404, detail=f"There is no sale with date '{date}'"
            )

        connection.commit()

    return report
