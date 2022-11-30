from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

# Create your views here.
dis = [dict(),
       dict(rollno=1, name='Akshay', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=2, name='Pratham', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=3, name='adesh', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=4, name='rohan', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=5, name='modi', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=6, name='mohan', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=7, name='radha', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=8, name='kashif', Class='co5i', time=str(datetime.datetime.now())),
       dict(rollno=9, name='sahil', Class='co5i', time=str(datetime.datetime.now())),
       ]


@api_view(['POST', 'GET'])
def homeapi(request):
    if request.method == 'POST':
        print('POST method is called')
        return Response(
            dis
        )
    if request.method == 'GET':
        ri = int(request.query_params['rollno'])
        return Response(dis[ri])
    for i in dis:
        print(i.get('rollno'), i.get('name'), i.get('Class'), i.get('time'), sep='\t')
    # print(for i in dis)
    return Response(
        dis
    )
