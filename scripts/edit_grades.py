from lib.input import ask_bool
from lib.display import ordered_list


def bulletin(students: dict):
    print("\n======== Boletim ========")
    for name, grades in students.items():
        print("\n" + name)
        print("\n".join(grades))
        print("Média:", sum(grades) / 4)


# Login teacher
user = input("Usuário: ")
password = input("Senha: ")

while password != "1234":
    password = input("Senha incorreta. Tente novamente: ")

# Register grades
students = {
    input("\nNome do aluno: "): [float(input(f"Bimestre {i}: ")) for i in range(1, 5)]
    for _ in range(10)
}

# Show grades
bulletin(students)

# Edit grades
edit = ask_bool("\nGostaria de editar algo?")

while edit:
    pick = input("\nQual aluno? ")
    print("\n".join(ordered_list(students[pick])))
    bimester = int(input("Qual bimestre gostaria de editar? ")) - 1
    students[pick][bimester] = float(input("Novo valor: "))

    edit = ask_bool("\nGostaria de editar algo?")

# Show grades (again)
bulletin(students)

print("\nThanks for using Cobra Manager :D 🐍")
