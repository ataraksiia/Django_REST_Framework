import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(payment):
    name = payment.paid_course if payment.paid_course else payment.paid_lesson
    stripe_product = stripe.Product.create(
        name=f"{name}",
    )
    return stripe_product.id


def create_stripe_price(amount, stripe_product_id):
    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=stripe_product_id,
    )
    return price.id


def create_stripe_session(price_id):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[
            {
                "price": price_id,
                "quantity": 1,
            }
        ],
        mode="payment",
        payment_method_types=["card"],
    )
    return session.get("id"), session.get("url")
