from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# 3. Pass the data back to the main.py file, so that you can print the data from main.py
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"
# 4. In main.py check if sheet_data contains any values for the "iataCode" key.
# If not, then the IATA Codes column is empty in the Google Sheet.
# In this case, pass each city name in sheet_data one-by-one to
# the FlightSearch class. For now, the FlightSearch class can
# respond with "TESTING" instead of a real IATA code. You should use the response
# from the FlightSearch class to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

#timedelta()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    ################
    if flight is None:
        continue
    ################

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message=f"Low price alert! Only {flight.price} GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"

        notification_manager.send_emails(emails, message)