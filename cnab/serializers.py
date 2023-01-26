from rest_framework import serializers
from .models import Transaction, FileForm

class TransactionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = ["id"]

class FileFormSerializer (serializers.ModelSerializer):
    class Meta:
        model = FileForm
        fields = "__all__"

        read_only_fields = ["id"]