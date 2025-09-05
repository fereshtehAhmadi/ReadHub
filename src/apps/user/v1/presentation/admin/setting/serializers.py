from rest_framework import serializers

from src.apps.user.models import User, LibraryStaff


class CreateEmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "mobile", "first_name", "last_name", "password"]


class CreateEmployeeSerializer(serializers.ModelSerializer):
    user = CreateEmployeeUserSerializer()

    class Meta:
        model = LibraryStaff
        fields = ["user", "library"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.pop("password")
        user = User.objects.create(**user_data)
        user.set_password(password)
        employee = LibraryStaff.objects.create(user=user, **validated_data)
        return employee


class EmployeeDetailSerializer(serializers.ModelSerializer):
    user = CreateEmployeeUserSerializer()

    class Meta:
        model = LibraryStaff
        fields = ["id", "user", "library", ]


class EmployeeListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user__username")

    class Meta:
        model = LibraryStaff
        fields = ["id", "username", "library", "is_active"]


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    user = CreateEmployeeUserSerializer()

    class Meta:
        model = LibraryStaff
        fields = ["user", "library"]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            password = user_data.pop("password", None)
            user = instance.user
            for attr, value in user_data.items():
                setattr(user, attr, value)
            if password:
                user.set_password(password)
            user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance