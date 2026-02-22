from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import TitanicSerializers
import joblib
import os
from django.conf import settings

scaler_path = os.path.join(settings.BASE_DIR, 'scaler_titanic (1).pkl')
model_path = os.path.join(settings.BASE_DIR, 'log_model_titanic (1).pkl')

scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

Sex = ['female']
Embarked = ['Q', 'S']

class TitanicPredict(views.APIView):
    def post(self, request):
        serializer = TitanicSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_sex = data.get('Sex')
            sex1or_0 = [1 if new_sex == i else 0 for i in Sex]

            new_embarked = data.get('Embarked')
            embarked1or_0 = [1 if new_embarked == i else 0 for i in Embarked]

            features = [data['Pclass']] + sex1or_0 + [data['Age'], data['SibSp'],
                                                      data['Parch'], data['Fare'],
                                                      data['SibParch']] + embarked1or_0
            scaled_data = scaler.transform([features])
            pred = model.predict(scaled_data)[0]

            return Response({'Predict': int(pred)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
