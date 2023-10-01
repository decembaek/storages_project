from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from . import serializers
from .models import Excel

import openpyxl as op


class Excels(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # 파일 업로드

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_excel = Excel.objects.all()
        serializer = serializers.ExcelSerializer(all_excel, many=True)
        return Response(serializer.data)

    def post(self, request):
        fields = [
            "a1",
            "b1",
            "c1",
            "d1",
            "e1",
            "a2",
            "b2",
            "c2",
            "d2",
            "e2",
            "a3",
            "b3",
            "c3",
            "d3",
            "e3",
        ]
        serializer = serializers.ExcelSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.FILES["excel"])
            excel = request.FILES["excel"]
            wb = op.load_workbook(rf"{excel}")  # 워크북 객체 생성(파일명 : test.xlsx)
            ws = wb.active
            excel_data = []
            for row in ws.iter_rows(min_row=1, max_col=5, max_row=3, values_only=True):
                for cell in row:
                    excel_data.append(cell)
            data_dict = dict(zip(fields, excel_data))
            serializer.save(**data_dict)
            # serializer = serializers.ExcelSerializer(excel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
