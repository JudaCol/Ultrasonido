from config.wsgi import *
from core.erp.models import Patient


# List
# select from tabla
query = Patient.objects.all()
print(query)

# Insert
# insert into tabla
# p = Patient()
# p.first_name = 'Naren'
# p.middle_name = 'Antonio'
# p.first_lastname = 'De Los'
# p.second_lastname = 'Angeles'
# p.patient_id = 123456
# p.save()


# Edit
# p = Patient.objects.get(pk=123456)
# p.second_lastname = 'Antonia'
# p.save()

# Delete
# p = Patient.objects.get(pk=123456)
# p.delete()

# Filter
