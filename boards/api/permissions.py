from rest_framework.permissions import BasePermission


class IsOwnerOrMember(BasePermission):
    def has_permission(self, request, view):
        # Für die Listenansicht prüfen wir nur, ob der Benutzer authentifiziert ist
        # Die tatsächliche Filterung der Boards erfolgt in der View
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Prüfe, ob der Benutzer der Besitzer oder ein Mitglied ist
        return obj.owner_id == request.user or request.user in obj.members.all()


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner_id == request.user
