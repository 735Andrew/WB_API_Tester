from typing import Dict
import datetime
import requests as r
from sqlalchemy import text
from config import WB_TOKEN
from app import engine


def report_creator() -> Dict:
    URL = "https://statistics-api-sandbox.wildberries.ru/api/v1/supplier/sales?"

    # Calculating the start of two weeks period
    today = datetime.date.today()
    start_of_current_week = today - datetime.timedelta(days=today.weekday())
    start_of_two_weeks_ago = start_of_current_week - datetime.timedelta(days=14)

    sales = r.get(
        URL,
        headers={"Authorization": WB_TOKEN},
        params={
            "dateFrom": f"{start_of_two_weeks_ago}",
            "flag": 0,
        },
    ).json()

    report = dict()

    with engine.connect() as connection:

        for sale in sales:
            date = sale["date"][:10]
            nmId = sale["nmId"]
            price = sale["totalPrice"]

            query = text(
                """
            INSERT INTO sales
            (date, "nmId", price)
            VALUES
            (:date_val, :nmId_val, :price);
            """
            )
            params = {"date_val": date, "nmId_val": nmId, "price": price}

            connection.execute(query, params)

            report[date] = {f"nmId_{nmId}": {"price": price}}

        connection.commit()

    return report
