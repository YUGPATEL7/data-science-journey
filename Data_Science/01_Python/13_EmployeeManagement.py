print("Employee Management System")

emp_data = []
DA = 0.50
HRA = 0.10
MEDICAL  = 0.04
INSURANCE  = 0.07
PF= 0.05
G_Salary= 0
DEDUCTION=0
NET_SALARY = 0
no_of_emp = int(input('How Many Employee You Want to Add ? '))

count = 1
for i in range (no_of_emp):
    print(f"#{count}")
    Id = input("Please Enter your Id:")
    Name =input("Please Enter your Name:")
    Role  = input("Please Enter your Role :")
    Salary = int(input("Please Enter your Salary:"))
    count+=1

    da_amount  = Salary  * DA
    HRA_amount = Salary  * HRA
    MEDICAL_amount = Salary  * MEDICAL

    G_Salary = Salary  + da_amount  + HRA_amount + MEDICAL_amount
    INSURANCE_amount = G_Salary*INSURANCE
    PF_amount = G_Salary*PF
    DEDUCTION_amonut = INSURANCE_amount + PF_amount
    NET_SALARY_amount = abs(DEDUCTION_amonut - G_Salary)
    emp_info= {
        "Id":Id,
        "Name":Name,
        "Role":Role,
        "Salary":Salary,
        "DA":da_amount,
        "HRA":HRA_amount,
        "MEDICAL":MEDICAL_amount,
        "G_Salary":G_Salary,
        "INSURANCE":INSURANCE_amount,
        "PF":PF_amount,
        "DEDUCTION":DEDUCTION_amonut,
        "NET_SALARY":NET_SALARY_amount
    }
    emp_data.append(emp_info)

print("===========================================================")
print("No\tEmpId\tName\tRole\tSalary\tDA\tHRA\tMEDICAL\tG_Salary\tINSURANCE\tPF\tDEDUCTION\tNET_SALARY")
count = 1
for data in emp_data:
    print(
        f"{count}\t"
        f"{data['Id']}\t"
        f"{data['Name']}\t"
        f"{data['Role']}\t"
        f"{data['Salary']}\t"
        f"{data['DA']}\t"
        f"{data['HRA']}\t"
        f"{data['MEDICAL']}\t"
        f"{data['G_Salary']}\t"
        f"{data['INSURANCE']}\t"
        f"{data['PF']}\t"
        f"{data['DEDUCTION']}\t"
        f"{data['NET_SALARY']}"
    )
    count+=1
print("===========================================================")


# No	EmpId	Name	B.Salary	DA	    HRA	    MEDIAL 	G.Salary	INSURANCE	PF	Deduction	N.Salary
# 1	    12	    MAYUR	10000		5000	1000	400	    16400		1148		820	1968		14432
# 2	    122	    KEYA	10000		5000	1000	400	    16400		1148		820	1968		14432
# 3	    22	    DHRUVI	10000		5000	1000	400	    16400		1148		820	1968		14432