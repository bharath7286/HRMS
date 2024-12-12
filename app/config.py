import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_REGION = 'ap-south-1'  # You can keep this or make it configurable
    USER_TABLE = 'F13_HRMS_Users'
    EMPLOYEE_TABLE = 'F13_HRMS_Employees'
    LEAVE_TABLE = 'F13_HRMS_Leaves'
    S3_BUCKET = 'f13-hrms-documents'

    # Cognito Settings (newly added)
    COGNITO_USER_POOL_ID = os.environ.get('COGNITO_USER_POOL_ID')
    COGNITO_CLIENT_ID = os.environ.get('COGNITO_CLIENT_ID')
    COGNITO_CLIENT_SECRET = os.environ.get('COGNITO_CLIENT_SECRET')
    COGNITO_REGION = os.environ.get('COGNITO_REGION', 'us-east-1')  # Default region if not set in .env
