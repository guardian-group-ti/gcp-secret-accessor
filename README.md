# gcp-secret-accessor
A public repo to make accessing GCP secrets easier.

To install, please use the following command with the appropriate arguments filled out

`%pip install --quiet --upgrade git+https://github.com/guardian-group-ti/gcp-secret-accessor.git`

## Example usage

```python
from gcp_secret_accessor import secret_loader # imports secret loader
db_secret = secret_loader.SecretLoader(PROJECT_ID).load_secret(secret_id, version_id)
```
