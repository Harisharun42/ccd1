class ccd:

    total_no_emps = 0
    malleshwaram = 0
    mgroad = 0
    kormangala = 0

    cf_rate = 50
    te_rate = 35

    cf_from_kormangala = 0
    cf_from_mgroad = 0
    cf_from_malleshwaram = 0

    te_from_kormangala = 0
    te_from_mgroad = 0
    te_from_malleshwaram = 0
    

    def __init__(self, fn, ln, email, mob, sal, branch):
        self.fn = fn
        self.ln = ln
        self.email = email
        self.mob = mob
        self.sal = sal
        self.branch = branch
        ccd.total_no_emps += 1
        if self.branch == 'malleshwaram':
            ccd.malleshwaram += 1
        if self.branch == 'mgroad':
            ccd.mgroad += 1
        if self.branch == 'kormangala':
            ccd.kormangala += 1

    def sell(self, brev, num):
        if brev == "cf":
            if self.branch == "kormangala":
                ccd.cf_from_kormangala += num
            if self.branch == "mgroad":
                ccd.cf_from_mgroad += num
            if self.branch == "malleshwaram":
                ccd.cf_from_malleshwaram += num
            print(ccd.cf_rate*num)
        if brev == "te":
            if self.branch == "kormangala":
                ccd.te_from_kormangala += num
            if self.branch == "mgroad":
                ccd.te_from_mgroad += num
            if self.branch == "malleshwaram":
                ccd.te_from_malleshwaram += num
            print(ccd.te_rate*num)

    @classmethod
    def report(cls):
       print("Total No. of employees in ccd are {ccd.total_no_emps}")
       print("Total No. of employees from Kormangala ccd are {ccd.kormangala}")
       print("Total No. of employees from mgroad ccd are {ccd.mgroad}")
       print("Total No. of employees from malleshwaram ccd are {ccd.malleshwaram}")
       print("Total coffees from all the Branch",(ccd.cf_from_kormangala+ccd.cf_from_mgroad+ccd.cf_from_malleshwaram))
       print("Total Tea from all the Branch",(ccd.te_from_kormangala+ccd.te_from_mgroad+ccd.te_from_malleshwaram))

       print("Total by Selling coffees from all the Branch",((ccd.cf_from_kormangala+ccd.cf_from_mgroad+ccd.cf_from_malleshwaram)*ccd.cf_rate))
       print("Total by Selling Teas from all the Branch",((ccd.te_from_kormangala+ccd.te_from_mgroad+ccd.te_from_malleshwaram)*ccd.te_rate))

    @classmethod
    def transfer(cls, emp, tobranch):
        frombranch = emp.branch
        if( frombranch == "malleshwaram"):
            ccd.malleshwaram -= 1
        if( frombranch == "mgroad"):
            ccd.mgroad -= 1
        if( frombranch == "kormangala"):
            ccd.kormangala -= 1
        emp.branch = tobranch
        if( tobranch == "malleshwaram"):
            ccd.malleshwaram += 1
        if( tobranch == "mgroad"):
            ccd.mgroad += 1
        if( tobranch == "kormangala"):
            ccd.kormangala += 1
        
emp1 = ccd('tim','cook','tim@ccd.com', 89789, 2000, "mgroad")
print(emp1.__dict__)
##print(ccd.total_no_emps)
##print(ccd.mgroad)

emp1.sell("cf",5)
emp1.sell("te",2)

#ccd.report()
ccd.transfer(emp1, "kormangala")
#ccd.report()
print(emp1.__dict__)
