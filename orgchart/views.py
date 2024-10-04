from django.shortcuts import render

from .models import Employee


def org_chart(request):
    employees = Employee.objects.all()

    # Create a dictionary to hold employees by ID for easy access
    employee_dict = {employee.id: employee for employee in employees}

    # Create a list for the tree structure
    tree = []

    # Build the hierarchy
    for employee in employees:
        if employee.manager:
            # Add this employee to their manager's children
            if not hasattr(employee_dict[employee.manager.id], "children"):
                employee_dict[employee.manager.id].children = []
            employee_dict[employee.manager.id].children.append(employee)
        else:
            # This employee is at the top level (no manager)
            tree.append(employee)

    context = {"employees": tree}
    return render(request, "orgchart/org_chart.html", context)
