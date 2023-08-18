from employee import Employee


class Company:
    def _init_(self):
        self.employees-[]

    def add_employees(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):
        print('current employees')
        for i in self.employees:
         print(i.fname,i.lname)
    print('-------------------------------------------')

    def main():
             my_company= Company()
             employee1=Employee("Praneeth",'Mulamalla','52000')
             my_company.add_employees(employee1)
             employee2=Employee("V",'J','50000')
             my_company.add_employees(employee2)
             employee3=Employee("siri",'v','60000')
             my_company.add_employees(employee3)
             my_company.display_employees()
    main()