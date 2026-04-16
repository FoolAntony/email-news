# Email News App
This app is designed to access news about some specified topic and send them by email.

### How does it work?

The app takes data by using *<a ref="https://newsapi.org/">NewsAPI</a>*, collects them and then sends to you by title and description on a new.

#### Preparation:

1) Install *Python 3.13* and *requests 25.1.1* (in terminal: <code>pip install requests==25.1.1</code>)
2) Clone the repository: <code>git clone https://github.com/FoolAntony/email-news.git</code>
3) Open <a ref="https://github.com/FoolAntony/email-news/blob/master/main.py">main.py</a> file and modify the <code>SENDER_EMAIL</code> and <code>SENDER_EMAIL_PWD</code> with your email credentials. (Leave the brackets, modify only their content >>> <code>"example@youremail.com"</code>)
4) Update <code>RECEIVER_EMAIL</code> variable with an email you want to deliver your message to.
5) Register and create an API key for your application on *<a ref="https://newsapi.org/">NewsAPI</a>* page.
6) Copy the key and change <code>api_key</code> variable in <a ref="https://github.com/FoolAntony/email-news/blob/master/send_email.py">send_email.py</a> file.

   * *NOTE: you may also update the <code>url</code>* variable with other URLs. By using different options, these URLs may be modified with required country, language, content, etc. For more information, please refer to *<a ref="https://newsapi.org/">NewsAPI</a> page*.

7) Run the program from the terminal: <code>python ./main.py</code>
