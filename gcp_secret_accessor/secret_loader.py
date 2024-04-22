from google.cloud import secretmanager
import json

class SecretLoader:

    def load_secret(self,project_id, secret_id, version_id):
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
        # Build the resource name of the secret version.
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
        # Access the secret version.
        response = client.access_secret_version(name=name)
        # Return the decoded payload.
        secret = json.loads(response.payload.data.decode('UTF-8'))
        return secret