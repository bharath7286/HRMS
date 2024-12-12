from flask import Flask, redirect, url_for
from app.config import Config
import boto3
import secrets
import os
from dotenv import load_dotenv, set_key
from pathlib import Path
from app.utils.db_setup import create_tables_and_bucket

def create_app():
    app = Flask(__name__)

    # Update secret key if needed
    root_dir = Path(__file__).paren
