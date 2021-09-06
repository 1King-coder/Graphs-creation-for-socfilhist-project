from .Answers import Answers

class Student(Answers):
  def __init__(self, answers_obj, student_obj) -> None:
    super().__init__(answers_obj)
    super().total_answers
    super().predominant_options

    self.id: int = student_obj['id']
    self.fullname: str = student_obj['fullname']
    self.age: int = student_obj['age']
    self.grade: str = student_obj['grade']
    self.status: str = student_obj['status']
    self.genre: str = student_obj['genre']

  def __repr__(self) -> str:
    return f"""
    Id: {self.id}
    Name: {self.fullname}
    Age: {self.age}
    Grade: {self.grade}
    Status: {self.status}
    Genre: {self.genre}
    Predominant options: {self.predominant_options}
    """