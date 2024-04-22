from google.cloud import secretmanager
import json

class SecretLoader:
    def __init__(self, project_id):
        self.project_id = project_id
        if project_id is None or secret_id is None or version_id is None:
            print("Some dependencies are missing.")
        else:
            print("You can go ahead and call the load_creds function.")


    def load_secret(self,secret_id, version_id, json_payload=True):
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
        # Build the resource name of the secret version.
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"
        # Access the secret version.
        response = client.access_secret_version(name=name)
        # Return the decoded payload.
        if json_payload:
            return json.loads(response.payload.data.decode('UTF-8'))
        else:
            return response.payload.data.decode('UTF-8')
