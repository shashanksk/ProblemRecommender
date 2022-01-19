import codeforces_api
import json
import os


#using the codeforces api to get a wrapper object
parser = codeforces_api.CodeforcesParser()
wrapper_object = codeforces_api.CodeforcesApi('2e89464a5fb953bf014b7c72036cc90366d97905','e9652017350294cdeda8690b20bf56d6d8fe3360')


#initialising the code with an dictionary
dict = { "data":[]}


#convert to json object
json_object = json.dumps(dict,indent = 4)


#just to find the size of the file
filesize = os.path.getsize("json_file.json")



#if the file empty make a new one if not append the data
if filesize==0:
    with open("json_file.json", "w") as outfile:
        outfile.write(json_object)


#just a counter(to keep a count of the data)
i=0



#get some data from the webstite
submission = wrapper_object.problemset_recent_status(1000, problemset_name= "")



#function to add dictionary values
def add_dict(key,value):
    dict.__setitem__(key,value)


#writes the dictionary to the json file========================================
def write_json(new_data, filename='json_file.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["data"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
#==============================================================================



for pointer in submission:
   
   
    i+=1
    #to make it into one dictionary
    add_dict('count',i)
    add_dict('ids',pointer.id)
    add_dict('contest',pointer.contest_id)
    add_dict('problemrating',pointer.problem.rating)
    print(dict)
    
    write_json(dict)
    
      

    
    







