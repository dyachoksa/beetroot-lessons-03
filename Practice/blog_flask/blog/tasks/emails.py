from flask_mail import Message

from blog.extensions import mail
from blog.models import User


def send_welcome_email(user: User):
    body = f"""
    Hi, {user.name}!
    
    Welcome to the BeetBlog!
    
    Thank you for registering!
    
    With best regards,
    BeetBlog Team.
    """

    html = f"""
    <h4>Hi, <em>{user.name}</em>!</h4>
    
    <h2>Welcome to the BeetBlog!</h2>
    
    <p>Thank you for registering!</p>
    
    <p>
        With best regards,<br />
        BeetBlog Team.
    </p>
    """

    msg = Message(
        subject='Welcome to BeetBlog',
        recipients=[user.email],
        body=body,
        html=html,
    )

    mail.send(msg)
