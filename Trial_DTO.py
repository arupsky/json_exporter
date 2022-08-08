from cmath import nan


class Trial_DTO:
    trial_id = ""
    pupil_dilation = []
    baseline = []
    rating = 0

    def __init__(self, trial_id="", pupil_dilation=[], baseline=[], rating=0):
        self.trial_id = trial_id
        self.pupil_dilation = pupil_dilation
        self.baseline = baseline
        self.rating = rating
    
    def tojson(self):
        if self.rating is not nan:
            return f'{{"trial_id": "{self.trial_id}", "pupil_dilation": {self.pupil_dilation}, "baseline": {self.baseline}, "rating": {self.rating}}}'.replace ("\'Nan\'", "0").replace ("None", "0")