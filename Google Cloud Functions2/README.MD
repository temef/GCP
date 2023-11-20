# Function with the Storage Trigger

### Cloud Function Entry Point: image_to_text_storage

This cloud function, with the entry point `image_to_text_storage`, is designed to be triggered when a file is uploaded to a storage bucket.

When an image with the .jpg extension is uploaded to the specified bucket, the Cloud Function is triggered. The function then downloads the image to a temporary directory, utilizes the Cloud Vision API (https://cloud.google.com/vision/docs/ocr) to detect text in the image, and subsequently uploads a text file with a .txt extension to the same bucket, containing the detected text.

## Cloud Vision API

The text detection from images is performed using the Cloud Vision API. For more details, refer to the [Cloud Vision OCR documentation](https://cloud.google.com/vision/docs/ocr).
