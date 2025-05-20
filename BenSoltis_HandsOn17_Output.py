Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py
Starting
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 11, in <module>
    cur.execute("select * from surgery")
sqlite3.OperationalError: no such table: surgery

= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py
Starting
[('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040'), ('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040'), ('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300'), ('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300'), ('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100'), ('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200'), ('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200'), ('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')]
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 11, in <module>
    cur.execute('''create table surgery (
sqlite3.OperationalError: table surgery already exists

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 11, in <module>
    cur.execute('''CREATE TABLE surgery (
sqlite3.OperationalError: table surgery already exists

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 11, in <module>
    cur.execute('''CREATE TABLE surgery (
sqlite3.OperationalError: table surgery already exists

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 74, in <module>
    doctorRecs = fetchall()
NameError: name 'fetchall' is not defined

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
('Back', 58000)
('Hand', 8000)
('Heart', 183000)
('Shoulder', 8000)
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
('Back', 58000)
('Hand', 8000)
('Heart', 183000)
('Shoulder', 8000)
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
('Back', 58000)
('Hand', 8000)
('Heart', 183000)
('Shoulder', 8000)
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
('Back', 58000)
('Hand', 8000)
('Heart', 183000)
('Shoulder', 8000)
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
('Back', 58000)
('Hand', 8000)
('Heart', 183000)
('Shoulder', 8000)
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 27, in <module>
    print(f"Patient {patientFN} {patientLN} Doctor: {doctorFN} {doctorLN}")
NameError: name 'patientFN' is not defined

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 26, in <module>
    for patientFN, patientLN, doctorFN, doctorLN in patientRecs:
ValueError: too many values to unpack (expected 4)

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 30, in <module>
    for patientFN, patientLN, doctorFN, doctorLN in patientRecs:
ValueError: too many values to unpack (expected 4)

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 27, in <module>
    cur.execute("""Select patientFN, patientLN, surgeryDesc, doctorFN, doctorLN FROM patient, doctor WHERE patient.doctorID = doctor.doctorID ORDER BY""")
sqlite3.OperationalError: incomplete input

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 27, in <module>
    cur.execute("""Select patientFN, patientLN, surgeryDesc, doctorFN, doctorLN FROM patient, doctor WHERE patient.doctorID = doctor.doctorID""")
sqlite3.OperationalError: no such column: surgeryDesc

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 29, in <module>
    for patientFN, patientLN, doctorFN, doctorLN in patient_doctor_recs:
NameError: name 'patient_doctor_recs' is not defined. Did you mean: 'patient_doctorRecs'?

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 30, in <module>
    print(f"Patient: {patientFN} {patientLN} Doctor: {doctorFN} {docotrLN}")
NameError: name 'docotrLN' is not defined. Did you mean: 'doctorLN'?

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Patient: Mary Walnut Doctor: Alice Earth
Patient: Joe Pecan Doctor: Jim Mercury
Patient: Ali Cashew Doctor: Jim Mercury
Patient: Frank Hazel Doctor: Aaron Saturn
Patient: Debra Almond Doctor: Sue Pluto
Patient: George Peanut Doctor: Aaron Saturn
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 32, in <module>
    cur.execute("""SELECT patientFN, patientLN, surgeryDesc, doctorFN, doctorLN FROM patient, surgery doctor WHERE surgery.doctorID = doctor.doctorID AND surgery.patientID = patient.patientID ORDER BY surgeryDesc""")
sqlite3.OperationalError: no such column: doctorFN

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Patient: Mary Walnut Doctor: Alice Earth
Patient: Joe Pecan Doctor: Jim Mercury
Patient: Ali Cashew Doctor: Jim Mercury
Patient: Frank Hazel Doctor: Aaron Saturn
Patient: Debra Almond Doctor: Sue Pluto
Patient: George Peanut Doctor: Aaron Saturn
Traceback (most recent call last):
  File "/Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py", line 35, in <module>
    for patientFN, patientLN, doctorFN, doctorLN in more_patientRecs:
ValueError: too many values to unpack (expected 4)

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Patient: Mary Walnut Doctor: Alice Earth
Patient: Joe Pecan Doctor: Jim Mercury
Patient: Ali Cashew Doctor: Jim Mercury
Patient: Frank Hazel Doctor: Aaron Saturn
Patient: Debra Almond Doctor: Sue Pluto
Patient: George Peanut Doctor: Aaron Saturn
Patient: Joe Pecan Surgery: Back Doctor: Jim Mercury
Patient: Frank Hazel Surgery: Back Doctor: Aaron Saturn
Patient: George Peanut Surgery: Back Doctor: Aaron Saturn
Patient: Mary Walnut Surgery: Hand Doctor: Alice Earth
Patient: Debra Almond Surgery: Hand Doctor: Sue Pluto
Patient: Mary Walnut Surgery: Heart Doctor: Alice Earth
Patient: Ali Cashew Surgery: Heart Doctor: Jim Mercury
Patient: Debra Almond Surgery: Shoulder Doctor: Sue Pluto
Surgery: {surgeryDesc} Cost: ${cost}
Surgery: {surgeryDesc} Cost: ${cost}
Surgery: {surgeryDesc} Cost: ${cost}
Surgery: {surgeryDesc} Cost: ${cost}
Total Cost is 257000
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
('S001', '12/09/2011', 'Heart', 96000, 'P100', 'D040')
('S999', '04/07/2012', 'Hand', 5000, 'P100', 'D040')
('S303', '10/10/2010', 'Back', 14000, 'P099', 'D300')
('S201', '11/11/2011', 'Heart', 87000, 'P200', 'D300')
('S200', '01/01/2001', 'Back', 22000, 'P300', 'D100')
('S105', '02/02/2002', 'Hand', 3000, 'P205', 'D200')
('S210', '03/03/2011', 'Shoulder', 8000, 'P205', 'D200')
('S111', '10/12/2011', 'Back', 22000, 'P400', 'D100')
('D200', 'Sue', 'Pluto', '555-1234', 'sue@pluto.com')
('D100', 'Aaron', 'Saturn', '555-1111', 'aaron@saturn.com')
('D300', 'Jim', 'Mercury', '555-2222', 'jim@mercury.com')
('D040', 'Alice', 'Earth', '555-5555', 'alice@earth.com')
('P100', 'Mary', 'Walnut', 'Ward1', '555-8888', 'D040')
('P099', 'Joe', 'Pecan', 'Ward3', '555-7777', 'D300')
('P200', 'Ali', 'Cashew', 'Ward4', '555-3333', 'D300')
('P300', 'Frank', 'Hazel', 'Ward5', '555-5050', 'D100')
('P205', 'Debra', 'Almond', 'Ward1', '555-8888', 'D200')
('P400', 'George', 'Peanut', 'Ward4', '555-3333', 'D100')
Patient: Mary Walnut Doctor: Alice Earth
Patient: Joe Pecan Doctor: Jim Mercury
Patient: Ali Cashew Doctor: Jim Mercury
Patient: Frank Hazel Doctor: Aaron Saturn
Patient: Debra Almond Doctor: Sue Pluto
Patient: George Peanut Doctor: Aaron Saturn
Patient: Joe Pecan Surgery: Back Doctor: Jim Mercury
Patient: Frank Hazel Surgery: Back Doctor: Aaron Saturn
Patient: George Peanut Surgery: Back Doctor: Aaron Saturn
Patient: Mary Walnut Surgery: Hand Doctor: Alice Earth
Patient: Debra Almond Surgery: Hand Doctor: Sue Pluto
Patient: Mary Walnut Surgery: Heart Doctor: Alice Earth
Patient: Ali Cashew Surgery: Heart Doctor: Jim Mercury
Patient: Debra Almond Surgery: Shoulder Doctor: Sue Pluto
Surgery: Back Cost: $58000
Surgery: Hand Cost: $8000
Surgery: Heart Cost: $183000
Surgery: Shoulder Cost: $8000
Total Cost is 257000
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Patient: Mary Walnut. Doctor: Alice Earth
Patient: Joe Pecan. Doctor: Jim Mercury
Patient: Ali Cashew. Doctor: Jim Mercury
Patient: Frank Hazel. Doctor: Aaron Saturn
Patient: Debra Almond. Doctor: Sue Pluto
Patient: George Peanut. Doctor: Aaron Saturn
Patient: Joe Pecan Surgery: Back. Doctor: Jim Mercury
Patient: Frank Hazel Surgery: Back. Doctor: Aaron Saturn
Patient: George Peanut Surgery: Back. Doctor: Aaron Saturn
Patient: Mary Walnut Surgery: Hand. Doctor: Alice Earth
Patient: Debra Almond Surgery: Hand. Doctor: Sue Pluto
Patient: Mary Walnut Surgery: Heart. Doctor: Alice Earth
Patient: Ali Cashew Surgery: Heart. Doctor: Jim Mercury
Patient: Debra Almond Surgery: Shoulder. Doctor: Sue Pluto
Surgery: Back. Cost: $58000
Surgery: Hand. Cost: $8000
Surgery: Heart. Cost: $183000
Surgery: Shoulder. Cost: $8000
Total Cost is 257000
ending

========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Patient: Mary Walnut. Doctor: Alice Earth
Patient: Joe Pecan. Doctor: Jim Mercury
Patient: Ali Cashew. Doctor: Jim Mercury
Patient: Frank Hazel. Doctor: Aaron Saturn
Patient: Debra Almond. Doctor: Sue Pluto
Patient: George Peanut. Doctor: Aaron Saturn
Patient: Joe Pecan Surgery: Back. Doctor: Jim Mercury
Patient: Frank Hazel Surgery: Back. Doctor: Aaron Saturn
Patient: George Peanut Surgery: Back. Doctor: Aaron Saturn
Patient: Mary Walnut Surgery: Hand. Doctor: Alice Earth
Patient: Debra Almond Surgery: Hand. Doctor: Sue Pluto
Patient: Mary Walnut Surgery: Heart. Doctor: Alice Earth
Patient: Ali Cashew Surgery: Heart. Doctor: Jim Mercury
Patient: Debra Almond Surgery: Shoulder. Doctor: Sue Pluto
Surgery: Back. Cost: $58000
Surgery: Hand. Cost: $8000
Surgery: Heart. Cost: $183000
Surgery: Shoulder. Cost: $8000
Total Cost is $257000
ending
>>> 
========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Patient: Mary Walnut. Doctor: Alice Earth
Patient: Joe Pecan. Doctor: Jim Mercury
Patient: Ali Cashew. Doctor: Jim Mercury
Patient: Frank Hazel. Doctor: Aaron Saturn
Patient: Debra Almond. Doctor: Sue Pluto
Patient: George Peanut. Doctor: Aaron Saturn
Patient: Joe Pecan Surgery: Back. Doctor: Jim Mercury
Patient: Frank Hazel Surgery: Back. Doctor: Aaron Saturn
Patient: George Peanut Surgery: Back. Doctor: Aaron Saturn
Patient: Mary Walnut Surgery: Hand. Doctor: Alice Earth
Patient: Debra Almond Surgery: Hand. Doctor: Sue Pluto
Patient: Mary Walnut Surgery: Heart. Doctor: Alice Earth
Patient: Ali Cashew Surgery: Heart. Doctor: Jim Mercury
Patient: Debra Almond Surgery: Shoulder. Doctor: Sue Pluto
Surgery: Back. Cost: $58000

Surgery: Hand. Cost: $8000

Surgery: Heart. Cost: $183000

Surgery: Shoulder. Cost: $8000

Total Cost is $257000
ending
>>> 
========================================================= RESTART: /Users/bensoltis/Desktop/ITP 150/Hands On 17/BenSoltis_HandsOn17_ITP150.py ========================================================
Starting
Patient: Mary Walnut. Doctor: Alice Earth
Patient: Joe Pecan. Doctor: Jim Mercury
Patient: Ali Cashew. Doctor: Jim Mercury
Patient: Frank Hazel. Doctor: Aaron Saturn
Patient: Debra Almond. Doctor: Sue Pluto
Patient: George Peanut. Doctor: Aaron Saturn
Patient: Joe Pecan. Surgery: Back. Doctor: Jim Mercury
Patient: Frank Hazel. Surgery: Back. Doctor: Aaron Saturn
Patient: George Peanut. Surgery: Back. Doctor: Aaron Saturn
Patient: Mary Walnut. Surgery: Hand. Doctor: Alice Earth
Patient: Debra Almond. Surgery: Hand. Doctor: Sue Pluto
Patient: Mary Walnut. Surgery: Heart. Doctor: Alice Earth
Patient: Ali Cashew. Surgery: Heart. Doctor: Jim Mercury
Patient: Debra Almond. Surgery: Shoulder. Doctor: Sue Pluto
Surgery: Back. Cost: $58000

Surgery: Hand. Cost: $8000

Surgery: Heart. Cost: $183000

Surgery: Shoulder. Cost: $8000

Total Cost is $257000
ending
