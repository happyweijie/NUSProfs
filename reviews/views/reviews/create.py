from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ...serializers.reviews import (
    ReviewCreateSerializer, 
    ReviewDisplaySerializer, 
)

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
