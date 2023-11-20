# Cloud Function for Creating Text File

This Cloud Function, built on the second generation, is designed to be triggered by an HTTP POST request. The trigger endpoint expects a JSON body containing "fileName" and "fileContent". The function's entry-point is named `create_text_file_http`.

## Functionality

Upon receiving an HTTP POST request, the function creates a file with the specified "fileName" inside a designated bucket. The bucket name is obtained from the environment variable `BUCKET_ENV_VAR`. If the bucket does not exist, the function creates it. The contents of the file are set to the value provided in "fileContent". The response body, in JSON format, contains the "fileName", and the HTTP status code is set to 200.

## HTTP Request Format

Send an HTTP POST request to the trigger endpoint with a JSON body:

```json
{
  "fileName": "example.txt",
  "fileContent": "This is the content of the file."
}
```

## Environment Variable

Ensure that the environment variable `BUCKET_ENV_VAR` is set to the desired bucket name.

## Response

Upon successful execution, the function responds with a JSON body containing the "fileName" and an HTTP status code of 200.

Example response:

```json
{
  "fileName": "example.txt"
}
```

## Error Handling

In case of any errors during execution, the function returns an appropriate HTTP status code along with an error message in the response body.

Feel free to deploy and utilize this Cloud Function to efficiently create text files within a specified bucket.

