emails = input('emails :')

emails = emails.split(',')

domains = []
for email in emails:
    idx = email.find('@')
    if idx != -1:
        domain = email[idx:]
        domains.append(domain)

print(domains)