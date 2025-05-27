from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from config import setting
from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime


    

conf = ConnectionConfig(
    MAIL_USERNAME = setting.mail_username,
    MAIL_FROM     = setting.mail_from,
    MAIL_PASSWORD = setting.mail_password,
    MAIL_PORT     = setting.mail_port,
    MAIL_SERVER   = setting.mail_server,
    MAIL_STARTTLS = setting.mail_starttls,
    MAIL_SSL_TLS  = setting.mail_ssl_tls
)
import json
from datetime import datetime
import os

def get_conversation(host_id):
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{host_id}_{date}.json"
    filepath = os.path.join("chat_data", filename)

    try:
        with open(filepath, "r") as f:
            data_json = json.load(f)
            print(f"Loaded chat data from {filename}")
            return data_json
    except FileNotFoundError:
        print(f"❌ Chat data file not found: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"❌ Failed to decode JSON in file: {filename}")
        return []

        
        
def format_chat_transcript_html(json_str: str) -> str:
    chat_data = json.loads(json_str)
    html = ""

    for entry in chat_data:
        html += f"<p><strong>{entry['role']}:</strong> {entry['content']}</p>"

    return html

async def sendEmail(host_id,data):
    chat_data = get_conversation(host_id)
    chat_html = format_chat_transcript_html(json.dumps(chat_data))

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("inquiry_email.html")
    html_content = template.render(
        name=data['name'],
        email=data['email'],
        user_message=data['message'],
        chat_transcript= chat_html
    )
    message = MessageSchema(
        subject="User Inquiry",
        recipients=setting.inquiry_email,
        body=html_content,
        subtype="html"
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)
    return True