from django.contrib import admin
from .models import Table_equipment
from .models import Equipment_detail
from .models import Borrow
from .models import Borro_order

admin.site.register(Table_equipment)
admin.site.register(Equipment_detail)
admin.site.register(Borrow)
admin.site.register(Borro_order)

