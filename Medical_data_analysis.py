import sys

print("-------Welcome to Hemoglobine Level Analyzer------!")
print()

total_patients = 0

low_hb_patient = 0
normal_hb_patient = 0
high_hb_patient = 0

patients_details = {}
with open("medical_data.txt","r") as file:
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split(",")

        name = parts[0]
        hb_level = float(parts[1])

        if hb_level < 12:
            status = "Low Hemoglobine"
            low_hb_patient += 1
            patients_details[name] = status

        elif 12 <= hb_level <= 17.5:
            status = "Normal Hemoglobine"
            normal_hb_patient+= 1
            patients_details[name] = status

        elif hb_level >= 17.5:
            status = "High Hemoglobine"
            high_hb_patient += 1 
            patients_details[name] = status

        total_patients += 1


print(f"Total pationt checked : {total_patients}.")        
print(f"Low Hemoglobin pationts : {low_hb_patient}.")      
print(f"Normal Hemoglobin pationts : {normal_hb_patient}.")      
print(f"High Hemoglobin pationts : {high_hb_patient}.")
print() 
     
       
while True:
    view_details = input("Do you want to See patients details: (yes/no): ").strip().lower()
    if view_details == "":
        print("you not enter (yes/no) plz enter (yes/no).")
        print()

    elif any(char.isdigit() for char in view_details):
        print("Plz enter only text (yes/no).Number not aloowed.")
        print()

    elif view_details == "no":
        print("thanks for using Hemoglobine level Analyzer.")
        break
    
    elif view_details == "yes":
        print()
        while True:
            print("Enter one options in below...")
            print("1.Show all patients details.")
            print("2.Show all (Normel Hemoglobine patient) details.")        
            print("3.Show all (Low Hemoglobine patient) details.")        
            print("4.Show all (High Hemoglobine patient) details.")
            print("5.Exit") 

            while True:
                try:
                    option = int(input(f"enter your option in numbers(1-5): "))
                    break
                except ValueError:
                    print(f"Enter only numbers in option you enter text.")
                    print() 
            
            if option == 1:
                print()
                s_no = 1
        
                print("---All Checked Patients Details---")
                print("-" * 40)
                for name,status in patients_details.items():
                    print(f"{s_no}.{name} : {status}.")
                    s_no += 1
                print("=" * 40)
                print()
        
            elif option == 2:
                print()
                s_no = 1
        
                print("---Pationts with Normal Hemoglobine level---")
                print("-" * 40)
                for name,status in patients_details.items():
                    if status == "Normal Hemoglobine":
                        print(f"{s_no}.{name} : {status}")
                        s_no += 1 
                print("=" * 40)
                print()  
        
            elif option == 3:
                print()
                s_no = 1
        
                print("---Patients with Low Hemoglobine level---")
                print("-" * 40)
                for name,status in patients_details.items():
                    if status == "Low Hemoglobine":
                        print(f"{s_no}.{name} : {status}")
                        s_no += 1
                print("=" * 40)
                print()  
        
            elif option == 4:
                print()
                s_no = 1
        
                print("---Patients with High Hemoglobine level---")
                print("-" * 40)
                for name,status in patients_details.items():
                    if status == "High Hemoglobine":
                        print(f"{s_no}.{name} : {status}")
                        s_no += 1 
                print("=" * 40)
                print() 
        
            elif option == 5:
                print("thanks for using Hemoglobine Level Analyzer.")
                sys.exit()
                
            else:
                print("invalid inpute")
                print()