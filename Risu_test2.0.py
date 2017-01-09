from EmailAddressChecker import EmailAddressChecker


def main():
    # userInput = 'j9988t@hotmail.com'
    # eac = EmailAddressChecker(userInput)
    # print(eac.emailName)
    userInput = getUserInput()
    printUserInput(userInput)

    eac = EmailAddressChecker(userInput)
    eac.checkEmailAddress()


def getUserInput():
    userInput = input('Key in an email address: ')
    return userInput


def printUserInput(email):
    print('Your email address: ' + email)


if __name__ == '__main__':
    main()
