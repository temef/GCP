import os
import io 
from google.cloud import storage, vision
from google.cloud.exceptions import NotFound
import functions_framework

@functions_framework.cloud_event
def image_to_text_storage(cloud_event):
    
    client = storage.Client()
    vision_client = vision.ImageAnnotatorClient()
    bucket_name = cloud_event.data['bucket']
    file_name = cloud_event.data['name']

    if file_name.lower().endswith('.txt'):
        return "Done"

    path = f'/tmp/{file_name}'

    try:
        bucket = client.get_bucket(bucket_name)
    except NotFound:
        bucket = client.create_bucket(bucket_name, location="EUROPE-WEST1")

    blob = bucket.blob(file_name)
    blob.download_to_filename(path)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    

    full_text = texts[0].description
    jpg_removed = file_name.split('.jpg')[0]
    save_txt = bucket.blob(f"{jpg_removed}.txt")
    save_txt.upload_from_string(full_text)

    return "Done"