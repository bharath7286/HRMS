def create_app():
    app = Flask(__name__)

    # Load environment variables
    root_dir = Path(__file__).parent.parent
    env_path = root_dir / '.env'
    if not env_path.exists():
        env_path.touch()

    load_dotenv(env_path)

    if not os.getenv('SECRET_KEY'):
        new_secret_key = secrets.token_urlsafe(32)
        set_key(env_path, 'SECRET_KEY', new_secret_key)

    app.config.from_object(Config)

    # Print the configuration to ensure values are loaded
    print("COGNITO_USERPOOL_ID:", app.config.get('COGNITO_USERPOOL_ID'))

    # Initialize Cognito
    cognito = CognitoAuth(app)
    
    # Your existing setup continues here...
    ```

This ensures that the `app.config` is populated correctly with the environment variables.

### 5. **Restart the Flask Application**:
After making the changes, stop the Flask application and start it again:

```bash
python run.py

