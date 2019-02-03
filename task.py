from datetime import datetime


class Task:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.note = kwargs.get("note")
        self.deadline = kwargs.get("deadline")
        self.started = kwargs.get("started", datetime.now())
        self.id = kwargs.get("id")

    def print(self):
        print("| {:2} | {:<16} | {:<55} | {:30} | {:<30}".format(self.id, self.name, self.note, self.started, self.deadline).lower())

    @classmethod
    def from_row(cls, row):
        if len(row) < 5:
            return cls(name=row[0], note=row[1], deadline=row[2])
        else:
            return cls( id=row[0], name=row[1], note=row[2], started=row[3], deadline=row[4])