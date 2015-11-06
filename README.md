An ongoing scheduling application as a learning project implemented in django, python.

Introduction:
    This application lets user(employer) to upload an existing excel file that holds the schedule of employees and transform the schedule of each employee into monthly calendar.
    The application assumes a fixed layout excel file for the purpose of demo with the actual employee schedule data to start from row 13 and date field to be at row 8.
    All these excel fields are transformed to django database and displayed in a calendar form clearly showing the work day and free day.
    
Basic Usage:
    1. User(employer) uploads excel file.
    2. Excel file is processed into database
    3. Employer auto generates user credentials for employees with the format: employeeid@companyname(for eg. 111@abc) and random password.
        (for demo purpose password generated is always "mypassword").
    3. User(employees) login with their credentials
    4. a monthly calendar is displayed to each user with their respective work schedule
    5. each day cell of calendar represent whether its working day or free day with different coloring.
  Note: For the development and testing purpose the file is already included and adding other excel file without specific formatting will not work.
  
This project is still in development phase.
for database/admin access: username- admin, password-admin
for demo calendar view: 222@admico, password:mypassword
                
copyright Anish.
    