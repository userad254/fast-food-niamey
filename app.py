import os
from typing import Any, Dict, List, Optional

import stripe
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

from produits import PRODUITS

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Security configuration
app.secret_key = os.getenv("SECRET_KEY", "default-secret-key")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# App configuration
DOMAIN = os.getenv("DOMAIN", "http://localhost:5000")


@app.route("/")
def index() -> str:
    """
    Render the home page with the list of food products.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template("index.html", produits=PRODUITS)


@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session() -> Any:
    """
    Create a Stripe Checkout Session for a specific product.

    Retrieves the product ID from the form, finds the product in the local data,
    and initializes a Stripe payment session.

    Returns:
        Any: Redirects to Stripe Checkout or back to index on failure.
    """
    product_id_raw: Optional[str] = request.form.get("product_id")

    if not product_id_raw:
        return redirect(url_for("index"))

    try:
        product_id: int = int(product_id_raw)
    except ValueError:
        return redirect(url_for("index"))

    # Search for the product in the list
    product: Optional[Dict[str, Any]] = next(
        (p for p in PRODUITS if p["id"] == product_id), None
    )

    if product:
        try:
            # Initialize Stripe Checkout Session
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "unit_amount": product["price"],
                            "product_data": {
                                "name": product["name"],
                            },
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=url_for("success", _external=True),
                cancel_url=url_for("cancel", _external=True),
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            # Log error and redirect (In a real app, use flash messages)
            print(f"Stripe Error: {e}")
            return redirect(url_for("index"))

    return redirect(url_for("index"))


@app.route("/success")
def success() -> str:
    """
    Render the success page after a successful payment.

    Returns:
        str: The rendered HTML template for the success page.
    """
    return render_template("success.html")


@app.route("/cancel")
def cancel() -> str:
    """
    Render the cancel page if the user cancels the payment.

    Returns:
        str: The rendered HTML template for the cancel page.
    """
    return render_template("cancel.html")


if __name__ == "__main__":
    app.run(debug=True)