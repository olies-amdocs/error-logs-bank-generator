class ErrorLog(object):

    def __init__(self):
        self._date = None
        self._log_level = None
        self._log_id = None
        self._log_event = None
        self._route = None
        self._transaction_id = None
        self._user_email = None
        self._package = None
        self._error_message = None

    def __str__(self):
        return 'ErrorLog [ ' +\
               '_date: ' + self.date + ', ' +\
               '_log_level: ' + self.log_level  + ', ' +\
               '_log_event: ' + self.log_event  + ', ' +\
               '_route: ' + self.route  + ', ' +\
               '_transaction_id: ' + self.transaction_id  + ', ' +\
               '_user_email: ' + self.user_email  + ', ' +\
               '_package: ' + self.package  + ', ' +\
               '_error_message: ' + self.error_message  + ', ' +\
               ' ]'
    
    def __iter__(self):
        return iter([self.date, self.log_level, self.log_id,
                     self.log_event, self.route, self.transaction_id,
                     self.user_email, self.package, self.error_message])

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
    def log_level(self):
        return self.logLevel

    @log_level.setter
    def log_level(self, value):
        self.logLevel = value

    @log_level.deleter
    def log_evel(self):
        del self.logLevel

    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value

    @log_id.deleter
    def log_id(self):
        del self._log_id

    @property
    def log_event(self):
        return self._log_event

    @log_event.setter
    def log_event(self, value):
        self._log_event = value

    @log_event.deleter
    def log_event(self):
        del self._log_event

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

