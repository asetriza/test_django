import os
import sys
import datetime
from datetime import date

import dateparser

sys.path.append(os.getcwd())
from src.aggregation.connection import booking_get, skypidcker_get


def flights_all_get(fly_from, fly_to, date_from, date_to):
    if date_from == None:
        dtf = date.today()
        date_from = str(date.today().strftime("%d/%m/%Y")).replace("-", "/")
    if date_to == None:
        dtt = date.today() + datetime.timedelta(days=30)
        date_to = str(dtt.strftime("%d/%m/%Y")).replace("-", "/")

    if dateparser.parse(date_from) > dateparser.parse(date_to):
        return "date_to should be < date_from"

    url_params = f"flights?fly_from={fly_from}&fly_to={fly_to}&date_from={date_from}&date_to={date_to}&curr=KZT"
    return skypidcker_get(url_params)


def flight_get(booking_token, bnum, adults, children, infants, currency):

    url_params = f"check_flights?v=2&booking_token={booking_token}&bnum={bnum}&currency={currency}"

    if bnum == None:
        bnum = 1
    elif bnum < 0:
        return "Minimum number of bags is 0"
    if adults == None:
        adults = 1
    elif adults <= 0:
        return "Minimum number of adults is 1"
    if children == None:
        children = 0
    elif children < 0:
        return "Minimum number of children is 0"
    if infants == None:
        infants = 0
    elif infants < 0:
        return "Minimum number of infants is 0"
    if currency == None:
        currency = "KZT"
    elif str(currency) == "KZT" or str(currency) == "USD" or str(currency) == "EUR":
        currency = currency
    else:
        return "currency should be KZT or USD or EUR"

    pnum = adults + children + infants
    if pnum > 9:
        return "Maximum number of passengers is 9"
    elif pnum < 0:
        return "Minimum number of passengers is 1"
    elif pnum <= 9 and pnum > 0:
        url_params += f"&pnum={pnum}"

    return booking_get(url_params)
