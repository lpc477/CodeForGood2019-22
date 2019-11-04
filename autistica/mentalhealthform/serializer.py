# serializers.py
from rest_framework import serializers

from .models import MHFormData

class MHFormDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MHFormData
        fields = ('formID','username','depression','anxiety','stress','date',
            'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12'
            ,'q13','q14','q15','q16','q17','q18','q19','q20','q21')
