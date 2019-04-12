__author__ = 'HuangyiLi'
__date__ = '2019-04-05 22:07'
from django.conf.urls import url
from django.urls import path
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView , OrgTeacherView,AddFavView,TeacherListView,TeacherDetailView

urlpatterns = [
    path('list/', OrgView.as_view(),name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    path('home/<int:pk>/', OrgHomeView.as_view(), name="org_home"),
    path('course/<int:pk>/', OrgCourseView.as_view(), name="org_course"),
    path('desc/<int:pk>/', OrgDescView.as_view(), name="org_desc"),
    path('org_teacher/<int:pk>/', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
    # 讲师列表页
    path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    # 讲师详情页
    path('teacher/detail/<int:pk>/', TeacherDetailView.as_view(), name="teacher_detail"),

]