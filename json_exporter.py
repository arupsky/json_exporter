from os import listdir
import openpyxl
import json
import Trial_DTO

input_folder_path = ""+"/"
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


trial_DTO = Trial_DTO.Trial_DTO()
# trial_DTO = Trial_DTO.build_trial_dto()
for current_row in range(2, m_row + 1):
    diameter_obj = sheet_obj.cell(row = current_row, column = 1)
    stimulii_obj = sheet_obj.cell(row = current_row, column = 2)
    # print(diameter_obj.value)
    if (stimulii_obj.value == 'b'):
        baseline.append(diameter_obj.value)
    elif (stimulii_obj.value == 'r' and trial_DTO.trial_id != stimulii_obj.value):        
        # save to dictionary
        trial_DTO = Trial_DTO.Trial_DTO(trial_id, pupil_dilation, baseline, 0)
        
        print(str(trial_DTO.baseline))
        # trial_DTO.trial_id = trial_id
        # trial_DTO.pupil_dilation = pupil_dilation
        # trial_DTO.baseline = baseline

        pupil_dilation = []
        baseline = []
            
    else:        
        pupil_dilation.append(diameter_obj.value)
        trial_id = stimulii_obj.value

