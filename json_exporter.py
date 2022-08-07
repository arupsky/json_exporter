from os import listdir
import openpyxl
import json
import Trial_DTO
import pandas

input_folder_path = "test_data/118170"+"/"
output_folder_path = input_folder_path +"/output.json"

trial_dictionary = {}

trial_id = ""
pupil_dilation = []
baseline = []
rating = 0

wb_obj =  openpyxl.load_workbook("test_data/118170/118170_pupil_reaction_to_faces_2022-08-04_1143.xlsx")
current_row = 2
sheet_obj = wb_obj.active
m_row = sheet_obj.max_row

isSaved = False
trial_DTO = Trial_DTO.Trial_DTO()
# trial_DTO = Trial_DTO.build_trial_dto()
for current_row in range(2, m_row + 1):
    diameter_obj = sheet_obj.cell(row = current_row, column = 1)
    stimulii_obj = sheet_obj.cell(row = current_row, column = 2)
    # print(diameter_obj.value)
    if (stimulii_obj.value == 'b'):
        baseline.append(diameter_obj.value)
        isSaved = False
    elif (stimulii_obj.value == 'r' and not isSaved):
        # save to dictionary
        trial_DTO = Trial_DTO.Trial_DTO(trial_id, pupil_dilation, baseline, 0)        
        # print(str(trial_DTO.baseline))

        trial_dictionary[trial_id] = trial_DTO

        pupil_dilation = []
        baseline = []
        isSaved = True
            
    else:        
        pupil_dilation.append(diameter_obj.value)
        trial_id = stimulii_obj.value


rating_csv = pandas.read_csv("test_data/118170/118170_pupil_reaction_to_faces_2022_Aug_04_1343.csv", usecols=['image.dir', 'rating_score.response'])
print(rating_csv['image.dir'][0])

for index in range (0, len(rating_csv)):
    trial_dictionary[rating_csv['image.dir'][index]].rating = rating_csv['rating_score.response'][index]

f = open (output_folder_path, 'w')
f.write (json.dumps (trial_dictionary))
f.close()

print ("Done: " + str (len(rating_csv)))

print(trial_dictionary['./images/male/28.jpg'].rating)
print(trial_dictionary['./images/male/28.jpg'].baseline[0])