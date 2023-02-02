from rest_framework import permissions


# 인증된 유저가 아니라면, 조회만 가능
class IsAuthorOrReadonly(permissions.BasePermission):
    # 유저가 있고, 인증되었다면 목록 조회 및 포스팅 허용 - list 부분
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    #  해당 obj의 작성자가 아니라면 조회만 가능하게 - detail 부분
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
