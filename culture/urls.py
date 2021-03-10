from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from culture_content.views import *
from course.views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('accounts/', include(('django.contrib.auth.urls','django.contrib.auth'), namespace='auth'), name="signin"),
    path('accounts/password_change/',TemplateView.as_view(template_name="registration/password_change_form.html"), name="password_change"),
    path('password-done', TemplateView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),
    path('grappelli/', include('grappelli.urls')),
    #path('password_reset/', auth_views.password_reset, name='password_reset'),
	 # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
	#	path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('request-user/', request_user, name='request-user'),

		path('password_reset/',auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
		path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
		path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
		path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('mod/<str:lang>/', get_modules, name='modules'),
    path('top/<int:top_id>/', get_topic_scenarios, name='topic-scenarios'),
    path('scenario/<int:scenario_id>/', get_scenario_detail, name='scenario'),
    path('course_results/<int:course_id>/', get_user_responses_in_course, name='responses_course'),
    path('save_response/<int:answer_id>/<str:response>', save_response, name='save_response'),
    path('responses/<str:lang>/', get_user_responses, name='responses'),
    path('responses/scenario/<int:scenario_id>/', get_options_results, name='responses'),
    path('course_responses/<int:course_id>/scenario/<int:scenario_id>/', get_options_results, name='course_responses'),
		path('courses/', get_courses, name='courses'),
		path('create-course/', login_required(CourseCreate.as_view()), name='create_course'),
	  path('enroll', enroll_course, name='enroll'),
		path('unenroll', remove_user_from_course, name ="unenroll"),
    path('dashboard', get_profile, name='profile'),
    path('profile', get_user_data, name='user_profile')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
