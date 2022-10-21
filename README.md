# main-gate

## Usage

1. Create an `input`  and an `output` folder.
2. Put audio files in `input`.
3. Put `audioFile.json` in `./main_gate/data`:

```json
{
  "01_auth": [{
    "name": "auth",
    "path": "./input/audio/01_auth/auth.wav"
  }],
  "02_id": [{
    "name": "id",
    "path": "./input/audio/02_id/id.wav"
  }],
  "02_name": [{
    "name": "name",
    "path": "./input/audio/02_name/name.wav"
  }],
  "03_aff": [{
    "name": "aff",
    "path": "./input/audio/03_aff/aff.wav"
  }],
  "04_success": [{
    "name": "success",
    "path": "./input/audio/04_success/success.wav"
  }],
  "05_open": [{
    "name": "open",
    "path": "./input/audio/05_open/open.wav"
  }]
}
```

4. Put `serviceAccount.json` in `./main_gate/data`:

```json
{
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}
```
  
5. Run python:

```bash
python3 -m main_gate
```
