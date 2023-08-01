from class_project import Project

with Project.users_from_json() as project:
    project.run()