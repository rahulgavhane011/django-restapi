from student.viewsets import StudentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Student', StudentViewset)