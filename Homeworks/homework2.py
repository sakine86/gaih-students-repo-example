# -*- coding: utf-8 -*-
"""Homework2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSW1siDbb9xcDtwSDv8HJ-X7_1HyeMcl
"""

alı_cv={"Name":"Ali", "Surname":"Türk", "Age":25, "e-mail":"ali@gmail.com", "Job":"Lawyer", "City":"İstanbul" }
ayse_cv={"Name":"Ayşe", "Surname":"Çatal", "Age":27, "e-mail":"ayse@gmail.com", "Job":"Nurse", "City":"İstanbul" }
buse_cv={"Name":"Buse", "Surname":"Şen", "Age":33, "e-mail":"buse@gmail.com", "Job":"Teacher", "City":"Ankara" }
efe_cv={"Name":"Efe", "Surname":"Çoban", "Age":45, "e-mail":"efe@gmail.com", "Job":"Judge", "City":"Ankara" }
mert_cv={"Name":"Mert", "Surname":"Demir", "Age":36, "e-mail":"mert@gmail.com", "Job":"Doctor", "City":"İzmir" }
personal_List =[alı_cv, ayse_cv, buse_cv, efe_cv, mert_cv]
personal_Name= ["Ali","Ayşe","Buse","Efe","Mert"]

#print("Ali's CV:", alı_cv.items())
#print("Ali's CV:", alı_cv)
#print("Ayşe's CV:", ayse_cv) 
#print("Ali's CV:", buse_cv)
#print("Ali's CV:", efe_cv)
#print("Ali's CV:", mert_cv)

for i in range(0,len(personal_List)):
  print(("{} 's CV: {} ".format(personal_Name[i], personal_List[i])))