class Worker:
    def __init__(self, name = None, value = None):
        self.worker = name
        self.wage = value
        self.next = None

class Hash:
    def __init__(self, num = 10):
        self.size = num
        self.tab = [None] * num

    def hashing(self, name):
        return ord(name[0]) % self.size
        
    def insert(self, worker):
        key = self.hashing(worker.worker)
        if self.tab[key]:
            aux = self.tab[key]
            if aux.next:
                while aux.next:
                    aux = aux.next
                aux.next = worker
            else:
                self.tab[key].next = worker
        else:
            self.tab[key] = worker

    def search(self, name):
        finded = False
        key = self.hashing(name[0])
        if self.tab[key]:
            aux = self.tab[key]
            while aux.next:
                aux = aux.next
                if aux.worker == name:
                    print(f'\n\n < O funcionário(a) {aux.worker} recebe R$ {aux.wage}! > \n\n')
                    finded = True
            if not finded:
                print('O funcionário informado não foi encontrado. Tente novamente!')
        else:
            print('Funcionário não encontrado, tente novamente!')

    def printOut(self):
        key_block = len(self.tab)
        key = 0
        print('\n\n')
        while key < key_block:
            if self.tab[key]:
                aux = self.tab[key]
                while aux.next:
                    print(f'< O funcionário(a) {aux.worker} recebe R$ {aux.wage}! >')
                    aux = aux.next
                print(f'< O funcionário(a) {aux.worker} recebe R$ {aux.wage}! >')
            key += 1
            
def menu():
    print('\n\n| SISTEMA DE FUNCIONÁRIOS |\n')
    print('1 - Cadastrar funcionário;\n2 - Buscar salário;\n3 - Sair;\n4 - Imprimir lista.')
    option = int (input('\nInforme o que deseja fazer: '))
    return option

def menu1(self):
    name = input ('\n\nInforme o nome do funcionário: ')
    wage = float (input('Informe o salário do funcionário: '))
    worker = Worker(name, wage)
    self.insert(worker)
    print('\n\n< Funcionário cadastrado com sucesso! >\n\n')

def menu2(self):
    name = input ('\n\nInforme o nome do funcionário: ')
    self.search(name)

def menu4(self):
    self.printOut()

hashTab = Hash()
option = menu()

while option != 3:
    if option == 1:
        menu1(hashTab)
    elif option == 2:
        menu2(hashTab)
    elif option == 4:
        menu4(hashTab)
    else:
        print('Comando não reconhecido, tente novamente!')
    option = menu()
print('Sistema encerrado!')