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
Each application will use credentials to talk to "Teh Eye":
* "The Eye" will provide each application with their `client_id` and `secret_key`
* Each application will be responsible for generating a JWT with their credentials
and send it in the `Authentication` header as a `Bearer` token on every request.
* "The Eye" will allow CORS from any source and only validate the JWT.
