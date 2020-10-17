from abc import ABCMeta, abstractmethod

# Subject
class Publisher:

    def __init__(self):
        
        self.__subscribers = []
        self.__books = [] 

    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.__subscribers.remove(subscriber)

    def get_subscribers(self):
        return self.__subscribers

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.push_notification()

    def add_book(self, book):
        self.__books.append(book)

    def get_books(self):
        return self.__books

# Observer
class Subscriber(metaclass = ABCMeta):
    
    @abstractmethod
    def push_notification(self):
        pass

# Concrete Observers
class EmailSubscriber(Subscriber):

    def __init__(self, publisher):
        self.__publisher = publisher
        self.__publisher.add_subscriber(self)

    def push_notification(self):
        print("New Email: Publisher")

class SMSSubscriber(Subscriber):

    def __init__(self, publisher):
        self.__publisher = publisher
        self.__publisher.add_subscriber(self)

    def push_notification(self):
        print("New SMS: Publisher")

# Client
if __name__ == '__main__':
    pub = Publisher()
    sms_subs = SMSSubscriber(pub)
    email_subs = EmailSubscriber(pub)
    print(pub.get_subscribers())
    pub.add_book("Cookbook")
    pub.notify_subscribers()
    pub.add_book("Programming")
    pub.notify_subscribers()