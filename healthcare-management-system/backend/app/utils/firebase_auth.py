import firebase_admin
from firebase_admin import auth, credentials

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\ayush\\OneDrive\\Desktop\\healthcare-management-system\\backend\\app\\utils\\hafza-90f6a-firebase-adminsdk-nl7hy-149b990214.json")
firebase_admin.initialize_app(cred)

def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    return user.uid

def login_user(email, password):
    # Firebase doesn't handle password authentication directly in Admin SDK
    # For production: Use Firebase Authentication Client SDKs for token generation
    return f"Simulated token for {email}"
