#first_name = "bro"
#print(type(first_name))
#last_name = "code"
#full_name = first_name+" " +last_name
#print("hello "+full_name)

#age = 21
#age +=1
#print(age)
#print("yor age is: "+str(age))

#height = 250.5
#print("Your height is: "+str(height)+"cm")
#print(type(height))

#human = True
#print(human)
#print("are you a huma:"+str(human))

# MULTIPLE ASSIGMENT = alows us to assgn multiple variables at the same time in line code
#name = "Bro"
#age = 21
#attractive = True
#name, age, attractive = "bro", 21, True

#print(name)
#rint(age)
#print(attractive)

#spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30
#Spongebob = patrick = Sandy = Squidward = 30

#print(Spongebob)

#STRING METHODS

#name = "Bro"
#print(len(name)) # len() indica a quantidade de caracteres "da variavel" chamado lengh method
#print(name.find(name)) #find() indica o posicionamento do caractere dentro da cadeia, no caso “Bro Code” ‘B’ está na primeira posição que é zero#
#print(name.capitalize()) #capitalize() poe o primeirop caracter em caixa alta#
#print(name.upper()) #upper() apresenta toda a cadeia de caracter em caixa alta#
#print(name.lower()) #lower() apresenta toda a cadeia de carater em caixa baixa"
#print(name.isdigit()) #isdigit() retorna o resultado logico 'booleano' que so é verdadeiro quando a cadeia é foramada somente por numeros, sem espaços letras ou qualquer tipo de caracter
#print(name.isalpha()) #isalpla() retorna o resultado logico 'booleano' que so é verdadeiro quando a cadeia é foramada somente por lestras do alfaberto, sem espaços numeros ou qualquer tipo de caracter
#print(name.count("e")) #cont("") conta os caracteres dentro da cadeia que pode ser um em especifico ou quantos ao todo quando não especificado
#print(name.replace("o","a")) # replace() substitui o primeiro elento pelo segundo
#print(name*3) #tambem é possivel repetir a cadeia de caracter fazendo essa multiplcação de variavel

#TYPE CAST = convert the data type of a value to another data type
#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#print(x)
#print(y)
#print(z)

#y = int(y) #esse type cast o torna permanente
#print(x)
#print(int(y)) #type cast aqui nesse caso há um type cast onde eu trasformo un elemento float em inteiro com int(), não é permanente!
#print(z)
#print("x is " +str(x)) #so se apresenta uma string com elementos de outra clase com o uso de type cast

# USER INPUT
#name = input("What is your name?: ") #input() sempre retorna uma str() e não é possivel usar-lo em operaçoes matematicas a não ser que seja usado da maneira abaixo 
#age = int(input("How old sre you?: ")) #int(input()) modo de usar input de modo a guardar variaveis inteiras e faser operaçoes matematicas
#print("Hello " +name) #name por ser um avariavel str é tranquilo <can only concatenate str to str>
#age = age +1
#height = float(input("how tall are you?: ")) #float(input) o mesmo vale para float <numeros xx.xx> o uso de type cast para idetificar a classe da variavel e guarda corretamente namemoria

#print(age)
#print(type(name))
#print(type(age))
#print("You are "+str(age)+" yers old") #can only concatenate str (not "int") to str, ou seja o correto é str(age). Ao receber in int(), ao apesenta-lo é preciso str(variable) 
#print("you are "+str(height)+" cm tall")

#MATH FUNCTIONS

#import math

#pi = -3.14

#x = 1
#y = 2
#z = 3

#float("%0.2f" % (variable)) # essa função retorna as casa decimais pos ponto, 2 para dua casa, 3 para 3 casas e assim por diante
#print(round(pi)) #round função matematica que arredonda o numero
#print(math.ceil(pi)) #A funcão ceil(x)retornar o menor numero interiro maior ou igual a x. 
#print(math.floor(pi)) #Similarmente, floor(x), retornar o maior numero inteiro menor ou igual a x
#print(abs(pi)) # a função abs() retorna o valor absoluto, 
#print(pow(pi,2)) # pow(x,y) retorna o expoente de x elevado a y 
#print(math.sqrt(36)) # math.sqrt(x) retorna a raiz quadrada de x
#print (max(1,2,3)) #max(x,y,z) retorna o maior numero
#print(min(1,2,3)) # min(x,y,z) retorna menor numero

#STRING SLICING = create a substring by estracting elements from another string index[] or slice()
#[start:stop:step]
#name = "marcio barros"
#first_name = name[:6] #[x:y] identifica o inicio e o final de seleção, x pode ser omitido caso se queira do começo a limite de y
#ast_name = name[7:] #[x:y] identifica do x posionamento indicado ao final y da string, y pode ser omitido caso se queira do começo ao final da instring
#funky_name = name[0:13:2] #[x:y:z] z indica o salto que sera selecionando
#reverse_name = name[::-1]  # [x:y:-1] apresenta a string de tras pra frente <- 
#print(first_name)

