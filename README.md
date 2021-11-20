# The Eye

A service to will collect events from multiple applications, to help your org making better data-driven decisions.

### SLA
"The Eye" will be receiving, in average, ~100 events/second, so when an event is received 
it will be accepted (202) and send to a Celery queue. Processing the events asynchronously
will avoid leaving the applications hanging.

### Event model constrains
* If an event without timestamp is received "The Eye" will
attach the current one before deferring for processing.
* An event timestamp can not be from the future.
* Events are indexed by session, category, and timestamp for filtering.

### Trusted applications
Each application will use credentials to talk to "The Eye":
* "The Eye" will provide each application with their `client_id` and `secret_key`
* Each application will be responsible for generating a JWT with their credentials
and send it in the `Authentication` header as a `Bearer` token on every request.
* "The Eye" will allow CORS from any source and only validate the JWT.

## Development environment

Prerequisites:
    
* Python >= 3.7

Initialize a python virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run DB migrations:

```bash
python manage.py migrate
```

Run the project:

```bash
python manage.py runserver
```

Run Redis server for the Celery broker

```bash
docker run -d -p 6379:6379 redis:latest
```

Run a celery worker

```bash
celery -A the_eye worker
```

### Generate client credentials and API access token

Create a django admin superuser
```bash
python manage.py createsuperuser
```

Then go to the django admin and create a Client Credential
and copy the generated `client_id` and `secret_key`.

Using that credential any client can generate a valid JWT to communicate
with the API using a Bearer token.
Expected token payload:
```json
{
  "jti": "[UNIQUE TOKEN ID]",
  "gty": "client-credentials",
  "sub": "[CLIENT_ID]",
  "iat": 1516239022,
  "exp": 1516249032
}
```
The token signature uses `HS256` encryption with the credentials `secret_key`
as encryption key.
