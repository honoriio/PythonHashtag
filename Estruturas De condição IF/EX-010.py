emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

email = input('Informe o email: ')
if email in emails_spam:
    print('O email informado e um email de spam')
else:
    print('Email Liberado.')