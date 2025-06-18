from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ReviewCreateSerializer, 
    ReviewDisplaySerializer, 
    ReviewUpdateSerializer, 
    ReplyCreateSerializer, 
    ReplyDisplaySerializer,
    ReplyUpdateSerializer
)
from .models import Review, Reply

User = get_user_model()

# Create your views here.

# Reviews
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Use the create serializer to validate input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

        # Use the display serializer to return enriched data
        display_serializer = ReviewDisplaySerializer(
            review, context={'request': request}
        )
        return Response(display_serializer.data, status=status.HTTP_201_CREATED)

class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own reviews
        return Review.objects.filter(user_id=self.request.user)

class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any review
        if self.request.user.is_staff:
            return Review.objects.all()
        # Only allow users to delete their own reviews
        return Review.objects.filter(user_id=self.request.user)

class ProfessorReviewsView(generics.ListAPIView):
    serializer_class = ReviewDisplaySerializer
    permission_classes = [permissions.AllowAny]

    # show latest reviews for a specific professor
    def get_queryset(self):
        prof_id = self.kwargs['prof_id']
        return Review.objects.filter(prof_id=prof_id).order_by('-timestamp')

class UserReviewListView(generics.ListAPIView):
    serializer_class = ReviewDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')  # Optional
        if username:
            user = get_object_or_404(User, username=username)
        else:
            user = self.request.user  # View own reviews

        return Review.objects.filter(user_id=user).order_by('-timestamp')

# Replies
class ReplyCreateView(generics.CreateAPIView):
    serializer_class = ReplyCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Use the create serializer to validate input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reply = serializer.save()

        # Use the display serializer to return enriched data
        display_serializer = ReplyDisplaySerializer(
            reply, context={'request': request}
        )
        return Response(display_serializer.data, status=status.HTTP_201_CREATED)

class ReplyUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ReplyUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to edit their own replies
        return Reply.objects.filter(user_id=self.request.user)

class ReplyDeleteView(generics.DestroyAPIView):
    queryset = Reply.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Staff can delete any reply
        if self.request.user.is_staff:
            return Reply.objects.all()
        # Only allow users to delete their own replies
        return Reply.objects.filter(user_id=self.request.user)

class ReplyDisplayView(generics.ListAPIView):
    serializer_class = ReplyDisplaySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return Reply.objects.filter(review_id=review_id).order_by('-timestamp')
    
# Likes
class LikeToggleView(APIView): # Generic view for toggling likes on reviews and replies
    permission_classes = [permissions.IsAuthenticated]
    model = None

    def post(self, request, pk):
        if not self.model:
            return Response({"detail": "Model not specified."}, status=500)
        
        obj = get_object_or_404(self.model, pk=pk)
        user = request.user

        if user in obj.likes.all():
            obj.likes.remove(user)
            liked = False
        else:
            obj.likes.add(user)
            liked = True

        return Response({
            "liked": liked, 
            "likes_count": obj.likes.count()
        }, status=status.HTTP_200_OK)
    
class ReviewLikeToggleView(LikeToggleView):
    model = Review

class ReplyLikeToggleView(LikeToggleView):
    model = Reply
