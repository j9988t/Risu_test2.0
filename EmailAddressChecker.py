import re


class EmailAddressChecker():
    def __init__(self):
        self.emailName = self.getUserInput()
        self.printUserInput()
        self.checkEmailAddress()

    def getUserInput(self):
        userInput = raw_input('Key in an email address: ')
        return userInput

    def printUserInput(self):
        print('Your email address: ' + self.emailName)

    def checkEmailAddress(self):
        if self.checkEmailMouse() == False:
            self.printEmailAddressResult(False)
            return
        emailFrag = self.splitEmailAddress()
        checkResult = (self.checkEmailLocalPart(emailFrag[0])
                       & self.checkEmailDomain(emailFrag[1]))
        self.printEmailAddressResult(checkResult)

    def checkEmailMouse(self):
        numOfMouse = len(re.findall('@', self.emailName))
        return(True if numOfMouse == 1 else False)

    def checkEmailLocalPart(self, emailLocalPart):
        ###

        return True

    def checkEmailDomain(self, emailDomain):
        ###
        return False

    def splitEmailAddress(self):
        emailFrag = []
        emailFrag = self.emailName.split('@')
        return emailFrag

    def printEmailAddressResult(self, checkResult):
        print('Your email address is ' +
              ('ACCEPTED !' if checkResult == True else 'REJECTED !'))
