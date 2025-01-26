from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# Landing

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

# Sign in flow

@app.route("/sign-in")
def sign_in_page():
    return render_template("sign_in_page.html")

@app.route("/forgot-password")
def forgot_password_page():
    return render_template("sign_in_page.html")

@app.route("/reset-password")
def reset_password_page():
    return render_template("sign_in_page.html")

# Sign up flow

@app.route("/sign-up-basic-information")
def sign_up_basic_information_page():
    return render_template("sign_in_page.html")

@app.route("/sign-up-delivery-instructions")
def sign_up_delivery_instructions_page():
    return render_template("sign_in_page.html")

@app.route("/sign-up-meal-preferences")
def sign_up_meal_preferences_page():
    return render_template("sign_in_page.html")

@app.route("/sign-up-payment-details")
def sign_up_payment_details_page():
    return render_template("sign_in_page.html")

# Dashboard

@app.route("/dashboard")
def dashboard_page():
    return render_template("sign_in_page.html")

# Update profile

@app.route("/update-profile-basic-information")
def update_profile_basic_information_page():
    return render_template("sign_in_page.html")

@app.route("/update-profile-delivery-instructions")
def update_profile_delivery_instructions_page():
    return render_template("sign_in_page.html")

@app.route("/update-profile-meal-preferences")
def update_profile_meal_preferences_page():
    return render_template("sign_in_page.html")

@app.route("/update-profile-payment-details")
def update_profile_payment_details_page():
    return render_template("sign_in_page.html")

@app.route("/profile-updated")
def profile_updated_page():
    return render_template("sign_in_page.html")

# Contact us

@app.route("/contact-us")
def contact_us_page():
    return render_template("sign_in_page.html")

@app.route("/contact-us-confirmation")
def contact_us_confirmation_page():
    return render_template("sign_in_page.html")

# Unsubscribe

@app.route("/account-deletion")
def account_deletion_page():
    return render_template("sign_in_page.html")

@app.route("/account-deletion-confirmation")
def account_deletion_confirmation_page():
    return render_template("sign_in_page.html")

# Profile history

@app.route("/order-history")
def order_history_page():
    return render_template("sign_in_page.html")

@app.route("/past-order")
def past_order_page():
    return render_template("sign_in_page.html")

@app.route("/review-order")
def review_order_page():
    return render_template("sign_in_page.html")

@app.route("/review-order-confirmation")
def review_order_confirmation_page():
    return render_template("sign_in_page.html")

# Terms and conditions

@app.route("/terms-and-conditions")
def terms_and_conditions_page():
    return render_template("sign_in_page.html")