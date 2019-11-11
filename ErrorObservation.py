class ErrorObservation(object):

    def __init__(self):
        self._date = None
        self._route = None
        self._transaction_id = None
        self._user_email = None
        self._package = None
        self._error_message = None
        self._reason = None
        self._count = 0
        
    def __iter__(self):
        return iter([self.date, self.route, self.transaction_id,
                    self.user_email, self.package, self.error_message,
                    self.reason, self.count])

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @date.deleter
    def date(self):
        del self._date
        
    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):
        self._route = value

    @route.deleter
    def route(self):
        del self._route

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @transaction_id.deleter
    def transaction_id(self):
        del self._transaction_id

    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, value):
        self._user_email = value

    @user_email.deleter
    def user_email(self):
        del self._user_email

    @property
    def package(self):
        return self._package

    @package.setter
    def package(self, value):
        self._package = value

    @package.deleter
    def package(self):
        del self._package

    @property
    def error_message(self):
        return self._error_message
    
    @error_message.setter
    def error_message(self, value):
        self._error_message = value

    @error_message.deleter
    def error_message(self):
        del self._error_message

    @property
    def reason(self):
        return self._reason
    
    @reason.setter
    def reason(self, value):
        self._reason = value

    @reason.deleter
    def reason(self):
        del self._reason

    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, value):
        self._count = value

    @count.deleter
    def count(self):
        del self._count

    def add_count(self):
        self._count += 1
