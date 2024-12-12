import os
from dotenv import load_dotenv

load_dotenv()  # This will load the environment variables from the .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_REGION = 'ap-south-1'  # This can also be set via the .env file
    USER_TABLE = 'F13_HRMS_Users'
    EMPLOYEE_TABLE = 'F13_HRMS_Employees'
    LEAVE_TABLE = 'F13_HRMS_Leaves'
    S3_BUCKET = 'f13-hrms-documents'

    # Cognito Configuration
    COGNITO_USERPOOL_ID = os.environ.get('COGNITO_USERPOOL_ID')
    COGNITO_CLIENT_ID = os.environ.get('COGNITO_CLIENT_ID')
    COGNITO_CLIENT_SECRET = os.environ.get('COGNITO_CLIENT_SECRET')
    COGNITO_REGION = os.environ.get('COGNITO_REGION')



