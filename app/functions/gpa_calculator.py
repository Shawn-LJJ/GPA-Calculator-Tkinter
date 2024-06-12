GRADE_TO_POINT = {
            'A+' : 4,
            'A' : 4,
            'B+' : 3.5,
            'B' : 3,
            'C+' : 2.5,
            'C' : 2,
            'D+' : 1.5,
            'D' : 1,
            'P' : 0.5
        }

class GPA_Calculator():
    def __init__(self, data: list) -> None:
        self.data: list = data

    def calculateGPA(self) -> float:
        
        numerator = 0
        denominator = 0
        
        for module in self.data:
            numerator += (int(module[0]) * GRADE_TO_POINT[module[1]])        # sum of product of credit and grade
            denominator += int(module[0])                                    # sum of credits
        
        return numerator / denominator