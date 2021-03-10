import terminusdb_client as woql
from terminusdb_client import WOQLQuery
import sys

db_id = "student"
client = woql.WOQLClient(server_url = "https://127.0.0.1:6363", insecure=True)
client.connect(key="root", account="admin", user="admin")
client.db(db_id)


WOQLQuery().insert("stu002", "scm:student") \
    .property("scm:name", "Bob") \
    .execute(client, "Adding Bob.")

