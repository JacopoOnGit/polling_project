from rest_framework.routers import DefaultRouter
from .views import PollViewSet, ChoiceViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'choices', ChoiceViewSet, basename='choice')
router.register(r'votes', VoteViewSet, basename='vote')

urlpatterns = router.urls

