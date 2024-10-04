from django.db import models


class Employee(models.Model):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.position}"


# Create employees:
# ceo = Employee.objects.create(name='John Doe', position='CEO')
# cto = Employee.objects.create(name='Jane Smith', position='CTO', manager=ceo)
# cfo = Employee.objects.create(name='Michael Green', position='CFO', manager=ceo)
# coo = Employee.objects.create(name='Sarah Miller', position='COO', manager=ceo)

# dev_manager = Employee.objects.create(name='Alice Johnson', position='Dev Manager', manager=cto)
# qa_manager = Employee.objects.create(name='David Wilson', position='QA Manager', manager=cto)

# Employee.objects.create(name='Bob Brown', position='Developer', manager=dev_manager)
# Employee.objects.create(name='Charlie Davis', position='Developer', manager=dev_manager)

# Employee.objects.create(name='Eve Taylor', position='QA Engineer', manager=qa_manager)

# operations_manager = Employee.objects.create(name='Henry Thomas', position='Operations Manager', manager=coo)
# Employee.objects.create(name='Grace Lee', position='Accountant', manager=cfo)
