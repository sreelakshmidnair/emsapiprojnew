from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from .models import Department, Employee
from datetime import date
from django.urls import reverse
from .serializers import EmployeeSerializer
from rest_framework import status

# Create your tests here.
class EmployeeViewSetTest(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(DepartmentName="HR")
        self.employee = Employee.objects.create(
            EmployeeName = "Jackie Chan",
            Designation = "Kungfu Master",
            DateOfJoining = date(2024, 11, 13),
            DepartmentId = self.department,
            Contact = "China",
            IsActive = True
        )
        self.cilent = APIClient() 
    def test_employee_list(self):
        url = reverse('employee-list')
        response = self.client.get(url)

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    

    def test_employee_details(self):
        url = reverse('employee-detail', args=[self.employee.EmployeeId])
        response = self.client.get(url)

        serializer = EmployeeSerializer(self.employee)
        
        self.assertEqual(response.status_code, status
        .HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)