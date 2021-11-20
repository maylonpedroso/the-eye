from jwt.api_jwt import decode_complete as decode_token
from rest_framework_simplejwt.exceptions import TokenBackendError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.backends import TokenBackend

from authz.models import ClientCredential


class ClientTokenBackend(TokenBackend):
    def get_verifying_key(self, token):
        unverified = decode_token(token, options={"verify_signature": False})
        try:
            client = ClientCredential.objects.get(
                client_id=unverified['payload'][api_settings.USER_ID_CLAIM]
            )
        except (KeyError, ClientCredential.DoesNotExist):
            raise TokenBackendError
        else:
            return str(client.secret_key)


class ClientCredentialsToken(AccessToken):
    token_type = 'client-credentials'

    def get_token_backend(self):
        if not self._token_backend:
            self._token_backend = ClientTokenBackend(
                api_settings.ALGORITHM,
            )
        return self._token_backend
