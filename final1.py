import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import simpledialog, Toplevel
from tkinter import messagebox
import pickle
import os

class Employee:
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details):
        """
        Initialize an employee object with the provided details.

        Parameters:
        - name (str): The name of the employee.
        - emp_id (str): The employee ID.
        - department (str): The department in which the employee works.
        - job_title (str): The job title of the employee.
        - basic_salary (float): The basic salary of the employee.
        - age (int): The age of the employee.
        - dob (str): The date of birth of the employee in the format 'YYYY-MM-DD'.
        - passport_details (dict): A dictionary containing passport details of the employee,
                                such as passport number, issue date, and expiration date.
                                Example: {'passport_number': 'AB123456', 'issue_date': 'YYYY-MM-DD', 'expiry_date': 'YYYY-MM-DD'}

        Returns:
        - None
        """
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

class ManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Management System")

        self.employee_btn = tk.Button(master, text="Employee", command=self.show_employee_buttons)
        self.employee_btn.pack()

        self.event_btn = tk.Button(master, text="Event", command=self.show_event_buttons)
        self.event_btn.pack()

        self.client_btn = tk.Button(master, text="Client", command=self.show_client_buttons)
        self.client_btn.pack()

        self.venue_btn = tk.Button(master, text="Venue", command=self.show_venue_buttons)
        self.venue_btn.pack()

        self.guest_btn = tk.Button(master, text="Guest", command=self.show_guest_buttons)
        self.guest_btn.pack()

    def show_employee_buttons(self):
        self.clear_buttons()
        self.add_employee_btn = tk.Button(self.master, text="Add Employee", command=self.add_employee)
        self.add_employee_btn.pack()
        self.update_employee_btn = tk.Button(self.master, text="Update Employee", command=self.update_employee)
        self.update_employee_btn.pack()
        self.delete_employee_btn = tk.Button(self.master, text="Delete Employee", command=self.delete_employee)
        self.delete_employee_btn.pack()
        self.view_employee_btn = tk.Button(self.master, text="View Employee by ID", command=self.view_employee)
        self.view_employee_btn.pack()

    def show_event_buttons(self):
        self.clear_buttons()
        self.add_event_btn = tk.Button(self.master, text="Add Event", command=self.add_event)
        self.add_event_btn.pack()
        self.update_event_btn = tk.Button(self.master, text="Update Event", command=self.update_event)
        self.update_event_btn.pack()
        self.delete_event_btn = tk.Button(self.master, text="Delete Event", command=self.delete_event)
        self.delete_event_btn.pack()
        self.view_event_btn = tk.Button(self.master, text="View Event by ID", command=self.view_event)
        self.view_event_btn.pack()

    def show_client_buttons(self):
        self.clear_buttons()
        self.add_client_btn = tk.Button(self.master, text="Add Client", command=self.add_client)
        self.add_client_btn.pack()
        self.update_client_btn = tk.Button(self.master, text="Update Client", command=self.update_client)
        self.update_client_btn.pack()
        self.delete_client_btn = tk.Button(self.master, text="Delete Client", command=self.delete_client)
        self.delete_client_btn.pack()
        self.view_client_btn = tk.Button(self.master, text="View Client by ID", command=self.view_client)
        self.view_client_btn.pack()
    def show_venue_buttons(self):
        self.clear_buttons()
        self.add_venue_btn = tk.Button(self.master, text="Add Venue", command=self.add_venue)
        self.add_venue_btn.pack()
        self.update_venue_btn = tk.Button(self.master, text="Update Venue", command=self.update_venue)
        self.update_venue_btn.pack()
        self.delete_venue_btn = tk.Button(self.master, text="Delete Venue", command=self.delete_venue)
        self.delete_venue_btn.pack()
        self.view_venue_btn = tk.Button(self.master, text="View Venue by ID", command=self.view_venue)
        self.view_venue_btn.pack()
    def show_guest_buttons(self):
        self.clear_buttons()
        self.add_guest_btn = tk.Button(self.master, text="Add Guest", command=self.add_guest)
        self.add_guest_btn.pack()
        self.update_guest_btn = tk.Button(self.master, text="Update Guest", command=self.update_guest)
        self.update_guest_btn.pack()
        self.delete_guest_btn = tk.Button(self.master, text="Delete Guest", command=self.delete_guest)
        self.delete_guest_btn.pack()
        self.view_guest_btn = tk.Button(self.master, text="View Guest by ID", command=self.view_guest)
        self.view_guest_btn.pack()
    def show_supplier_buttons(self):
        self.clear_buttons()
        self.add_supplier_btn = tk.Button(self.master, text="Add Supplier", command=self.add_supplier)
        self.add_supplier_btn.pack()
        self.update_supplier_btn = tk.Button(self.master, text="Update Supplier", command=self.update_supplier)
        self.update_supplier_btn.pack()
        self.delete_supplier_btn = tk.Button(self.master, text="Delete Supplier", command=self.delete_supplier)
        self.delete_supplier_btn.pack()
        self.view_supplier_btn = tk.Button(self.master, text="View Supplier by ID", command=self.view_supplier)
        self.view_supplier_btn.pack()


    def clear_buttons(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def add_employee(self):
        # Create a new window for adding employee
        add_window = Toplevel(self.master)
        add_window.title("Add Employee")

        # Entry fields for employee details
        tk.Label(add_window, text="Name:").grid(row=0, column=0)
        tk.Label(add_window, text="Employee ID:").grid(row=1, column=0)
        tk.Label(add_window, text="Department:").grid(row=2, column=0)
        tk.Label(add_window, text="Job Title:").grid(row=3, column=0)
        tk.Label(add_window, text="Basic Salary:").grid(row=4, column=0)
        tk.Label(add_window, text="Age:").grid(row=5, column=0)
        tk.Label(add_window, text="Date of Birth:").grid(row=6, column=0)
        tk.Label(add_window, text="Passport Details:").grid(row=7, column=0)

        name_entry = tk.Entry(add_window)
        emp_id_entry = tk.Entry(add_window)
        department_entry = tk.Entry(add_window)
        job_title_entry = tk.Entry(add_window)
        basic_salary_entry = tk.Entry(add_window)
        age_entry = tk.Entry(add_window)
        dob_entry = tk.Entry(add_window)
        passport_details_entry = tk.Entry(add_window)

        name_entry.grid(row=0, column=1)
        emp_id_entry.grid(row=1, column=1)
        department_entry.grid(row=2, column=1)
        job_title_entry.grid(row=3, column=1)
        basic_salary_entry.grid(row=4, column=1)
        age_entry.grid(row=5, column=1)
        dob_entry.grid(row=6, column=1)
        passport_details_entry.grid(row=7, column=1)

        # Function to handle adding employee when the button is clicked
        def add():
            name = name_entry.get()
            emp_id = emp_id_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            basic_salary = float(basic_salary_entry.get())
            age = int(age_entry.get())
            dob = dob_entry.get()
            passport_details = passport_details_entry.get()

            employee = Employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details)

            with open(f"{emp_id}.dat", "wb") as file:
                pickle.dump(employee, file)
            print("Employee added successfully.")
            add_window.destroy()

        # Button to add employee
        tk.Button(add_window, text="Add", command=add).grid(row=8, column=1, pady=10)

        pass
    def update_employee(self):
        # Functionality for updating employee
        emp_id = simpledialog.askstring("Update Employee", "Enter employee ID to update:")
        if emp_id:
            if os.path.exists(f"{emp_id}.dat"):
                with open(f"{emp_id}.dat", "rb") as file:
                    employee = pickle.load(file)

                # Create a new window for updating employee
                update_window = Toplevel(self.master)
                update_window.title("Update Employee")

                # Entry fields for updated employee details
                tk.Label(update_window, text="Name:").grid(row=0, column=0)
                tk.Label(update_window, text="Employee ID:").grid(row=1, column=0)
                tk.Label(update_window, text="Department:").grid(row=2, column=0)
                tk.Label(update_window, text="Job Title:").grid(row=3, column=0)
                tk.Label(update_window, text="Basic Salary:").grid(row=4, column=0)
                tk.Label(update_window, text="Age:").grid(row=5, column=0)
                tk.Label(update_window, text="Date of Birth:").grid(row=6, column=0)
                tk.Label(update_window, text="Passport Details:").grid(row=7, column=0)

                name_var = tk.StringVar(value=employee.name)
                emp_id_var = tk.StringVar(value=employee.emp_id)
                department_var = tk.StringVar(value=employee.department)
                job_title_var = tk.StringVar(value=employee.job_title)
                basic_salary_var = tk.StringVar(value=employee.basic_salary)
                age_var = tk.StringVar(value=employee.age)
                dob_var = tk.StringVar(value=employee.dob)
                passport_details_var = tk.StringVar(value=employee.passport_details)

                name_entry = tk.Entry(update_window, textvariable=name_var)
                emp_id_entry = tk.Entry(update_window, textvariable=emp_id_var, state='readonly')
                department_entry = tk.Entry(update_window, textvariable=department_var)
                job_title_entry = tk.Entry(update_window, textvariable=job_title_var)
                basic_salary_entry = tk.Entry(update_window, textvariable=basic_salary_var)
                age_entry = tk.Entry(update_window, textvariable=age_var)
                dob_entry = tk.Entry(update_window, textvariable=dob_var)
                passport_details_entry = tk.Entry(update_window, textvariable=passport_details_var)

                name_entry.grid(row=0, column=1)
                emp_id_entry.grid(row=1, column=1)
                department_entry.grid(row=2, column=1)
                job_title_entry.grid(row=3, column=1)
                basic_salary_entry.grid(row=4, column=1)
                age_entry.grid(row=5, column=1)
                dob_entry.grid(row=6, column=1)
                passport_details_entry.grid(row=7, column=1)

                # Function to handle updating employee when the button is clicked
                def update():
                    employee.name = name_var.get()
                    employee.department = department_var.get()
                    employee.job_title = job_title_var.get()
                    employee.basic_salary = float(basic_salary_var.get())
                    employee.age = int(age_var.get())
                    employee.dob = dob_var.get()
                    employee.passport_details = passport_details_var.get()

                    with open(f"{emp_id}.dat", "wb") as file:
                        pickle.dump(employee, file)
                    tk.messagebox.showinfo("Update Employee", "Employee details updated successfully.")
                    update_window.destroy()

                # Button to update employee
                tk.Button(update_window, text="Update", command=update).grid(row=8, column=1, pady=10)
            else:
                tk.messagebox.showinfo("Update Employee", "Employee not found.")

    def delete_employee(self):
    # Functionality for deleting employee
        emp_id = simpledialog.askstring("Delete Employee", "Enter employee ID to delete:")
        if emp_id:
            if os.path.exists(f"{emp_id}.dat"):
                os.remove(f"{emp_id}.dat")
                message = f"Employee with ID {emp_id} deleted successfully."
            else:
                message = f"Employee with ID {emp_id} not found."
            tk.messagebox.showinfo("Delete Employee", message)
        pass
    def view_employee(self):
    # Functionality for viewing employee
        emp_id = simpledialog.askstring("View Employee", "Enter employee ID to view:")
        if emp_id:
            if os.path.exists(f"{emp_id}.dat"):
                with open(f"{emp_id}.dat", "rb") as file:
                    employee = pickle.load(file)

                # Create a message with employee details
                message = f"Employee Details:\n"
                message += f"Name: {employee.name}\n"
                message += f"Employee ID: {employee.emp_id}\n"
                message += f"Department: {employee.department}\n"
                message += f"Job Title: {employee.job_title}\n"
                message += f"Basic Salary: {employee.basic_salary}\n"
                message += f"Age: {employee.age}\n"
                message += f"Date of Birth: {employee.dob}\n"
                message += f"Passport Details: {employee.passport_details}"

                tk.messagebox.showinfo("View Employee", message)
            else:
                tk.messagebox.showinfo("View Employee", "Employee not found.")
                pass
    def add_event(self):
        event_window = tk.Toplevel(self.master)
        event_window.title("Add Event")

        # Entry fields for event details
        tk.Label(event_window, text="Event ID:").grid(row=0, column=0)
        tk.Label(event_window, text="Event Type:").grid(row=1, column=0)
        tk.Label(event_window, text="Theme:").grid(row=2, column=0)
        tk.Label(event_window, text="Date:").grid(row=3, column=0)
        tk.Label(event_window, text="Time:").grid(row=4, column=0)
        tk.Label(event_window, text="Duration:").grid(row=5, column=0)
        tk.Label(event_window, text="Venue Address:").grid(row=6, column=0)
        tk.Label(event_window, text="Client ID:").grid(row=7, column=0)
        tk.Label(event_window, text="Guest List:").grid(row=8, column=0)
        tk.Label(event_window, text="Catering Company:").grid(row=9, column=0)
        tk.Label(event_window, text="Cleaning Company:").grid(row=10, column=0)
        tk.Label(event_window, text="Decorations Company:").grid(row=11, column=0)
        tk.Label(event_window, text="Entertainment Company:").grid(row=12, column=0)
        tk.Label(event_window, text="Furniture Supply Company:").grid(row=13, column=0)
        tk.Label(event_window, text="Invoice:").grid(row=14, column=0)

        event_id_var = tk.StringVar()
        event_type_var = tk.StringVar()
        theme_var = tk.StringVar()
        date_var = tk.StringVar()
        time_var = tk.StringVar()
        duration_var = tk.StringVar()
        venue_address_var = tk.StringVar()
        client_id_var = tk.StringVar()
        guest_list_var = tk.StringVar()
        catering_company_var = tk.StringVar()
        cleaning_company_var = tk.StringVar()
        decorations_company_var = tk.StringVar()
        entertainment_company_var = tk.StringVar()
        furniture_supply_company_var = tk.StringVar()
        invoice_var = tk.StringVar()

        event_id_entry = tk.Entry(event_window, textvariable=event_id_var)
        event_type_entry = tk.Entry(event_window, textvariable=event_type_var)
        theme_entry = tk.Entry(event_window, textvariable=theme_var)
        date_entry = tk.Entry(event_window, textvariable=date_var)
        time_entry = tk.Entry(event_window, textvariable=time_var)
        duration_entry = tk.Entry(event_window, textvariable=duration_var)
        venue_address_entry = tk.Entry(event_window, textvariable=venue_address_var)
        client_id_entry = tk.Entry(event_window, textvariable=client_id_var)
        guest_list_entry = tk.Entry(event_window, textvariable=guest_list_var)
        catering_company_entry = tk.Entry(event_window, textvariable=catering_company_var)
        cleaning_company_entry = tk.Entry(event_window, textvariable=cleaning_company_var)
        decorations_company_entry = tk.Entry(event_window, textvariable=decorations_company_var)
        entertainment_company_entry = tk.Entry(event_window, textvariable=entertainment_company_var)
        furniture_supply_company_entry = tk.Entry(event_window, textvariable=furniture_supply_company_var)
        invoice_entry = tk.Entry(event_window, textvariable=invoice_var)

        event_id_entry.grid(row=0, column=1)
        event_type_entry.grid(row=1, column=1)
        theme_entry.grid(row=2, column=1)
        date_entry.grid(row=3, column=1)
        time_entry.grid(row=4, column=1)
        duration_entry.grid(row=5, column=1)
        venue_address_entry.grid(row=6, column=1)
        client_id_entry.grid(row=7, column=1)
        guest_list_entry.grid(row=8, column=1)
        catering_company_entry.grid(row=9, column=1)
        cleaning_company_entry.grid(row=10, column=1)
        decorations_company_entry.grid(row=11, column=1)
        entertainment_company_entry.grid(row=12, column=1)
        furniture_supply_company_entry.grid(row=13, column=1)
        invoice_entry.grid(row=14, column=1)

        # Function to handle adding the event
        def add():
            # Get the values from entry fields
            event_id = event_id_var.get()
            event_type = event_type_var.get()
            theme = theme_var.get()
            date = date_var.get()
            time = time_var.get()
            duration = duration_var.get()
            venue_address = venue_address_var.get()
            client_id = client_id_var.get()
            guest_list = guest_list_var.get()
            catering_company = catering_company_var.get()
            cleaning_company = cleaning_company_var.get()
            decorations_company = decorations_company_var.get()
            entertainment_company = entertainment_company_var.get()
            furniture_supply_company = furniture_supply_company_var.get()
            invoice = invoice_var.get()

            # Create an Event object with the input values
            new_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice)

            # Save the event data using Pickle
            file_name = f"{event_id}.dat"
            with open(file_name, "wb") as file:
                pickle.dump(new_event, file)

            messagebox.showinfo

    def update_event(self):
        event_id = simpledialog.askstring("Update Event", "Enter Event ID to update:")

        if not event_id:
            messagebox.showerror("Update Event", "Event ID cannot be empty.")
            return

        # Check if the event file exists
        file_name = f"{event_id}.dat"
        if not os.path.exists(file_name):
            messagebox.showerror("Update Event", f"Event with ID {event_id} not found.")
            return

        # Load the event data from the file
        with open(file_name, "rb") as file:
            existing_event = pickle.load(file)

        # Create the update event window
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Event")

        # Entry fields for event details
        tk.Label(update_window, text="Event ID:").grid(row=0, column=0)
        tk.Label(update_window, text="Event Type:").grid(row=1, column=0)
        tk.Label(update_window, text="Theme:").grid(row=2, column=0)
        tk.Label(update_window, text="Date:").grid(row=3, column=0)
        tk.Label(update_window, text="Time:").grid(row=4, column=0)
        tk.Label(update_window, text="Duration:").grid(row=5, column=0)
        tk.Label(update_window, text="Venue Address:").grid(row=6, column=0)
        tk.Label(update_window, text="Client ID:").grid(row=7, column=0)
        tk.Label(update_window, text="Guest List:").grid(row=8, column=0)
        tk.Label(update_window, text="Catering Company:").grid(row=9, column=0)
        tk.Label(update_window, text="Cleaning Company:").grid(row=10, column=0)
        tk.Label(update_window, text="Decorations Company:").grid(row=11, column=0)
        tk.Label(update_window, text="Entertainment Company:").grid(row=12, column=0)
        tk.Label(update_window, text="Furniture Supply Company:").grid(row=13, column=0)
        tk.Label(update_window, text="Invoice:").grid(row=14, column=0)

        # Variables for entry fields
        event_id_var = tk.StringVar(update_window, value=existing_event.event_id)
        event_type_var = tk.StringVar(update_window, value=existing_event.event_type)
        theme_var = tk.StringVar(update_window, value=existing_event.theme)
        date_var = tk.StringVar(update_window, value=existing_event.date)
        time_var = tk.StringVar(update_window, value=existing_event.time)
        duration_var = tk.StringVar(update_window, value=existing_event.duration)
        venue_address_var = tk.StringVar(update_window, value=existing_event.venue_address)
        client_id_var = tk.StringVar(update_window, value=existing_event.client_id)
        guest_list_var = tk.StringVar(update_window, value=existing_event.guest_list)
        catering_company_var = tk.StringVar(update_window, value=existing_event.catering_company)
        cleaning_company_var = tk.StringVar(update_window, value=existing_event.cleaning_company)
        decorations_company_var = tk.StringVar(update_window, value=existing_event.decorations_company)
        entertainment_company_var = tk.StringVar(update_window, value=existing_event.entertainment_company)
        furniture_supply_company_var = tk.StringVar(update_window, value=existing_event.furniture_supply_company)
        invoice_var = tk.StringVar(update_window, value=existing_event.invoice)

        # Entry fields
        event_id_entry = tk.Entry(update_window, textvariable=event_id_var, state="readonly")
        event_type_entry = tk.Entry(update_window, textvariable=event_type_var)
        theme_entry = tk.Entry(update_window, textvariable=theme_var)
        date_entry = tk.Entry(update_window, textvariable=date_var)
        time_entry = tk.Entry(update_window, textvariable=time_var)
        duration_entry = tk.Entry(update_window, textvariable=duration_var)
        venue_address_entry = tk.Entry(update_window, textvariable=venue_address_var)
        client_id_entry = tk.Entry(update_window, textvariable=client_id_var)
        guest_list_entry = tk.Entry(update_window, textvariable=guest_list_var)
        catering_company_entry = tk.Entry(update_window, textvariable=catering_company_var)
        cleaning_company_entry = tk.Entry(update_window, textvariable=cleaning_company_var)
        decorations_company_entry = tk.Entry(update_window, textvariable=decorations_company_var)
        entertainment_company_entry = tk.Entry(update_window, textvariable=entertainment_company_var)
        furniture_supply_company_entry = tk.Entry(update_window, textvariable=furniture_supply_company_var)
        invoice_entry = tk.Entry(update_window, textvariable=invoice_var)

        event_id_entry.grid(row=0, column=1)
        event_type_entry.grid(row=1, column=1)
        theme_entry.grid(row=2, column=1)
        date_entry.grid(row=3, column=1)
        time_entry.grid(row=4, column=1)
        duration_entry.grid(row=5, column=1)
        venue_address_entry.grid(row=6, column=1)
        client_id_entry.grid(row=7, column=1)
        guest_list_entry.grid(row=8, column=1)
        catering_company_entry.grid(row=9, column=1)
        cleaning_company_entry.grid(row=10, column=1)
        decorations_company_entry.grid(row=11, column=1)
        entertainment_company_entry.grid(row=12, column=1)
        furniture_supply_company_entry.grid(row=13, column=1)
        invoice_entry.grid(row=14, column=1)

        # Function to handle updating the event
        def update():
            # Get the updated values from entry fields
            existing_event.event_type = event_type_var.get()
            existing_event.theme = theme_var.get()
            existing_event.date = date_var.get()
            existing_event.time = time_var.get()
            existing_event.duration = duration_var.get()
            existing_event.venue_address = venue_address_var.get()
            existing_event.client_id = client_id_var.get()
            existing_event.guest_list = guest_list_var.get()
            existing_event.catering_company = catering_company_var.get()
            existing_event.cleaning_company = cleaning_company_var.get()
            existing_event.decorations_company = decorations_company_var.get()
            existing_event.entertainment_company = entertainment_company_var.get()
            existing_event.furniture_supply_company = furniture_supply_company_var.get()
            existing_event.invoice = invoice_var.get()

            # Save the updated event data using Pickle
            with open(file_name, "wb") as file:
                pickle.dump(existing_event, file)

            messagebox.showinfo("Update Event", "Event updated successfully.")
            update_window.destroy()

        # Button to update the event
        update_button = tk.Button(update_window, text="Update", command=update)


    def delete_event(self):
        # Prompt user to enter the event ID
        event_id = simpledialog.askstring("Delete Event", "Enter Event ID to delete:")

        if not event_id:
            messagebox.showerror("Delete Event", "Event ID cannot be empty.")
            return

        # Check if the event file exists
        file_name = f"{event_id}.dat"
        if os.path.exists(file_name):
            # Delete the event file
            os.remove(file_name)
            messagebox.showinfo("Delete Event", "Event deleted successfully.")
        else:
            messagebox.showerror("Delete Event", f"Event with ID {event_id} not found.")

    def view_event(self):
        # Prompt user to enter the event ID
        event_id = simpledialog.askstring("View Event", "Enter Event ID to view:")

        if not event_id:
            messagebox.showerror("View Event", "Event ID cannot be empty.")
            return

        # Check if the event file exists
        file_name = f"{event_id}.dat"
        if os.path.exists(file_name):
            # Load the event data from the file
            with open(file_name, "rb") as file:
                event = pickle.load(file)

            # Display the event details in a message box
            event_details = f"Event ID: {event.event_id}\n" \
                            f"Event Type: {event.event_type}\n" \
                            f"Theme: {event.theme}\n" \
                            f"Date: {event.date}\n" \
                            f"Time: {event.time}\n" \
                            f"Duration: {event.duration}\n" \
                            f"Venue Address: {event.venue_address}\n" \
                            f"Client ID: {event.client_id}\n" \
                            f"Guest List: {event.guest_list}\n" \
                            f"Catering Company: {event.catering_company}\n" \
                            f"Cleaning Company: {event.cleaning_company}\n" \
                            f"Decorations Company: {event.decorations_company}\n" \
                            f"Entertainment Company: {event.entertainment_company}\n" \
                            f"Furniture Supply Company: {event.furniture_supply_company}\n" \
                            f"Invoice: {event.invoice}"

            messagebox.showinfo("Event Details", event_details)
        else:
            messagebox.showerror("View Event", f"Event with ID {event_id} not found.")
    def add_client(self):
        # Create a Toplevel window for adding client details
        add_client_window = tk.Toplevel(self.master)
        add_client_window.title("Add Client")

        # Labels and Entry fields for client details
        tk.Label(add_client_window, text="Client ID:").grid(row=0, column=0)
        tk.Label(add_client_window, text="Name:").grid(row=1, column=0)
        tk.Label(add_client_window, text="Address:").grid(row=2, column=0)
        tk.Label(add_client_window, text="Contact Details:").grid(row=3, column=0)
        tk.Label(add_client_window, text="Budget:").grid(row=4, column=0)

        client_id_var = tk.StringVar(add_client_window)
        name_var = tk.StringVar(add_client_window)
        address_var = tk.StringVar(add_client_window)
        contact_var = tk.StringVar(add_client_window)
        budget_var = tk.DoubleVar(add_client_window)

        tk.Entry(add_client_window, textvariable=client_id_var).grid(row=0, column=1)
        tk.Entry(add_client_window, textvariable=name_var).grid(row=1, column=1)
        tk.Entry(add_client_window, textvariable=address_var).grid(row=2, column=1)
        tk.Entry(add_client_window, textvariable=contact_var).grid(row=3, column=1)
        tk.Entry(add_client_window, textvariable=budget_var).grid(row=4, column=1)

        # Function to handle adding client
        def add():
            client_id = client_id_var.get()
            name = name_var.get()
            address = address_var.get()
            contact_details = contact_var.get()
            budget = budget_var.get()

            # Create a Client object
            new_client = Client(client_id, name, address, contact_details, budget)

            # Save the client data using Pickle
            file_name = f"{client_id}.dat"
            with open(file_name, "wb") as file:
                pickle.dump(new_client, file)

            messagebox.showinfo("Add Client", "Client added successfully.")
            add_client_window.destroy()

        # Button to add client
        add_button = tk.Button(add_client_window, text="Add", command=add)
        add_button.grid(row=5, columnspan=2)

    def update_client(self):
        # Prompt user to enter the client ID
        client_id = simpledialog.askstring("Update Client", "Enter Client ID to update:")

        if not client_id:
            messagebox.showerror("Update Client", "Client ID cannot be empty.")
            return

        # Check if the client file exists
        file_name = f"{client_id}.dat"
        if os.path.exists(file_name):
            # Load the client data from the file
            with open(file_name, "rb") as file:
                client = pickle.load(file)

            # Create a Toplevel window for updating client details
            update_client_window = tk.Toplevel(self.master)
            update_client_window.title("Update Client")

            # Labels and Entry fields for client details
            tk.Label(update_client_window, text="Client ID:").grid(row=0, column=0)
            tk.Label(update_client_window, text="Name:").grid(row=1, column=0)
            tk.Label(update_client_window, text="Address:").grid(row=2, column=0)
            tk.Label(update_client_window, text="Contact Details:").grid(row=3, column=0)
            tk.Label(update_client_window, text="Budget:").grid(row=4, column=0)

            client_id_var = tk.StringVar(update_client_window, value=client.client_id)
            name_var = tk.StringVar(update_client_window, value=client.name)
            address_var = tk.StringVar(update_client_window, value=client.address)
            contact_var = tk.StringVar(update_client_window, value=client.contact_details)
            budget_var = tk.DoubleVar(update_client_window, value=client.budget)

            tk.Entry(update_client_window, textvariable=client_id_var, state='readonly').grid(row=0, column=1)
            tk.Entry(update_client_window, textvariable=name_var).grid(row=1, column=1)
            tk.Entry(update_client_window, textvariable=address_var).grid(row=2, column=1)
            tk.Entry(update_client_window, textvariable=contact_var).grid(row=3, column=1)
            tk.Entry(update_client_window, textvariable=budget_var).grid(row=4, column=1)

            # Function to handle updating client
            def update():
                client.name = name_var.get()
                client.address = address_var.get()
                client.contact_details = contact_var.get()
                client.budget = budget_var.get()

                # Save the updated client data using Pickle
                with open(file_name, "wb") as file:
                    pickle.dump(client, file)

                messagebox.showinfo("Update Client", "Client details updated successfully.")
                update_client_window.destroy()

            # Button to update client
            update_button = tk.Button(update_client_window, text="Update", command=update)
            update_button.grid(row=5, columnspan=2)
        else:
            messagebox.showerror("Update Client", f"Client with ID {client_id} not found.")


    def delete_client(self):
        # Prompt user to enter the client ID
        client_id = simpledialog.askstring("Delete Client", "Enter Client ID to delete:")

        if not client_id:
            messagebox.showerror("Delete Client", "Client ID cannot be empty.")
            return

        # Check if the client file exists
        file_name = f"{client_id}.dat"
        if os.path.exists(file_name):
            # Delete the client file
            os.remove(file_name)
            messagebox.showinfo("Delete Client", "Client deleted successfully.")
        else:
            messagebox.showerror("Delete Client", f"Client with ID {client_id} not found.")

    def view_client(self):
        # Prompt user to enter the client ID
        client_id = simpledialog.askstring("View Client", "Enter Client ID to view:")

        if not client_id:
            messagebox.showerror("View Client", "Client ID cannot be empty.")
            return

        # Check if the client file exists
        file_name = f"{client_id}.dat"
        if os.path.exists(file_name):
            # Load the client data from the file
            with open(file_name, "rb") as file:
                client = pickle.load(file)

            # Display the client details in a message box
            client_details = f"Client ID: {client.client_id}\n" \
                            f"Name: {client.name}\n" \
                            f"Address: {client.address}\n" \
                            f"Contact Details: {client.contact_details}\n" \
                            f"Budget: {client.budget}"

            messagebox.showinfo("Client Details", client_details)
        else:
            messagebox.showerror("View Client", f"Client with ID {client_id} not found.")
    def add_venue(self):
        # Create a Toplevel window for adding venue details
        add_venue_window = tk.Toplevel(self.master)
        add_venue_window.title("Add Venue")

        # Labels and Entry fields for venue details
        tk.Label(add_venue_window, text="Venue ID:").grid(row=0, column=0)
        tk.Label(add_venue_window, text="Name:").grid(row=1, column=0)
        tk.Label(add_venue_window, text="Address:").grid(row=2, column=0)
        tk.Label(add_venue_window, text="Contact:").grid(row=3, column=0)
        tk.Label(add_venue_window, text="Min Guests:").grid(row=4, column=0)
        tk.Label(add_venue_window, text="Max Guests:").grid(row=5, column=0)

        venue_id_var = tk.StringVar(add_venue_window)
        name_var = tk.StringVar(add_venue_window)
        address_var = tk.StringVar(add_venue_window)
        contact_var = tk.StringVar(add_venue_window)
        min_guests_var = tk.IntVar(add_venue_window)
        max_guests_var = tk.IntVar(add_venue_window)

        tk.Entry(add_venue_window, textvariable=venue_id_var).grid(row=0, column=1)
        tk.Entry(add_venue_window, textvariable=name_var).grid(row=1, column=1)
        tk.Entry(add_venue_window, textvariable=address_var).grid(row=2, column=1)
        tk.Entry(add_venue_window, textvariable=contact_var).grid(row=3, column=1)
        tk.Entry(add_venue_window, textvariable=min_guests_var).grid(row=4, column=1)
        tk.Entry(add_venue_window, textvariable=max_guests_var).grid(row=5, column=1)

        # Function to handle adding venue
        def add():
            venue_id = venue_id_var.get()
            name = name_var.get()
            address = address_var.get()
            contact = contact_var.get()
            min_guests = min_guests_var.get()
            max_guests = max_guests_var.get()

            # Create a Venue object
            new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)

            # Save the venue data using Pickle
            file_name = f"{venue_id}.dat"
            with open(file_name, "wb") as file:
                pickle.dump(new_venue, file)

            messagebox.showinfo("Add Venue", "Venue added successfully.")
            add_venue_window.destroy()

        # Button to add venue
        add_button = tk.Button(add_venue_window, text="Add", command=add)
        add_button.grid(row=6, columnspan=2)

    def update_venue(self):
        # Prompt user to enter the venue ID
        venue_id = simpledialog.askstring("Update Venue", "Enter Venue ID to update:")

        if not venue_id:
            messagebox.showerror("Update Venue", "Venue ID cannot be empty.")
            return

        # Check if the venue file exists
        file_name = f"{venue_id}.dat"
        if os.path.exists(file_name):
            # Load the venue data from the file
            with open(file_name, "rb") as file:
                venue = pickle.load(file)

            # Create a Toplevel window for updating venue details
            update_venue_window = tk.Toplevel(self.master)
            update_venue_window.title("Update Venue")

            # Labels and Entry fields for venue details
            tk.Label(update_venue_window, text="Venue ID:").grid(row=0, column=0)
            tk.Label(update_venue_window, text="Name:").grid(row=1, column=0)
            tk.Label(update_venue_window, text="Address:").grid(row=2, column=0)
            tk.Label(update_venue_window, text="Contact:").grid(row=3, column=0)
            tk.Label(update_venue_window, text="Min Guests:").grid(row=4, column=0)
            tk.Label(update_venue_window, text="Max Guests:").grid(row=5, column=0)

            venue_id_var = tk.StringVar(update_venue_window, value=venue.venue_id)
            name_var = tk.StringVar(update_venue_window, value=venue.name)
            address_var = tk.StringVar(update_venue_window, value=venue.address)
            contact_var = tk.StringVar(update_venue_window, value=venue.contact)
            min_guests_var = tk.IntVar(update_venue_window, value=venue.min_guests)
            max_guests_var = tk.IntVar(update_venue_window, value=venue.max_guests)

            tk.Entry(update_venue_window, textvariable=venue_id_var, state='readonly').grid(row=0, column=1)
            tk.Entry(update_venue_window, textvariable=name_var).grid(row=1, column=1)
            tk.Entry(update_venue_window, textvariable=address_var).grid(row=2, column=1)
            tk.Entry(update_venue_window, textvariable=contact_var).grid(row=3, column=1)
            tk.Entry(update_venue_window, textvariable=min_guests_var).grid(row=4, column=1)
            tk.Entry(update_venue_window, textvariable=max_guests_var).grid(row=5, column=1)

            # Function to handle updating venue
            def update():
                venue.name = name_var.get()
                venue.address = address_var.get()
                venue.contact = contact_var.get()
                venue.min_guests = min_guests_var.get()
                venue.max_guests = max_guests_var.get()

                # Save the updated venue data using Pickle
                with open(file_name, "wb") as file:
                    pickle.dump(venue, file)

                messagebox.showinfo("Update Venue", "Venue details updated successfully.")
                update_venue_window.destroy()

            # Button to update venue
            update_button = tk.Button(update_venue_window, text="Update", command=update)
            update_button.grid(row=6, columnspan=2)
        else:
            messagebox.showerror("Update Venue", f"Venue with ID {venue_id} not found.")


    def delete_venue(self):
        # Prompt user to enter the venue ID
        venue_id = simpledialog.askstring("Delete Venue", "Enter Venue ID to delete:")

        if not venue_id:
            messagebox.showerror("Delete Venue", "Venue ID cannot be empty.")
            return

        # Check if the venue file exists
        file_name = f"{venue_id}.dat"
        if os.path.exists(file_name):
            # Delete the venue file
            os.remove(file_name)
            messagebox.showinfo("Delete Venue", "Venue deleted successfully.")
        else:
            messagebox.showerror("Delete Venue", f"Venue with ID {venue_id} not found.")

    def view_venue(self):
        # Prompt user to enter the venue ID
        venue_id = simpledialog.askstring("View Venue", "Enter Venue ID to view:")

        if not venue_id:
            messagebox.showerror("View Venue", "Venue ID cannot be empty.")
            return

        # Check if the venue file exists
        file_name = f"{venue_id}.dat"
        if os.path.exists(file_name):
            # Load the venue data from the file
            with open(file_name, "rb") as file:
                venue = pickle.load(file)

            # Display the venue details in a message box
            venue_details = f"Venue ID: {venue.venue_id}\n" \
                            f"Name: {venue.name}\n" \
                            f"Address: {venue.address}\n" \
                            f"Contact: {venue.contact}\n" \
                            f"Min Guests: {venue.min_guests}\n" \
                            f"Max Guests: {venue.max_guests}"

            messagebox.showinfo("Venue Details", venue_details)
        else:
            messagebox.showerror("View Venue", f"Venue with ID {venue_id} not found.")

    def add_guest(self):
        # Create a Toplevel window for adding guest details
        add_guest_window = tk.Toplevel(self.master)
        add_guest_window.title("Add Guest")

        # Labels and Entry fields for guest details
        tk.Label(add_guest_window, text="Guest ID:").grid(row=0, column=0)
        tk.Label(add_guest_window, text="Name:").grid(row=1, column=0)
        tk.Label(add_guest_window, text="Address:").grid(row=2, column=0)
        tk.Label(add_guest_window, text="Contact Details:").grid(row=3, column=0)

        guest_id_var = tk.StringVar(add_guest_window)
        name_var = tk.StringVar(add_guest_window)
        address_var = tk.StringVar(add_guest_window)
        contact_var = tk.StringVar(add_guest_window)

        tk.Entry(add_guest_window, textvariable=guest_id_var).grid(row=0, column=1)
        tk.Entry(add_guest_window, textvariable=name_var).grid(row=1, column=1)
        tk.Entry(add_guest_window, textvariable=address_var).grid(row=2, column=1)
        tk.Entry(add_guest_window, textvariable=contact_var).grid(row=3, column=1)

        # Function to handle adding guest
        def add():
            guest_id = guest_id_var.get()
            name = name_var.get()
            address = address_var.get()
            contact_details = contact_var.get()

            # Create a Guest object
            new_guest = Guest(guest_id, name, address, contact_details)

            # Save the guest data using Pickle
            file_name = f"{guest_id}.dat"
            with open(file_name, "wb") as file:
                pickle.dump(new_guest, file)

            messagebox.showinfo("Add Guest", "Guest added successfully.")
            add_guest_window.destroy()

        # Button to add guest
        add_button = tk.Button(add_guest_window, text="Add", command=add)
        add_button.grid(row=4, columnspan=2)

    def update_guest(self):
        # Prompt user to enter the guest ID
        guest_id = simpledialog.askstring("Update Guest", "Enter Guest ID to update:")

        if not guest_id:
            messagebox.showerror("Update Guest", "Guest ID cannot be empty.")
            return

        # Check if the guest file exists
        file_name = f"{guest_id}.dat"
        if os.path.exists(file_name):
            # Load the guest data from the file
            with open(file_name, "rb") as file:
                guest = pickle.load(file)

            # Create a Toplevel window for updating guest details
            update_guest_window = tk.Toplevel(self.master)
            update_guest_window.title("Update Guest")

            # Labels and Entry fields for guest details
            tk.Label(update_guest_window, text="Guest ID:").grid(row=0, column=0)
            tk.Label(update_guest_window, text="Name:").grid(row=1, column=0)
            tk.Label(update_guest_window, text="Address:").grid(row=2, column=0)
            tk.Label(update_guest_window, text="Contact Details:").grid(row=3, column=0)

            guest_id_var = tk.StringVar(update_guest_window, value=guest.guest_id)
            name_var = tk.StringVar(update_guest_window, value=guest.name)
            address_var = tk.StringVar(update_guest_window, value=guest.address)
            contact_var = tk.StringVar(update_guest_window, value=guest.contact_details)

            tk.Entry(update_guest_window, textvariable=guest_id_var, state='readonly').grid(row=0, column=1)
            tk.Entry(update_guest_window, textvariable=name_var).grid(row=1, column=1)
            tk.Entry(update_guest_window, textvariable=address_var).grid(row=2, column=1)
            tk.Entry(update_guest_window, textvariable=contact_var).grid(row=3, column=1)

            # Function to handle updating guest
            def update():
                guest.name = name_var.get()
                guest.address = address_var.get()
                guest.contact_details = contact_var.get()

                # Save the updated guest data using Pickle
                with open(file_name, "wb") as file:
                    pickle.dump(guest, file)

                messagebox.showinfo("Update Guest", "Guest details updated successfully.")
                update_guest_window.destroy()

            # Button to update guest
            update_button = tk.Button(update_guest_window, text="Update", command=update)
            update_button.grid(row=4, columnspan=2)
        else:
            messagebox.showerror("Update Guest", f"Guest with ID {guest_id} not found.")


    def delete_guest(self):
        # Prompt user to enter the guest ID
        guest_id = simpledialog.askstring("Delete Guest", "Enter Guest ID to delete:")

        if not guest_id:
            messagebox.showerror("Delete Guest", "Guest ID cannot be empty.")
            return

        # Check if the guest file exists
        file_name = f"{guest_id}.dat"
        if os.path.exists(file_name):
            # Delete the guest file
            os.remove(file_name)
            messagebox.showinfo("Delete Guest", "Guest deleted successfully.")
        else:
            messagebox.showerror("Delete Guest", f"Guest with ID {guest_id} not found.")

    def view_guest(self):
        # Prompt user to enter the guest ID
        guest_id = simpledialog.askstring("View Guest", "Enter Guest ID to view:")

        if not guest_id:
            messagebox.showerror("View Guest", "Guest ID cannot be empty.")
            return

        # Check if the guest file exists
        file_name = f"{guest_id}.dat"
        if os.path.exists(file_name):
            # Load the guest data from the file
            with open(file_name, "rb") as file:
                guest = pickle.load(file)

            # Display the guest details in a message box
            guest_details = f"Guest ID: {guest.guest_id}\n" \
                            f"Name: {guest.name}\n" \
                            f"Address: {guest.address}\n" \
                            f"Contact Details: {guest.contact_details}"

            messagebox.showinfo("Guest Details", guest_details)
        else:
            messagebox.showerror("View Guest", f"Guest with ID {guest_id} not found.")

    def add_supplier(self):
        # Create a Toplevel window for adding supplier details
        add_supplier_window = tk.Toplevel(self.master)
        add_supplier_window.title("Add Supplier")

        # Labels and Entry fields for supplier details
        tk.Label(add_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        tk.Label(add_supplier_window, text="Name:").grid(row=1, column=0)
        tk.Label(add_supplier_window, text="Address:").grid(row=2, column=0)
        tk.Label(add_supplier_window, text="Contact Details:").grid(row=3, column=0)
        tk.Label(add_supplier_window, text="Menu:").grid(row=4, column=0)
        tk.Label(add_supplier_window, text="Min Guests:").grid(row=5, column=0)
        tk.Label(add_supplier_window, text="Max Guests:").grid(row=6, column=0)

        supplier_id_var = tk.StringVar(add_supplier_window)
        name_var = tk.StringVar(add_supplier_window)
        address_var = tk.StringVar(add_supplier_window)
        contact_var = tk.StringVar(add_supplier_window)
        menu_var = tk.StringVar(add_supplier_window)
        min_guests_var = tk.IntVar(add_supplier_window)
        max_guests_var = tk.IntVar(add_supplier_window)

        tk.Entry(add_supplier_window, textvariable=supplier_id_var).grid(row=0, column=1)
        tk.Entry(add_supplier_window, textvariable=name_var).grid(row=1, column=1)
        tk.Entry(add_supplier_window, textvariable=address_var).grid(row=2, column=1)
        tk.Entry(add_supplier_window, textvariable=contact_var).grid(row=3, column=1)
        tk.Entry(add_supplier_window, textvariable=menu_var).grid(row=4, column=1)
        tk.Entry(add_supplier_window, textvariable=min_guests_var).grid(row=5, column=1)
        tk.Entry(add_supplier_window, textvariable=max_guests_var).grid(row=6, column=1)

        # Function to handle adding supplier
        def add():
            supplier_id = supplier_id_var.get()
            name = name_var.get()
            address = address_var.get()
            contact_details = contact_var.get()
            menu = menu_var.get()
            min_guests = min_guests_var.get()
            max_guests = max_guests_var.get()

            # Create a Supplier object
            new_supplier = Supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)

            # Save the supplier data using Pickle
            file_name = f"{supplier_id}.dat"
            with open(file_name, "wb") as file:
                pickle.dump(new_supplier, file)

            messagebox.showinfo("Add Supplier", "Supplier added successfully.")
            add_supplier_window.destroy()

        # Button to add supplier
        add_button = tk.Button(add_supplier_window, text="Add", command=add)
        add_button.grid(row=7, columnspan=2)
    def update_supplier(self):
        # Prompt user to enter the supplier ID
        supplier_id = simpledialog.askstring("Update Supplier", "Enter Supplier ID to update:")

        if not supplier_id:
            messagebox.showerror("Update Supplier", "Supplier ID cannot be empty.")
            return

        # Check if the supplier file exists
        file_name = f"{supplier_id}.dat"
        if os.path.exists(file_name):
            # Load the supplier data from the file
            with open(file_name, "rb") as file:
                supplier = pickle.load(file)

            # Create a Toplevel window for updating supplier details
            update_supplier_window = tk.Toplevel(self.master)
            update_supplier_window.title("Update Supplier")

            # Labels and Entry fields for supplier details
            tk.Label(update_supplier_window, text="Supplier ID:").grid(row=0, column=0)
            tk.Label(update_supplier_window, text="Name:").grid(row=1, column=0)
            tk.Label(update_supplier_window, text="Address:").grid(row=2, column=0)
            tk.Label(update_supplier_window, text="Contact Details:").grid(row=3, column=0)
            tk.Label(update_supplier_window, text="Menu:").grid(row=4, column=0)
            tk.Label(update_supplier_window, text="Min Guests:").grid(row=5, column=0)
            tk.Label(update_supplier_window, text="Max Guests:").grid(row=6, column=0)

            supplier_id_var = tk.StringVar(update_supplier_window, value=supplier.supplier_id)
            name_var = tk.StringVar(update_supplier_window, value=supplier.name)
            address_var = tk.StringVar(update_supplier_window, value=supplier.address)
            contact_var = tk.StringVar(update_supplier_window, value=supplier.contact_details)
            menu_var = tk.StringVar(update_supplier_window, value=supplier.menu)
            min_guests_var = tk.IntVar(update_supplier_window, value=supplier.min_guests)
            max_guests_var = tk.IntVar(update_supplier_window, value=supplier.max_guests)

            tk.Entry(update_supplier_window, textvariable=supplier_id_var, state='readonly').grid(row=0, column=1)
            tk.Entry(update_supplier_window, textvariable=name_var).grid(row=1, column=1)
            tk.Entry(update_supplier_window, textvariable=address_var).grid(row=2, column=1)
            tk.Entry(update_supplier_window, textvariable=contact_var).grid(row=3, column=1)
            tk.Entry(update_supplier_window, textvariable=menu_var).grid(row=4, column=1)
            tk.Entry(update_supplier_window, textvariable=min_guests_var).grid(row=5, column=1)
            tk.Entry(update_supplier_window, textvariable=max_guests_var).grid(row=6, column=1)

            # Function to handle updating supplier
            def update():
                supplier.supplier_id = supplier_id_var.get()
                supplier.name = name_var.get()
                supplier.address = address_var.get()
                supplier.contact_details = contact_var.get()
                supplier.menu = menu_var.get()
                supplier.min_guests = min_guests_var.get()
                supplier.max_guests = max_guests_var.get()

                # Save the updated supplier data using Pickle
                with open(file_name, "wb") as file:
                    pickle.dump(supplier, file)

                messagebox.showinfo("Update Supplier", "Supplier updated successfully.")
                update_supplier_window.destroy()

            # Button to update supplier
            update_button = tk.Button(update_supplier_window, text="Update", command=update)
            update_button.grid(row=7, columnspan=2)
        else:
            messagebox.showerror("Update Supplier", f"Supplier with ID {supplier_id} not found.")
    def delete_supplier(self):
        # Prompt user to enter the supplier ID
        supplier_id = simpledialog.askstring("Delete Supplier", "Enter Supplier ID to delete:")

        if not supplier_id:
            messagebox.showerror("Delete Supplier", "Supplier ID cannot be empty.")
            return

        # Check if the supplier file exists
        file_name = f"{supplier_id}.dat"
        if os.path.exists(file_name):
            # Confirm deletion with user
            confirmation = messagebox.askyesno("Delete Supplier", f"Are you sure you want to delete supplier with ID {supplier_id}?")
            if confirmation:
                # Delete the supplier file
                os.remove(file_name)
                messagebox.showinfo("Delete Supplier", "Supplier deleted successfully.")
        else:
            messagebox.showerror("Delete Supplier", f"Supplier with ID {supplier_id} not found.")
    def view_supplier(self):
        # Prompt user to enter the supplier ID
        supplier_id = simpledialog.askstring("View Supplier", "Enter Supplier ID to view:")

        if not supplier_id:
            messagebox.showerror("View Supplier", "Supplier ID cannot be empty.")
            return

        # Check if the supplier file exists
        file_name = f"{supplier_id}.dat"
        if os.path.exists(file_name):
            # Load the supplier data from the file
            with open(file_name, "rb") as file:
                supplier = pickle.load(file)

            # Create a Toplevel window for viewing supplier details
            view_supplier_window = tk.Toplevel(self.master)
            view_supplier_window.title("View Supplier Details")

            # Display supplier details
            tk.Label(view_supplier_window, text="Supplier ID:").grid(row=0, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.supplier_id).grid(row=0, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Name:").grid(row=1, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.name).grid(row=1, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Address:").grid(row=2, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.address).grid(row=2, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Contact Details:").grid(row=3, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.contact_details).grid(row=3, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Menu:").grid(row=4, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.menu).grid(row=4, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Min Guests:").grid(row=5, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.min_guests).grid(row=5, column=1, sticky="w")
            tk.Label(view_supplier_window, text="Max Guests:").grid(row=6, column=0, sticky="w")
            tk.Label(view_supplier_window, text=supplier.max_guests).grid(row=6, column=1, sticky="w")
        else:
            messagebox.showerror("View Supplier", f"Supplier with ID {supplier_id} not found.")


def main():
    root = tk.Tk()
    app = ManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()