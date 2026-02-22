from rest_framework import serializers

class TitanicSerializers(serializers.Serializer):
    Pclass = serializers.IntegerField()
    Sex = serializers.CharField(max_length=32)
    Age = serializers.IntegerField()
    SibSp = serializers.IntegerField()
    Parch = serializers.IntegerField()
    Fare = serializers.FloatField()
    SibParch = serializers.IntegerField()
    Embarked = serializers.CharField(max_length=32)