#each character within a string has a positive index and a negative index as well. End a negative index works almost exatly the same way except the character most on the right
# begins with a negative index of minus one and the character on the left of that would be it´s as if you´re counting backwards (contando de tras pra frente, da direita pra esquerda).
#Toda essa explicação para executar o exercio abaixo

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7,-4) # portando com objetivo de obter o dominio do site é usado o metodo de negative index no metodo slice. Não funciona o metodo index! Dai usar o metodo index para presentar
#print(website1[slice])
#print(website2[slice])

# if STATEMENT = a code of code that will execute if it´s condition is 

#age = int(input("How old are you?: "))
#if age == 100: # == são usados em condição de iqualdade, comparação
#    print("You are a centuty old!")
#elif age >= 18:
#    print("You are an adult!")
#elif age < 0: # a partir da condição if, podemos acidinar as demais codição com retorno verdadeiro com o comando elif
#    print ("you haven t been born yet")
#else: # se a condição if e elif não é verdadeira a condição else é executada 'senao'. else vem por ultimo quando todas as condiçoes if elif forem falsas
#    print("You are a child!")

# LOGICAL OPERATORS (and, or,not) = used to check if or two more condition etatment is true

#temp = int(input("What is the temprerature outside?: "))
#if not temp >= 0 and temp <= 30: 
#    print("the temperature is goof today")
#    print("go outside!")
#elif not temp < 0 or temp > 30:
#    print("the tempetature is bad today")
#    print("stay inside")

#WHILE LOOP = a statement that will execute it´s block of code, as long as it´s confition remains true

#name = None
#while not name:
#    name = input("enter your name: ")
#print("helo "+name)

# FOR LOOP = a statement that will executeit´s block of code a limited amount of times
#import time
#for i in range(10):
#    print(i)

#for i in range(50,60+1): #the first number is inclusive and and the second number is exclusive
#    print(i)
#for i in range(50, 70+1,2): #,2 é o inclemento
#    print(i)

#for i in "marcio barros": # em Python o comando tambem trabalha com strings 
#    print(i)

#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("Happy New Year!")

#NESTED LOOPS = The "inner loop" will finish all of it´s interations before finishing one iterationof the "outer lool"

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns? : "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol,end="") # em print o end="" faz com que seja apresentado na hoizontal, sem ele is items serão escritos um por um na vertical
#    print()

# LOOP CONTROL STETEMENTS =  change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iterarionof the loop
# pass = does nothing, acts as a placeholder
 
#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break # Esse é o brack, encerra o Loop

#phone_number = "123-456-7890"

#for i in phone_number:
#    if i == "-":
#        continue #skips to the next iterarion of the loop
#    print(i, end="") #em print o end="" faz com que seja apresentado na hoizontal, sem ele is items serão escritos um por um na vertical

#for i in range(1,21):# lebre-se em um range o ultimo número exclusive ou seja a contagem vai ate 20
#    if i == 13:
#        pass # does nothing, acts as a placeholder
#    else:
#        print(i,end=" ")

# LIST = used to store multiple itens in a single variable

#food = ["pizza","hamburger","hotdog","spagetti"] # List é uma matrix de uma dimenção cujo indices comçam a patir do zero
#food[0] = "sushi" # aqui o indice 0 foi atualizado com novo indice, de pizza passou a ser sushi
# food.append("ice cream") # food.append("x") acresenta o elemento x ao final da matriz ou list
#food.remove("hotdog") # food.remove("x") remove o elemento da matriz list
#food.pop() # food.pop() remove o ultimo elemento da matriz list
#food.insert(0,"cake") # food.insert(x,"y") insere o elemento(y) no inidice(x), consequentemente o demais elementos são reposisionados uma posição a frente
#food.sort() # food.sort() ordena a lista em orde alfabetica
#food.clear() # food.clear() # esvazia a lista, elimina os elementos
#for x in food: #apresentaçao basicas dos elemtos da matrix ou list food
#    print(x)
#print(food[0]) # forma busca um elemento da lista   

# 2Dlist = a list of list

#drinks = ["coffe","soda","tea"] # lista de drinks, pizza  e dessert cada uma delas possui seus indice individuais com contagem a partir do zero
#dinner = ["pizza","hamburger","hotdog"]
#dessert = ["cake","ice cream"]
#food = [drinks,dinner,dessert] # a list food contem em si as matrizes indicadas separadas por virgula 
# y são os indices individuais contido dentro de cada uma das matrizes: drinks, dinner e dessert 
#print(food[0][0]) # food([x][y]) é o modo de identificação dos indices, em que x (drinks,dinner,dessert) são os indices da matiz food.
