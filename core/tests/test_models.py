import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_name


class GetFileNameTestCase(TestCase):

    def setUp(self):
        self.example_file_name = f'{uuid.uuid4()}.png'

    def test_get_file_name(self):
        file = get_file_name(None, 'test.png')
        self.assertTrue(len(self.example_file_name), len(file))
        self.assertEqual(file.split('.')[-1], 'png')


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service_example = mommy.make('Service')

    def test_service_str(self):
        self.assertEqual(str(self.service_example), self.service_example.service)


class RoleTestCase(TestCase):

    def setUp(self):
        self.role_example = mommy.make('Role')

    def test_role_str(self):
        self.assertEqual(str(self.role_example), self.role_example.role)


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee_example = mommy.make('Employee')

    def test_employee_str(self):
        self.assertEqual(str(self.employee_example), self.employee_example.name)
