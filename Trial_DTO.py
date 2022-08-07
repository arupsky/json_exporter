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