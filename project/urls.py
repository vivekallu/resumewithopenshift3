from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from openshiftapp import views as views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),

     url(r'^$', 'views.home', name='home'),
    url(r'^sendemail$', 'views.sendemail'),
    url(r'^quantcast$', 'views.quantcast'),
    url(r'^zynga$', 'views.zynga'),
    #url(r'^choice$', 'views.choice'),
    url(r'^paypal$', TemplateView.as_view(template_name="home/paypal.html")),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^choice$', TemplateView.as_view(template_name="home/choice.html")),
    url(r'^applovin$', TemplateView.as_view(template_name="home/applovin.html")),
    url(r'^StreetEasy$', TemplateView.as_view(template_name="home/streeteasy.html")),
    url(r'^DassaultSystemes$', TemplateView.as_view(template_name="home/ds.html")),
    url(r'^MassIT$', TemplateView.as_view(template_name="home/massit.html")),
    url(r'^BlackBoard$', TemplateView.as_view(template_name="home/blackboard.html")),
    url(r'^LexisNexis$', TemplateView.as_view(template_name="home/lexis.html")),
    url(r'^IBM$', TemplateView.as_view(template_name="home/ibm.html")),
    url(r'^Intel$', TemplateView.as_view(template_name="home/intel.html")),
    url(r'^vmware$', TemplateView.as_view(template_name="home/vmware.html")),
    url(r'^HireVue$', TemplateView.as_view(template_name="home/hirevue.html")),
    url(r'^Sprint$', TemplateView.as_view(template_name="home/sprint.html")),
    url(r'^Capgemini$', TemplateView.as_view(template_name="home/capgemini.html")),
    url(r'^Qualcomm$', TemplateView.as_view(template_name="home/qualcomm.html")),
    url(r'^HedvigInc$', TemplateView.as_view(template_name="home/hedviginc.html")),
    url(r'^CoreOS$', TemplateView.as_view(template_name="home/coreos.html")),

]
