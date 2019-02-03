from datetime import datetime


class Task:

    def __init__(self, name, note, deadline, id=None, started=datetime.now()):
        self.name = name
        self.note = note
        self.deadline = deadline
        self.started = started
        self.id = id

    def print(self):
        print("| {:2} | {:<16} | {:<55} | {:30} | {:<30}".format(self.id, self.name, self.note, self.started, self.deadline).lower())

    @classmethod
    def from_row(cls, row):
        if len(row) < 5:
            return cls(row[0], row[1], row[2])
        else:
            return cls(row[1], row[2], row[4], row[0], row[3])