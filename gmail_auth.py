import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    creds_path = os.path.expanduser('~/.openclaw/workspace/credentials/gmail-client.json')
    token_path = os.path.expanduser('~/.openclaw/workspace/credentials/token.json')

    if not os.path.exists(creds_path):
        print(f"Error: {creds_path} not found. Please ensure the JSON file is there.")
        return

    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    creds = flow.run_local_server(port=8080, open_browser=False, bind_addr='0.0.0.0')
    
    with open(token_path, 'wb') as token:
        pickle.dump(creds, token)
        print(f"\n[SUCCESS] token.json created at {token_path}")

if __name__ == '__main__':
    main()
