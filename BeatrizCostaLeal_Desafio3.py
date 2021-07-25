def autoriza_voto(ano):
     from datetime import date
     atual=date.today().year
     idade=atual-ano
     if idade<16:
        return "NEGADO"
     elif 16>=idade<18 or idade>65:   
          return "OPCIONAL"  
     else: 
       return "OBRIGATÓRIO"

def votacao(autorizacao,voto):
     autorizacao = autoriza_voto(ano_Nasc)
     if autorizacao== "NEGADO":
          return "Voce ainda nao pode votar"
     if voto==1:
          candidatos["Valente"]+=1
     elif voto==2:
          candidatos["Bud"]+=1 
     elif voto==3:
         candidatos["Chaves"]+=1
     elif voto==4:
          candidatos["Nulo"]+=1
     elif voto==5:
          candidatos["Branco"]+=1     
     return "Seu voto foi aceito"


candidatos = {"Valente":0, "Bud":0, "Chaves":0, "Nulo":0,"Branco":0}
while True:
     ano_Nasc=int(input("Qual ano voce nasceu?"))
     print("Candidato Valente [1]\nCandidato Bud [2]\nCandidato Chaves [3]\nNulo [4]\nBranco [5]")
     escolha_Candidato= int(input("Digite o numero do candidato"))
     autorizacao= autoriza_voto(ano_Nasc)
     print(votacao(autorizacao,escolha_Candidato))
     print("Obrigada pelo seu voto!")
     var= input("Deseja continuar? [S/N]").upper()[0]
     while var not in "SN":
          var= input("Deseja continuar? [S/N]").upper()[0]
     if var=="N":
          break

print(f"Candidato Valente recebeu {candidatos['Valente']} votos")
print(f"Candidato Bud recebeu {candidatos['Bud']} votos")
print(f"Candidato Chaves recebeu {candidatos['Chaves']} votos")
print(f"Candidato Nulo recebeu {candidatos['Nulo']} votos")
print(f"Candidato Brancos recebeu {candidatos['Brancos']} votos")

if candidatos["Valente"] > candidatos ["Bud"] and candidatos["Valente"] > candidatos ["Chaves"] and candidatos["Valente"] > candidatos ["Nulo"] and candidatos["Valente"] > candidatos ["Branco"]:
     print("Candidato Valente venceu")
elif candidatos["Bud"] > candidatos["Valente"] and candidatos["Bud"] > candidatos ["Chaves"] and candidatos["Bud"] > candidatos ["Nulo"] and candidatos["Bud"] > candidatos ["Branco"]:
     print("Candidato Bud venceu")

elif candidatos["Chaves"] > candidatos["Valente"] and candidatos["Chaves"] > candidatos ["Bud"] and candidatos["Chaves"] > candidatos ["Nulo"] and candidatos["Chaves"] > candidatos ["Branco"]:
     print("Candidato Chaves venceu")
elif candidatos["Nulo"] > candidatos["Valente"] and candidatos["Nulo"] > candidatos ["Bud"] and candidatos["Nulo"] > candidatos ["Chaves"] and candidatos["Nulo"] > candidatos ["Branco"]:
     print("Votos nulos venceu")            
elif candidatos["Branco"] > candidatos["Valente"] and candidatos["Branco"] > candidatos ["Bud"] and candidatos["Branco"] > candidatos ["Chaves"] and candidatos["Branco"] > candidatos ["Nulo"]:
     print("Votos Brancos venceu")   