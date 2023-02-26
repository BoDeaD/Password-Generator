#creating password
import secrets

def create_new(lengh,characters):
    try:
        return "".join(secrets.choice(characters) for i in range(lengh))
    except IndexError:
        return "put the tick"