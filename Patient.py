from Person import Person
class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, isfamily=False):  #symptom
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.isfamily = isfamily
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return f'{self.__first_name} {self.__surname}'
        


    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def get_surname(self):
        return self.__surname

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
