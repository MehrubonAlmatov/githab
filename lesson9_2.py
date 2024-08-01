class Person:
    def __init__(self, first_name, last_name, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession

    def person_info(self):
        return f"{self.first_name} {self.last_name}, kasbi {self.profession}"

class Teacher(Person):
    def __init__(self, first_name, last_name, profession, experience, speciality):
        super().__init__(first_name, last_name, profession)  # Parent classdan propertylar o'zlashtiriladi
        self.experience = experience
        self.speciality = speciality

    def action(self):
        return f"O'qituvchi {self.speciality} yo'nalishi bo'yicha dars beradi."

    def update_experience(self, new_experience):
        print(f"Ish staji {self.experience}dan {new_experience}ga o'zgartirildi.")
        self.experience = new_experience

    def person_info(self):
        return f"{self.first_name} {self.last_name}, kasbi {self.profession}, {self.speciality} yo'nalishida {self.experience} yil tajribaga ega."

teacher = Teacher("Falochi", "Pistonchiyev", "O'qituvchi", 10, "Matematika")

print(teacher.person_info())

print(teacher.action())

teacher.update_experience(12)

print(teacher.person_info())
