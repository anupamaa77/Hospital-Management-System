from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):   
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')  #prints out the items in list numbered

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1   changed
        if username == self.__username and password == self.__password:
            print('You are logged in!')
            return True
        else:
            return False
    
        

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2  changed 
        first_name = input('Enter the first name of the doctor: ')
        surname = input('Enter the surname of the doctor: ')
        speciality = input('Enter the speciality of the doctor: ')
        return first_name, surname, speciality
    
    def group_patients(self, patients):
        s_family=[]
        for patient in patients:
            if (patient.get_surname() == "Smith"):
                s_family.append(str(patient))
        self.view(s_family)

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3  changed 
        op = input('Choose an option: ')
    

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4   changed
            doctor_first_name, doctor_surname, doctor_speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if doctor_first_name == doctor.get_first_name() and doctor_surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    #ToDo5
                    break # save time and end the loop
            # else:
            #         speciality = speciality
            #         doctors.append(Doctor(doctor_first_name,doctor_surname, speciality))

            #ToDo6
            if(name_exists == False):
              doctors.append(Doctor(doctor_first_name, doctor_surname, doctor_speciality))                                            # ... to the list of doctors
              print('Doctor info registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                #if(len(doctors)!=0):
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index,doctors)
                    if doctor_index!=False:
                        break 
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = input('Input: ') # make the user input lowercase

            #ToDo8
            # if(len(doctors)!= 0):
            try:
                if op == '1':
                  new_first_name = input('Enter the new first name: ')
                  doctors[index].set_first_name(new_first_name = new_first_name)
                  print('--Doctor info updated--')
                elif op == '2':
                  new_surname = input('Enter the new surname: ')
                  doctors[index].set_surname(new_surname = new_surname)
                  print('--Doctor info updated--')
                elif op == '3':
                  new_speciality = input('Enter the new speciality: ')
                  doctors[index].set_speciality(new_speciality = new_speciality)
                  print('--Doctor info updated--')
            except ValueError:
                print('Choose a valid option')
            except Exception as e:
                print('This ID isnot correct')

        # Delete
        elif op == '4':
            
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))

            #ToDo9
            if doctor_index == 0:
                print('The id is invalid')
            elif int(doctor_index) in range(len(doctors)+1):
                del doctors[int(doctor_index)-1]
            else:
                   print('The id entered is incorrect') 
            

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        # for index, item in enumerate(patients):
        #     print(f'{index+1:3} | {item}')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        assign = []
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        for index, item in enumerate(patients):
            print(f'{index+1:3} | {item}')

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index]  #.patients(symptom) # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        # self.view(doctors)
        for index, item in enumerate(doctors):
            print(f'{index+1:3} | {item}')
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                self.write_patientRecords(patients)
                #####
                # patient = patients[patient_index]
                # patient.link(doctor = doctors[doctor_index].full_name())
                # doctors[doctor_index].add_patient(patient)

                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)
        patient_index = int(input('Please enter the patient ID: ')) -1

        #ToDo12
        
        discharge_patients.append(patients[patient_index])
        del patients[patient_index]

        self.write_patientRecords(patients)
        print('Successfully discharged')
           
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)
    def read_patientsRecord(self):
        patient_list = []
        file_name = 'patients_details.txt'
        try:
            with open (file_name, 'r') as fd:
                for i in fd:
                    i.split(',')
        except FileNotFoundError:
            print('File does not exist')
        finally:
            return patient_list
    
    def write_patientRecords(self, patients):
        file_name = 'patients_details.txt'
        file = open(file_name, 'w')
        for patient in patients:
            s = str(patient)
            file.write(f'{s}\n')
        file.close()

    

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            self.__username = username
            print('Username updated')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print('Password updated')

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            # if address == input('Enter the address again:'):
            self.__address = address
            print('Address updated')

        else:
            #ToDo16
            print('Please choose correct option!')
    def get_management_report(self, doctors, patients):
        print('------Management Report------')
        print('Choose the operation')
        print('1 - Total doctors in the system')
        print('2 - Total patient per doctor')
        print('3 - Total number of appointments per month per doctor')
        print('4 - Total number of patients based on the illness type.')
        op = input('Choose an option: ')
        try:
            if op == '1':
                print(f'The total number of doctors: {len(doctors)}')
            elif op == '2':
                for doctor in doctors:
                        totalPatients = doctor.get_total_patients()
                        print(f"{doctor.full_name()} has {totalPatients} patients")
            elif op =='3':
                for doctor in doctors:
                        total_appointments = doctor.get_total_appointments()
                        print(f"{doctor.full_name()} has {total_appointments} this month")
                        
            elif op == '4':
                unique_symptoms = set(tuple(patient.get_symptoms()) for patient in patients)
                for symptoms in unique_symptoms:
                        total = sum(1 for patient in patients if tuple(patient.get_symptoms()) == symptoms)
                        print(f'The total number of patients with {symptoms}: {total}')
            else:
                    print("Invalid Option")    
        except Exception as e:
                print(e)
    # def group_patients(self, isfamily):
    #     s_family=[]


