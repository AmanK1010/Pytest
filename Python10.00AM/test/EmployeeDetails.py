class Employee:
    # setters
    def setEmpId(self, id):
        self.emp_id = id

    def setEmpName(self, name):
        self.emp_name = name

    def setEmpEmail(self, email):
        self.emp_email = email

    # getters
    def getEmpId(self):
        return self.emp_id

    def getEmpName(self):
        return self.emp_name

    def getEmpEmail(self):
        return self.emp_email


e1 = Employee()
e1.setEmpId(100)
e1.setEmpName("bala")
e1.setEmpEmail("bala@gmail.com")

e2 = Employee()
e2.setEmpId(200)
e2.setEmpName("mani")
e2.setEmpEmail("mani@gmail.com")

e3 = Employee()
e3.setEmpId(300)
e3.setEmpName("ram")
e3.setEmpEmail("ram@gmail.com")

l = [e1, e2, e3]
print(l[1].getEmpId())
print(l[1].getEmpName())
print(l[1].getEmpEmail())
