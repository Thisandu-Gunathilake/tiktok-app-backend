from flask import Flask, request
import requests
import os

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
    return "TikTok backend is running <3"


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

    # =========================
    # DEBUG OUTPUT (VERY IMPORTANT)
    # =========================
    print("\nSTATUS CODE:", response.status_code)
    print("\nRESPONSE TEXT:", response.text)

    # Return response to browser
    return response.text


# =========================
# RUN APP (RAILWAY SAFE)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
