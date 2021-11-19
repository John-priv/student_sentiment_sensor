import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
account = "studentsentimentsensor@gmail.com"
password = "stud3nts3ntim3nts3nsor"


class solution_rich:
    def __init__(self, text, list_of_tuples):
        self.text = text
        self.list_of_tuples = list_of_tuples

    def get_text(self):
        return self.text

    def get_text_link_pairs(self):
        return self.list_of_tuples


def send_email(receiver, text):
    # Create a secure SSL context
    context = ssl.create_default_context()



    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your Student Sentiment Sensor Results"
    msg['From'] = account
    msg['To'] = receiver

    html = """\
    <html>
      <head></head>
      <body>
        <p>
            {}
        </p>
      </body>
    </html>
    """.format(text)

    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(account, password)
        server.sendmail(account, receiver, msg.as_string())
        server.quit()


def email_solutions(receiver, rsolution):
    text = rsolution.get_text()
    text += '\n<ul>'
    for link_text, link_url in rsolution.get_text_link_pairs():
        text += '\n<li> <a href={}>{}</a></li>'.format(link_url,link_text)
    text += '\n</ul>'
    send_email(receiver, text)


if __name__ == '__main__':
    links = [("Google", "https://www.google.com/"),
             ("Wikipedia","https://en.wikipedia.org/wiki/Main_Page")]
    example_solution = solution_rich('Here are important websites: ', links)
    email_solutions("mmortonred@gmail.com", example_solution)

    text = example_solution.get_text()
    text += '\n<ul>'
    for link_text, link_url in example_solution.get_text_link_pairs():
        text += '\n<li> <a href={}>{}</a></li>'.format(link_url, link_text)
    text += '\n</ul>'
    print(text)
