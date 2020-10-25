from abc import ABCMeta, abstractmethod

# Product

class Section(metaclass = ABCMeta):

    @abstractmethod
    def describe_the_section(self):
        pass

# Concrete Products

class InfoSection(Section):

    def describe_the_section(self):
        return "This is about the user info."

class AlbumSection(Section):

    def describe_the_section(self):
        return "The user's pics."

# Creator

class SocialNetwork(metaclass = ABCMeta):

    def __init__(self, name):
        self.sections = []
        self.name = ""
        self.create_profile(name)

    def select_sections(self, *sections):
        self.sections = sections

    def show_profile(self):
        return self.name

    # Factory Method

    @abstractmethod
    def create_profile(self, name):
        pass

# Concrete Creators

class LinkedInProfile(SocialNetwork):

    def create_profile(self, name):
        self.select_sections([InfoSection()])
        self.name = "Linkedin name => " + name

class FacebookProfile(SocialNetwork):

    def create_profile(self, name):
        self.select_sections([AlbumSection()])
        self.name = "Facebook name => " + name


# Client

if __name__ == '__main__':
    my_facebook = FacebookProfile("saman")
    my_linkedin = LinkedInProfile("saman")

    print(my_facebook.show_profile())
    print(my_linkedin.show_profile())