from django.shortcuts import get_list_or_404
from django.shortcuts import render
from rest_framework.views import Response, Request, APIView, status
from rest_framework import viewsets
from .serializers import FileFormSerializer, TransactionSerializer
from .models import Transaction, FileForm
from utils.utils import transactions
from django.db.models import Count, Sum

class ListViewSet(viewsets.ModelViewSet):
    queryset = FileForm.objects.all()
    serializer_class = FileFormSerializer

    def create(self, request: Request, *arqs, **kwargs):
        try:
            if len(request.FILES.keys())==0:
                return Response({"message":"a file needed .txt file"},status.HTTP_400_BAD_REQUEST)
            
            file_request = request.FILES["File"].readlines()

            list_op = []

            for op in file_request:
                list_op.append(op.decode('utf-8').rstrip())
            
            op_return = []

            for op_save in list_op:
                value = int(op_save[9:19])/100

                operation={
                    "tipo":op_save[0:1],
                    "data":f"{op_save[7:9]}/{op_save[5:7]}/{op_save[1:5]}",
                    "valor": value,
                    "cpf": op_save[19:30],
                    "cartao": op_save[30:42],
                    "hora":f"{op_save[42:44]}:{op_save[44:46]}:{op_save[46:48]}",
                    "dono_da_loja":op_save[48:62].strip(),
                    "nome_loja":op_save[62:80],
                }

                serializer=TransactionSerializer(data=operation)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                op_return.append(operation)

            serializer = self.get_serializer(data=request.FILES)
            serializer.is_valid(raise_exception=True,)
            serializer.save()

            return Response(op_return,status.HTTP_201_CREATED)
        
        except ValueError:
            return Response({"message":"you need to select a valid file CNAB.txt"},status.HTTP_400_BAD_REQUEST)

class ListDetailView(APIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self,request:Request) :
        
        stores = Transaction.objects.values("nome_loja").annotate(the_count=Count("valor"))
        balance = []
        for store in stores:
            name = store["nome_loja"]
            total_sum = Transaction.objects.filter(
                nome_loja=store["nome_loja"],
                tipo=["1","4","5","6","7","8"],
            ).aggregate(Sum("valor"))
            total_sub = Transaction.objects.filter(
                nome_loja=store["nome_loja"], tipo=["2","3","9"]
            ).aggregate(Sum("valor"))

            if not total_sum["valor__sum"]:
                total_sum["valor__sum"] = 0
            if not total_sub["valor__sum"]:
                total_sub["valor__sum"] = 0

            balance.append((name, total_sum["valor__sum"] - total_sub["valor__sum"]))

            return Response(balance)


