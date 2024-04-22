from google.cloud import secretmanager
import json

class SecretLoader:
    def __init__(self, project_id, secret_id, version_id):
        self.project_id = project_id
        self.secret_id = secret_id
        self.version_id = version_id
        if project_id is None or secret_id is None or version_id is None:
            print("Some dependencies are missing.")
        else:
            print("You can go ahead and call the load_creds function.")


    def load_creds(self):
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
        # Build the resource name of the secret version.
        name = f"projects/{self.project_id}/secrets/{self.secret_id}/versions/{self.version_id}"
        # Access the secret version.
        response = client.access_secret_version(name=name)
        # Return the decoded payload.
        snowflake_creds = json.loads(response.payload.data.decode('UTF-8'))
        return snowflake_creds