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


def print_data():
    for i in dis:
        print(i.get('rollno'), i.get('name'), i.get('Class'), i.get('time'), sep='\t')


@api_view(['POST', 'GET', 'DELETE'])
def homeapi(request):
    print('\n\n\n', request.method, 'method is called')
    if request.method == 'POST':
        print_data()
        return Response(
            dis
        )
    if request.method == 'DELETE':

        if request.query_params:
            print('--------------------------------')
        roli = int(request.query_params['rollno'])

        if int(request.data['rollno']):
            print("========================================")
            roli = 3
        dis.pop(3)
        return Response(dis[3])
    
    if request.method == 'GET':
        ri = int(request.query_params['rollno'])
        return Response(dis[ri])

    # print(for i in dis)
