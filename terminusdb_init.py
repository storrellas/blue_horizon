import terminusdb_client as woql
from terminusdb_client import WOQLQuery
import sys

db_id = "student"
client = woql.WOQLClient(server_url = "https://127.0.0.1:6363", insecure=True)
client.connect(key="root", account="admin", user="admin")


existing = client.get_database(db_id, "admin")
if existing is not None:
    client.delete_database(db_id)
client.create_database(db_id, accountid="admin", 
                        label = "Student", 
                        description = "Create a graph with student data")

WOQLQuery().doctype("scm:student").property("scm:name", "xsd:string").execute(client, "student schema created.")

WOQLQuery().insert("stu002", "scm:student") \
    .property("scm:name", "Bob") \
    .execute(client, "Adding Bob.")

