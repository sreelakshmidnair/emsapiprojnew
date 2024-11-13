from rest_framework import serializers
from .models import Employee,Department
from django.contrib.auth.models import User , Group
from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.ModelSerializer):
    #creating the custom field called group name
    group_name = serializers.CharField(write_only=True,required=False)
    #write_only means the field will be used for input

    #function to create the user
    def create(self, validated_data):
        #at first remove the group name from the validated_data
        #so we have only username and password to creare the user
        group_name = validated_data.pop("group_name",None)
        #as  part of security ,encrypt the password and saveit
        validated_data['password'] = make_password(validated_data.get("password"))
        user=super(SignupSerializer,self).create(validated_data)
        #now we can add the created user to the group
        if group_name:
            group,created = Group.objects.get_or_create(name=group_name)
            #attending create a group objects with the specified group name if not exits
            user.groups.add(group) #add the user to that group
        return user #return the nwly created user


    class Meta:
        model = User
        fields = ['username','password','group_name']    
    
class LoginSerializer(serializers.ModelSerializer):
    #creating the custom field for username
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']    
    

#create serializer by inheriting modelserializer class
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: #will provide metadata to the model
        model = Department
        fields = ('DepartmentId','DepartmentName')
        

#add function for employee name validation (should be more than 4 character)
def name_validation(employee_name):
    if len(employee_name)<3:
        raise serializers.ValidationError("Name must be at least 3 chars")
    return employee_name

    #create serializer by inheriting modelserializer class
class EmployeeSerializer(serializers.ModelSerializer):
#department is  CUSTOM FIELD in this serializer
#source =departmentId says that the field should get data about
#the Dep

    Department = DepartmentSerializer(source='DepartmentId',read_only=True)
    #adding validation fn called 'name_validation' to thr field employeename
    #defining the Employeename field as custom field so that we can 
    #add the validator

    EmployeeName = serializers.CharField(max_length=200,validators=[name_validation])
    class Meta: #will provide metadata to the model

        
        model = Employee
        fields = ('EmployeeId','EmployeeName','Designation','DateOfJoining','IsActive','DepartmentId','Department')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')    #get only these two fields