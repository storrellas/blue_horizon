from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

import terminusdb_client as woql
from terminusdb_client import WOQLQuery

db_id = "student"
client = woql.WOQLClient(server_url = "https://127.0.0.1:6363", insecure=True)
client.connect(key="root", account="admin", user="admin")
client.db(db_id)


class StudentAPIView(APIView):
    """
    Create Student API
    """
    def post(self, request, *args, **kwargs):


        WOQLQuery().insert("stu002", "scm:student") \
            .property("scm:name", request.data['name']) \
            .execute(client)

        # Generate response
        return Response({'message':'ok'})