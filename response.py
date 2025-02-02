from validator_collection import validators

def main():
    email = input("what's your email address ? ")
    try:
        email_cheak = validators.email(email)
        print("valid")
    except :
        print("invalid")
if __name__ == "__main__":
    main()
