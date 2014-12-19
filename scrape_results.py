# for controlling the browser
from selenium import webdriver
# for soup what else?! (to parse the data)
from bs4 import BeautifulSoup
# to emulate pressing enter instead of getting the button and clicking it
from selenium.webdriver.common.keys import Keys
# To select 2nd sem from drop down list
from selenium.webdriver.support.ui import Select
# To convert an object into data that can be handled as a chunk, remember Writing things to file is the file objects responsibility.
import pickle
# because otherwise python doesnt recognise the error I specified and throws a NameError: name 'NoSuchElementException' is not defined
from selenium.common.exceptions import NoSuchElementException

# open a window of firefox
driver = webdriver.Firefox()

# lets store the data in objects of this class
class student:
        # the things that "Define" a student! lol
	name = "aditya"

	rollno = "110113006"

	dept = u'SECOND SEMESTER INSTRUMENTATION AND CONTROL ENGINEERING MAY-2014(REGULAR)'
    
	# btw u means unicode format is used to represent the string
	# the value are , in order
	row_key = [u'Sr.No.', u'Course Code', u'Course Name', u'Credit', u'Grade', u'Attendance Grade']

	# Course Code, Course Name, Credit, Grade, Attendance Grade
	srno1 = ['1','PH102','PHYSICS - II','4','B','G']

	# these are just the default values so dont mind them
	srno2 = ['2','PH102','PHYSICS - II','4','B','G']
	srno3 = ['3','PH102','PHYSICS - II','4','B','G']
	srno4 = ['4','PH102','PHYSICS - II','4','B','G']
	srno5 = ['5','PH102','PHYSICS - II','4','B','G']
	srno6 = ['6','PH102','PHYSICS - II','4','B','G']
	srno7 = ['7','PH102','PHYSICS - II','4','B','G']
	srno8 = ['8','PH102','PHYSICS - II','4','B','G']
	srno9 = ['9','PH102','PHYSICS - II','4','B','G']

	# I mean credits here, ob!
	total_registed = '23'
	total_earned = '23'

	GPA = '7.57'

for roll_number in range(106113001,106113100):
    
    # intialize a empty list in which the students data will be stored
    temp_data=[]

    # Found the url where the actual elements lie in, behind the frame!
    driver.get("http://www.nitt.edu/prm/nitreg/ShowRes.aspx")

    # Get a handle onto the text box where we enter the student's roll number
    rollno = driver.find_element_by_name("TextBox1")

    # enter the details's of the student about whom the data should be obtained
    rollno.send_keys(str(roll_number))
    rollno.send_keys(Keys.RETURN)

    # in some cases the specified roll number will not have a student
    # thus no element from which we can select 2nd semester appears on the
    # webpage. To catch this NoSuchElementException:
    try:
        # Get the dropdown menu into the select wrapper with which
        select = Select(driver.find_element_by_id("Dt1"))
    except NoSuchElementException:
        print "No student corresponding to this rollnumber : "+str(roll_number)+" Exists in the database"
        continue
    # we select the "student's" 2nd semester marks as our area of intrest
    select.select_by_visible_text("MAY-2014(REGULAR)")

    # now that we have the table which hold the data in the page
    # lets form a list with this data, a list for each student!

    # get the raw source code into html
    html = driver.page_source

    # soupify IT - basically parse it for further operations
    soup = BeautifulSoup(html)
    
    # soup.findAll('table') this returns all tables in the page ( 4 of them actually)
    # of which we want the data in the second one thus soup.findAll('table')[1]
    # from this table we extract the table body identified by 'tbody'
    table_body=soup.findAll('table')[1].find('tbody')

    # we use 'tr' to get all the rows of this table into the rows list
    rows = table_body.find_all('tr')

    # we iterate over the rows
    for row in rows:
        # col = column, ele = element
        cols = row.find_all('td')
        
        cols  = [ele.text.strip() for ele in cols]
        # add to temp_data
        temp_data.append([ele for ele in cols if ele]) # Get rid of empty values
        # Now temp_data has the data we need in form of nested lists

    # Lets take this data and populate a new instance of student
    temp_student = student()

    temp_student.dept = temp_data[0][0]
    temp_student.name = temp_data[1][1]
    temp_student.rollno = temp_data[2][1]

    # the always same top row of the table (Assert!!)
    temp_list=[]
    for ele in temp_data[4]:
        temp_list.append(ele)
    assert temp_list == [u'Sr.No.', u'Course Code', u'Course Name', u'Credit', u'Grade', u'Attendance Grade']

    # the following are as u can see the different rows of the table
    # 5 corresponds to Sr.No. 1 and 6 -> 2 etc..
    temp_list=[]
    for ele in temp_data[5]:
        temp_list.append(ele)
    temp_student.srno1 = temp_list

    temp_list=[]
    for ele in temp_data[6]:
        temp_list.append(ele)
    temp_student.srno2 = temp_list

    temp_list=[]
    for ele in temp_data[7]:
        temp_list.append(ele)
    temp_student.srno3 = temp_list

    temp_list=[]
    for ele in temp_data[8]:
        temp_list.append(ele)
    temp_student.srno4 = temp_list

    temp_list=[]
    for ele in temp_data[9]:
        temp_list.append(ele)
    temp_student.srno5 = temp_list

    temp_list=[]
    for ele in temp_data[10]:
        temp_list.append(ele)
    temp_student.srno6 = temp_list

    temp_list=[]
    for ele in temp_data[11]:
        temp_list.append(ele)
    temp_student.srno7 = temp_list

    temp_list=[]
    for ele in temp_data[12]:
        temp_list.append(ele)
    temp_student.srno8 = temp_list

    temp_list=[]
    for ele in temp_data[13]:
        temp_list.append(ele)
    temp_student.srno9 = temp_list


    # The credits of this semester
    temp_student.total_registed = temp_data[14][1]

    temp_student.total_earned = temp_data[15][1]

    # the last entry in the nested list The GPA
    temp_student.GPA = temp_data[16][1]

    # now for this student we have his data stored in temp_student

    # Lets get a handle in permenant memory using the rollno as the filename
    file_handler = open(temp_student.rollno+".student", 'wb')

    # and  save this information
    pickle.dump(temp_student, file_handler)

    print "stored "+temp_data[0][0][16:55]+"'s student ("+temp_student.rollno+") "+temp_student.name+"'s "+temp_data[0][0][0:15]+" marks to memory."
    


    
    
    



	
    

