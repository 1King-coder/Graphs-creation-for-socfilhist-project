from abc import ABC

class Answers(ABC):
  def __init__ (self, answers_obj) -> None:
    self.answers: list = list(answers_obj.items())[1:]

  @property
  def total_answers(self) -> dict:
    total_option_1, total_option_2, total_option_3 = [0, 0, 0]
    
    for _, value in self.answers:
      if (value == 1):
        total_option_1 += 1

      if (value == 2):
        total_option_2 += 1
      
      if (value == 3):
        total_option_3 += 1

    return {
      'total_option_1': total_option_1,
      'total_option_2': total_option_2,
      'total_option_3': total_option_3
    }

  @property
  def predominant_options(self) -> str:
    total_options: dict = {
      "option 1": self.total_answers['total_option_1'],
      "option 2": self.total_answers['total_option_2'],
      "option 3": self.total_answers['total_option_3']
    }

    predominant_options: str = ''
    major: int = 0

    for option, total in total_options.items():
      if total > major:
        major = total
        predominant_options = option
      
      elif total == major:
        predominant_options += f', {option}'
    
    return predominant_options