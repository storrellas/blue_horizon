import terminusdb_client as woql
from terminusdb_client import WOQLQuery

"""
client = c.WOQLClient(server_url="https://127.0.0.1:6363", insecure=True)
client.connect(user="admin", account="admin", key="root", db="testdb")
carInstance = woql().insert(insert_id="OBJ123", insert_type="doc_car")
carInstance.label("Porche 911")
carInstance.property("car_make", "Porche")
carInstance.property("car_model", "911")
carInstance.execute(client)
"""
"""
client = terminusdb_client.WOQLClient(server_url="https://127.0.0.1:6363", insecure=True)
client.connect(user="admin", account="admin", key="root")
client.create_database("pybike", "Bicycle Graph")
station = WOQLQuery().doctype("Station").label("Bike Station")
journey = WOQLQuery().doctype("Journey")
journey = journey.label("Journey")
journey = journey.property("start_station", "Station").label("Start Station")
journey = journey.property("end_station", "Station").label("End Station")
schema = WOQLQuery().when(True).woql_and(station, journey)
schema.execute(client)
"""

db_id = "pybike"
client = woql.WOQLClient(server_url = "https://127.0.0.1:6363", insecure=True)
client.connect(key="root", account="admin", user="admin")


existing = client.get_database(db_id, "admin")
if existing is not None:
    client.delete_database(db_id)
client.create_database(db_id, accountid="admin", label = "Bike Graph", description = "Create a graph with bike data")

"""
if existing is None: 
    print("creating db")
    client.create_database(db_id, accountid="admin", label = "Bike Graph", description = "Create a graph with bike data")
else:
    client.db(db_id)
"""

# station_dt = WOQLQuery().doctype("doc_car",
#                     label="doc_car",
#                     description="A station where bikes are deposited")
# station_dt.execute(client, "creating schema")

# carInstance = WOQLQuery().insert(insert_id="OBJ123", insert_type="doc_car")
# carInstance.label("Porche 911")
# carInstance.property("car_make", "Porche")
# carInstance.property("car_model", "911")
# carInstance.execute(client)

WOQLQuery().doctype("scm:student").property("scm:name", "xsd:string").execute(client, "student schema created.")
WOQLQuery().insert("stu001", "scm:student").property("scm:name", "Alice").execute(client, "Adding Alice.")
WOQLQuery().insert("stu002", "scm:student").property("scm:name", "Bob").execute(client, "Adding Bob.")
client.query(WOQLQuery().star())
"""
station_dt = WOQLQuery().doctype("station",
                        label="Bike Station",
                        description="A station where bikes are deposited")
bicycle_dt = WOQLQuery().doctype("bike", label="Bicycle")
journey_dt = (
        WOQLQuery().doctype("journey", label="Journey").
        property("start_station", "Station", label="Start Station").
        property("end_station", "Station", label="End Station").
        property("duration", "integer", label="Journey Duration").
        property("start_time", "dateTime", label="Time Started").
        property("end_time", "dateTime", label="Time Ended").
        property("journey_bicycle", "Bicycle", label="Bicycle Used")
        )
schema = station_dt + bicycle_dt + journey_dt
schema.execute(client, "creating schema")
"""

#client.delete_database(db_id)