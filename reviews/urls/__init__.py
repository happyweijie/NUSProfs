from .reviews import urlpatterns as review_urlpatterns
from .replies import urlpatterns as reply_urlpatterns

urlpatterns = review_urlpatterns + reply_urlpatterns
