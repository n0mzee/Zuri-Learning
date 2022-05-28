class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    
    def change_name(self, change_name):
        self.change_name = change_name
        print("Name updated successfully. New name is: ",change_name)

    def change_age (self, change_age):
        self.change_age = change_age
        print("Age updated successfully. New age is: ",change_age)

    def add_track (self, add_track):
        self.tracks.append(add_track)
        print ("Track(s)", add_track, "added successfully. New tracks: ", self.tracks)

    def get_score(self):
        print("Score fetch successful. The score is: ", self.score)
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
