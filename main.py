import csv
from fastapi import FastAPI
from pydantic import BaseModel

# app = FastAPI()


def kk31():
    with open('menu_hours.csv') as file_obj:
        reader_obj = csv.reader(file_obj)
        data = [("store_id", "uptime_last_hour(in minutes)", "uptime_last_day(in hours)", "update_last_week(in hours)", "downtime_last_hour(in minutes)", "downtime_last_day(in hours)", "downtime_last_week(in hours)")]
        # with open('business_hours.csv') as file_obj1:
        #     reader_obj1 = csv.reader(file_obj1)
        for row in reader_obj:
            kk311 = (row[0], row[3][3]+row[3][4], row[2][0]+row[2][1])
            print(kk311)

kk31()


# with open('business_hours.csv') as file_obj:
#     reader_obj = csv.reader(file_obj)
#
#     # Iterate through each row
#     # for row in reader_obj:
#     #     print(row)
#
# with open('menu_hours.csv') as file_obj:
#     reader_obj = csv.reader(file_obj)
#
#     # Iterate through each row
#     # for row in reader_obj:
#     #     print(row)
#
#
# class Rep(BaseModel):
#     report_id: int
#
#
# @app.post("/get_report")
# def get_report(rep: Rep):
#     return {"Hello": "World"}