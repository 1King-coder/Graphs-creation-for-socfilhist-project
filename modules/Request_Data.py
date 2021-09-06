import requests
import json
from .log import log

STUDENTS_URL = 'http://54.94.27.19/students'
STUDENTS_ANSWERS_URL = 'http://54.94.27.19/questions/retrieveData/answers'

class Get_Data:
  @staticmethod
  def request_data(url: str) -> dict:
    response = requests.get(url)
    
    data = json.loads(response.text)
    return data

  @staticmethod
  def students_data() -> list:
    return Get_Data.request_data(STUDENTS_URL)

  @staticmethod
  def answers_data() -> list:
    return Get_Data.request_data(STUDENTS_ANSWERS_URL)


if __name__ == "__main__":
  array = ['a', 'b', 'c']

  for i, a in enumerate(array):
    print(i, a)