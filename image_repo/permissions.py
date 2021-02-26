from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message = "Authentication Required error."

	# def is_authenticated(self, request, view):
	# 	return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		return True if request.user == obj.owner else False