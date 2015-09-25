from app.data import exportToFile
from app.task import Task

def test_Export_To_File():
    # Create a mock task
    task = Task()
    task.title = "Title"
    task.description = "Description"
    task.creator = "test@test.com"
    task.assignee = "test@test.com"

    exportToFile([task], 'test.json')
