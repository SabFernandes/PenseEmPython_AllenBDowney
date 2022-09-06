#Exercícios 

#Exercícios 1.1

#Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
1. print('hello' -> SyntaxError: unexpected EOF while parsing
print'hello' -> SyntaxError: invalid syntax

#Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
2. print(hello, world) -> NameError: name 'hello' is not defined
print('hello) -> SyntaxError: EOL while scanning string literal

#Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
3. print(2++2) -> 4

#Na notação matemática, zeros á esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no python?
4. print(2+02) -> SyntaxError: leading zeros in decimal in teger literals are not permitted; use an 0o prefix for octal integers

#O que acontece se você tiver dois valores sem nenhum operador entre eles?
5. 2 2 -> SyntaxError: invalid syntax

Exercício 1.2

#Quantos segundos há em 42 minutos e 42 segundos?
1. print(42 * 60 + 42) -> 2562

#Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1.61 quilômetro
2. print(10/1.61) -> 6.211180124223602

#Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o passo médio (Tempo por milha em minutos e segundos)? Qual é a velocidade média em milhas por hora?
3. print((42 * 60 + 42) / (10 / 1.61) / 60) -> 6.8747000000000001
print((10 / 1.61) * (60 * 60) / (42 * 60 + 42) -> 8.727653570337614
