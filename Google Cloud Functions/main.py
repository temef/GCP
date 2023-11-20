import flask
import os
import functions_framework
from google.cloud import storage
from google.cloud.exceptions import NotFound
# from cloudevents.http import CloudEvent


@functions_framework.http
def create_text_file_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        Return the fileName in the body of the response.
        Return a HTTP status code of 200.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    
    # TODO: Add logic here
    request_json = request.get_json(silent=True)
    env_var = os.environ.get('BUCKET_ENV_VAR')
    # print(env_var, "oeee")
    if request_json and "fileName" in request_json:
        file_name = request_json["fileName"]
    if request_json and "fileContent" in request_json:
        file_content = request_json["fileContent"]
    # client = storage.Client(project='css2023-teemu')
    
    client = storage.Client()
    bucket_name = env_var
    try:
        bucket = client.get_bucket(bucket_name)
    except NotFound:
        bucket = client.create_bucket(bucket_name, location="EUROPE-WEST1")
        
    # bucket = client.create_bucket(bucket_name, location="EUROPE-WEST1")
    blob = bucket.blob(file_name)
    blob.upload_from_string(file_content)


    return flask.jsonify({"fileName": file_name}), 200
    