from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class KeycloakOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super().create_user(claims)
        user.username = claims.get('preferred_username', user.username)
        user.save()
        return user

    def update_user(self, user, claims):
        user = super().update_user(user, claims)
        user.username = claims.get('preferred_username', user.username)
        user.save()
        return user