arquivo = open("alunos.txt", "r", encoding="utf-8")

for linha in arquivo:
    aluno = linha.split()

    resultado = ""

    if int(aluno[2]) > 7:
        resultado = "aprovado"
    else:
        resultado = "reprovado"

    print(f"""
            Aluno: {aluno[0]}
            Curso: {aluno[1]}
            Nota: {aluno[2]}  
            Resultado: {resultado}
            """)

