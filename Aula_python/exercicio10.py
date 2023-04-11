#10.Chico tem 1,50m e cresce 2 centímetros por ano, 
#enquanto Juca tem 1,10m e cresce 5 centímetros por ano. 
#Considerando que Chico e Juca continuem crescendo constantemente, escreva 
#um algoritmo que calcule quantos anos seriam necessários para Juca ser mais alto que Chico.
altura_Chico = 1.5
altura_Juca = 1.1
ano = 0
while altura_Chico > altura_Juca:
    altura_Chico += 0.02
    altura_Juca += 0.05
    ano += 1
print(f'Seriam necessários {ano} anos')