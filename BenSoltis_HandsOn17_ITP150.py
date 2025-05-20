

#Hands On 17
#Ben Soltis
#ITP 150 Prof McNally

import sqlite3
print("Starting")

con = sqlite3.connect('medicaldemo.db')
cur = con.cursor()

cur.execute("""Select patientFN, patientLN, doctorFN, doctorLN FROM patient, doctor WHERE patient.doctorID = doctor.doctorID""")    
patient_doctorRecs = cur.fetchall()
for patientFN, patientLN, doctorFN, doctorLN in patient_doctorRecs:
    print(f"Patient: {patientFN} {patientLN}. Doctor: {doctorFN} {doctorLN}")

cur.execute("""SELECT patientFN, patientLN, surgeryDesc, doctorFN, doctorLN FROM patient, surgery, doctor WHERE surgery.doctorID = doctor.doctorID AND surgery.patientID = patient.patientID ORDER BY surgeryDesc""")

more_patientRecs = cur.fetchall()
for patientFN, patientLN, surgeryDesc, doctorFN, doctorLN in more_patientRecs:
    print(f"Patient: {patientFN} {patientLN}. Surgery: {surgeryDesc}. Doctor: {doctorFN} {doctorLN}")
    
cur.execute(f"Select surgeryDesc, sum(surgerycost) Cost from surgery group by surgeryDesc")
surgCosts = cur.fetchall()
total_cost = 0
for surgeryDesc, cost in surgCosts:
    print(f"Surgery: {surgeryDesc}. Cost: ${cost}\n")
    total_cost += cost
print(f"Total Cost is ${total_cost}")


con.close()
print("ending")




