import re


class EmailAddressChecker():
    def __init__(self, emailName):
        self.emailName = emailName

    def checkEmailAddress(self):
        if self.checkEmailMouse() is False:
            checkResult = False
        else:
            emailFrag = self.getSplitedEmailAddress()
            emailUserName = emailFrag[0]
            emailDomainName = emailFrag[1]
            checkResult = (self.checkEmailLocalPart(emailUserName)
                           & self.checkEmailDomain(emailDomainName))

        self.printCheckResult(checkResult)

    def checkEmailMouse(self):
        numOfMouse = len(re.findall('@', self.emailName))
        return(True if numOfMouse == 1 else False)

    def getSplitedEmailAddress(self):
        return self.emailName.split('@')

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
