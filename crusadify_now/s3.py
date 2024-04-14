from reflex import Application, Request, Route, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
import uuid
import aiobotocore

from dotenv import dotenv_values

load = dotenv_values()


async def upload(request: Request):
    form = await request.form()
    file = form.get("file")

    if file is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No file received.")

    client_credentials = {
      "s3BucketName": load["S3_BUCKET_NAME"],
        "AWS_ACCESS_KEY_ID": load["AWS_ACCESS_KEY_ID"],
        "AWS_REGION": load["AWS_REGION"],
        "AWS_SECRET_ACCESS_KEY": load["AWS_SECRET_ACCESS_KEY"]
    },
    
    try:
        s3_service = s3_service(
            aws_access_key_id=client_credentials["aws_access_key_id"],
            aws_secret_access_key=client_credentials["aws_secret_access_key"],
            region_name=client_credentials["region_name"]
        )

        response = await s3_service.upload_to_s3('/hackathon', f'{uuid.uuid4().hex}', client_credentials["s3BucketName"], 'PUBLIC')
        
        return JSONResponse({"message": "File successfully saved", "response": response})
    except Exception as error:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(error))





class S3Service:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.session = aiobotocore.get_session()
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name

    async def upload_to_s3(self, file_path, modified_file_name, bucket_name, privacy):
        async with self.session.create_client('s3', region_name=self.region_name,
                                              aws_secret_access_key=self.aws_secret_access_key,
                                              aws_access_key_id=self.aws_access_key_id) as s3_client:
            with open(file_path, 'rb') as file_data:
                await s3_client.put_object(Bucket=bucket_name,
                                           Key=modified_file_name,
                                           Body=file_data,
                                           ACL='private' if privacy == 'PRIVATE' else 'public-read')
                return f"https://{bucket_name}.s3.{self.region_name}.amazonaws.com/{modified_file_name}"
