sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma_distribuidora = sp + rj + mg + es + outros

porcentagem_sp = (sp*100)//soma_distribuidora
porcentagem_rj = (rj*100)//soma_distribuidora
porcentagem_mg = (rj*100)//soma_distribuidora
porcentagem_es = (rj*100)//soma_distribuidora
porcentagem_outros = (rj*100)//soma_distribuidora

print(f"A porcentagem de São Paulo é de {porcentagem_sp}%")
print(f"A porcentagem do Rio de Janeiro é de {porcentagem_rj}%")
print(f"A porcentagem de Minas Gerais é de {porcentagem_mg}%")
print(f"A porcentagem do Espírito Santo é de {porcentagem_es}%")
print(f"A porcentagem dos outros estados é de {porcentagem_outros}%")

