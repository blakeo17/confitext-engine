import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")

def send_weekly_email(content):
    resend.Emails.send({
        "from": "ConfiText Engine <blake@newburyai.com>",
        "to": ["blake@newburyai.com"],
        "subject": "ConfiText – Next Week Content Plan",
        "html": f"""
        <h2>ConfiText – Weekly Content Plan</h2>
        <pre style="white-space: pre-wrap; font-family: monospace;">
        {content}
        </pre>
        """
    })
