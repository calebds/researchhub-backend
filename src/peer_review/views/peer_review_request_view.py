from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated
)
from peer_review.models import PeerReviewRequest
from peer_review.serializers import PeerReviewRequestSerializer
from peer_review.permissions import IsAllowedToRequest
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.http import DELETE, POST, PATCH, PUT


class PeerReviewRequestViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = PeerReviewRequestSerializer

    @action(
        detail=False,
        methods=[POST],
        permission_classes=[IsAllowedToRequest]
    )
    def request_review(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def invite_reviewers(self):
        print('to implement')

    def accept_review_request(self):
        print('to implement')

    def decline_review_request(self):
        print('to implement')

    def accept_review(self):
        print('to implement')