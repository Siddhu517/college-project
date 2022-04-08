from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('teacher_view_question/<int:pk>', views.remove_question_view,name='remove-question'),

# **** teacher dashboard section *****
path('teacher_view_student', views.teacher_view_student_view,name='teacher_view_student'),
path('teacher_view_course', views.teacher_view_course_view,name='teacher_view_course'),
path('teacher_view_question', views.teacher_view_question_view,name='teacher_view_question'),

# **** teacher_Student_section ****
path('teacher_student', views.teacher_student_view,name='teacher_student'),
path('teacher_view_student', views.teacher_view_student_view,name='teacher_view_student'),
path('teacher_view_student_marks', views.teacher_view_student_marks_view,name='teacher_view_student_marks'),
path('teacher_view_marks/<int:pk>', views.teacher_view_marks_view,name='teacher_view_marks'),
path('teacher_check_marks/<int:pk>', views.teacher_check_marks_view,name='teacher_check_marks'),


path('teacher_update_student/<int:pk>', views.teacher_update_student,name='teacher_update_student'),
]