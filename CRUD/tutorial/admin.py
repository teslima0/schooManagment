from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,StudentResult, SessionYearModel, AdminHOD,Attendance,LeaveReportStaff,LeaveReportStudent, AttendanceReport,Subjects, Students, Courses,Staffs,FeedBackStaffs,FeedBackStudent,NotificationStaffs,NotificationStudent


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(SessionYearModel)
admin.site.register(LeaveReportStaff)
admin.site.register(LeaveReportStudent)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(FeedBackStaffs)
admin.site.register(FeedBackStudent)
admin.site.register(NotificationStaffs)
admin.site.register(NotificationStudent)
admin.site.register(StudentResult)