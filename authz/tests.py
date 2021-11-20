from time import time

import jwt
from django.test import TestCase
from rest_framework_simplejwt.exceptions import TokenError

from authz.models import ClientCredential
from authz.tokens import ClientCredentialsToken


class ClientCredentialTokenTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client_id = "dfa5f592-b20b-48db-9cab-241200d52b3a"
        cls.secret_key = "764185fa-ebbb-403b-9070-5d3118e49e9a"
        cls.raw_token = jwt.encode(
            payload={
                "jti": "123456789",
                "sub": cls.client_id,
                "gty": "client-credentials",
                "iat": time(),
                "exp": time() + 10000,
            },
            key=cls.secret_key,
        )

    def test_non_existent_client_credentials_fails(self):
        with self.assertRaises(TokenError):
            ClientCredentialsToken(self.raw_token)

    def test_existent_client_credentials_and_invalid_key_fails(self):
        ClientCredential.objects.create(
            name="test client", client_id=self.client_id
        )
        with self.assertRaises(TokenError):
            ClientCredentialsToken(self.raw_token)

    def test_existent_client_credentials_and_valid_key_succeeds(self):
        ClientCredential.objects.create(
            name="test client", client_id=self.client_id, secret_key=self.secret_key
        )
        token = ClientCredentialsToken(self.raw_token)
        token.verify()

        self.assertEqual(token.payload['sub'], self.client_id)
