from flask import Flask, request
import requests

app = Flask(__name__)

# =========================
# TIKTOK CONFIG
# =========================
CLIENT_KEY = "sbawqarzjnwpqvmez4"
CLIENT_SECRET = "GDqEtbSGUKMkLVgbx3SZqfWtgWJf3fRy"

REDIRECT_URI = "https://web-production-1d8f9.up.railway.app/callback"


# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():
    return "TikTok backend is running"


# =========================
# CALLBACK ROUTE
# =========================
@app.route("/callback")
def callback():

    code = request.args.get("code")

    if not code:
        return "No authorization code received"

    token_url = "https://open.tiktokapis.com/v2/oauth/token/"

    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(token_url, data=data)

    return response.text


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
