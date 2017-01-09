import re


class EmailAddressChecker():
    def __init__(self):
        self.emailName = self.getUserInput()
        self.printUserInput()
        self.checkEmailAddress()

    def getUserInput(self):
        userInput = input('Key in an email address: ')
        return userInput

    def printUserInput(self):
        print('Your email address: ' + self.emailName)

    def checkEmailAddress(self):
        if self.checkEmailMouse() is False:
            checkResult = False
        else:
            emailFrag = self.splitEmailAddress()
            emailUserName = emailFrag[0]
            emailDomainName = emailFrag[1]
            checkResult = (self.checkEmailLocalPart(emailUserName)
                           & self.checkEmailDomain(emailDomainName))

        self.printEmailAddressResult(checkResult)

    def checkEmailMouse(self):
        numOfMouse = len(re.findall('@', self.emailName))
        return(True if numOfMouse == 1 else False)

    def splitEmailAddress(self):
        emailFrag = []
        emailFrag = self.emailName.split('@')
        return emailFrag

    def checkEmailLocalPart(self, emailLocalPart):
        ###
        return True

    def checkEmailDomain(self, emailDomain):
        ###
        return False

    def printCheckResult(self, checkResult):
        print('Your email address is ', end='')
        if checkResult is True:
            print('ACCEPTED!')
        else:
            print('REJECTED!')
