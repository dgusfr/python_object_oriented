class Student:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    def __str__(self):
        return f"Aluno: {self.name}, Média: {self.average():.2f}"

    def average(self):
        return sum(self.notes) / len(self.notes)


minhas_notas = [9.2, 8.5, 7.0]
aluno = Student("Diego", minhas_notas)

print(aluno)
