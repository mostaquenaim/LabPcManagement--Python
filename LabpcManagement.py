class PC : 

    def __init__(self,LAB_PCs) :
        """This method is called whenever an object of the class is created"""
        self.LAB_PCs=LAB_PCs

    def update_pc(self,pc_no):
        """This is for updating PC info such as os,status"""

        if pc_no not in self.LAB_PCs:
            print("PC number not found.")
        else:
            os = input("Installed operating system in the PC: ")
            status = input("Status: ")
            self.LAB_PCs[pc_no]["os"] = os
            self.LAB_PCs[pc_no]["status"] = status
            print("PC information updated successfully.")

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()

    def add_pc(self,pc_no=""):
        """This method is to add new PC in the lab"""
        if pc_no=="":
            pc_no = input("PC no: ")
        if pc_no in self.LAB_PCs:
            print("PC number already exists in the lab")
            print("\nChoose one\n")
            print("1. Modify existing PC")
            print("2. Remove existing PC")
            print("3. Skip")

            select = input("\nChoose one number: ")

            while select!='1' and select!='2' and select!='3':
                select=input("Choose between 1 to 3: ")

            if select == '1':
                self.update_pc(pc_no)
            elif select == '2':
                self.remove_pc(pc_no)
            elif select == '3':
                self.main()
            
        else:
            for i in pc_no:
                if i<'0' or i>'9':
                    print("\t\tPc number can only be digits\n")
                    self.main()

            os = input("The installed operating system in the PC: ")
            status = input("Status : ")
            self.LAB_PCs[pc_no] = {"os": os, "status": status}
            print("PC added successfully.")

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()
            
    def remove_pc(self,pc_no):
        """This method is for deleting a particular pc from lab"""
        if pc_no not in self.LAB_PCs:
            print("PC number not found.")
        else:
            del self.LAB_PCs[pc_no]
            print("PC removed successfully.")

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()

    def show_all_pc(self):
        """This method will show all pc info including os, status"""

        print("\n\nLab PC information\n")
        if not self.LAB_PCs:
            print("No PCs found.")
        else:
            for pc_no,pc_function in self.LAB_PCs.items():
                print(f"PC number:{pc_no}", )
                print(f"Operating system: {pc_function['os']}" )
                print(f"Status: {pc_function['status']}")
                print()

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()

    def show_pc(self):
        """This is for displaying info of a particular PC"""
        print("\nSearch for a PC info\n")
        pc_number = input("Enter PC number: ")
        if pc_number in self.LAB_PCs:
            for pc_no,pc_function in self.LAB_PCs.items():
                if pc_no==pc_number:
                    print(f"PC number:{pc_no}", )
                    print(f"Operating system: {pc_function['os']}" )
                    print(f"Status: {pc_function['status']}")
                    print()
        else:
            print("\nPC not found.")
        
        m=input("\n\nPress 0 to go back to Menu: ")
        if m=='0':
            self.main()

    def show_functionality(self):
        """This shows a specific function of a particular pc"""
        print("\nSee functionality of a PC\n")
        pc_number = input("Enter PC number: ")
        if pc_number not in self.LAB_PCs:
            print("\nPC not found.")
            print(f"Do you want to add PC no. {pc_number}?")
            print("1. Yes\t 2.No")
            yOn=int(input("Select 1 or 2: "))
            while yOn!=1 and yOn!=2:
                yOn=input("Please select 1 or 2: ")
            if yOn==1:
                self.add_pc(pc_number)
            else:
                self.main()

        else:
            fn=input("Which funtionality you want to see: ")
            fn.lower()
            if fn!='status' or fn!='os':
                fn=input("Choose either 'os' or 'status': ")
                fn.lower()

            print(f"{fn} for PC number {pc_number} is:", self.LAB_PCs[pc_number][fn])

            m=int(input("\n\nPress 0 to go back to Menu: "))
            if m==0:
                self.main()

    def store_pc(self):
        """This method is for storing all the PCs added"""
        filename=input("Your file name(add .txt): ")

        while filename[-4:]!='.txt':
            filename=input("Add .txt at the end of your file name): ")
        try:
            with open(filename, 'a') as file:
                if not self.LAB_PCs:
                    print("No PCs found.")
                else:
                    for pc_no,pc_function in self.LAB_PCs.items():
                        file.write(f"PC number:{pc_no}\n", )
                        file.writelines(f"OS:{pc_function['os']}\n", )
                        file.writelines(f"Status:{pc_function['status']}\n", )
                    #  file.write(f"Operating system: {pc_functionality[0]}" )
                        # file.write(f"Status: {pc_functionality[1]}")
                        file.write("\n")

                    print("\nAll the PCs stored in file\n")
        except FileNotFoundError: 
            print("Sorry, file not found")

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()

    def main(self):
        """This method is to display main menu"""

        print("\n\t\t****** Menu ******\n")
        print("\t\tChoose one\n")
        print("\t\t1. Add PC")
        print("\t\t2. Update PC")
        print("\t\t3. Remove PC")
        print("\t\t4. Show all PC")
        print("\t\t5. Search a PC")
        print("\t\t6. See a functionalty of a PC")
        print("\t\t7. Store PC")
        print("\t\t8. Quit")
        
        select=input("\n\nChoose one number: ")


        while select<'1' or select>'8':
            select=input("\n\nChoose between 1 to 8 please: ")

        if select=='1':
            self.add_pc()
        elif select=='2':
            select=input("Enter the PC no. you want to update: ")
            self.update_pc(select)
        elif select=='3':
            select=input("Enter the PC no. you want to remove: ")
            self.remove_pc(select)
        elif select=='4':
            self.show_all_pc()
        elif select=='5':
            self.show_pc()
        elif select=='6':
            self.show_functionality()
        elif select=='7':
            self.store_pc()
        else: 
            return 

LAB_PCs={}        
labobj=PC(LAB_PCs)


labobj.main()

