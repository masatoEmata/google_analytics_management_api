# json_key_name = "client_secrets_sample.json"

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class GetServiceClient:
    def get():
        json_key_name = "../common/secret/client_secrets.json"
        api_name='analytics'
        api_version='v3'
        scopes=[
            # 'https://www.googleapis.com/auth/analytics.readonly',
            'https://www.googleapis.com/auth/analytics.edit'
            ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
                json_key_name, scopes)
        service = build(api_name, api_version, credentials=credentials)
        print("get client: ", service)
        return service

if __name__ == '__main__':
    print("input JSON Key file name")
    json_key_name = input()

    GetServiceClient.get(json_key_name)


#from apiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials
#from writeCsv import WriteCsv
#
#json_key_name = "client_secrets.json"
#
#class GetServiceClient:
#
#    def iniService(api_name, api_version, scopes, key_file_location):
#
#        credentials = ServiceAccountCredentials.from_json_keyfile_name(
#                key_file_location, scopes=scopes)
#        service = build(api_name, api_version, credentials=credentials)
#
#        return service
#
#    def get():
#        # Define the auth scopes to request.
#        scope = 'https://www.googleapis.com/auth/analytics.readonly'
#
#        # Authenticate and construct service.
#        service = iniService(
#                api_name='analytics',
#                api_version='v3',
#                scopes=[scope],
#                key_file_location=json_key_name)
#
#        return service
#
#if __name__ == '__main__':
#    get()
