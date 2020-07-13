class Conta:

    #Criação dos atributos
    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #função para exibir o extrato
    def extrato(self):
        print("Valor{}. Cliente {}".format(self.__saldo,self.__titular))

    #função para depositar valor
    def deposita(self, valor):
        self.__saldo += valor


    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    # função para sacar valor
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Limite excedido")

    # função para transferir valor
    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    # função Get para retornar o saldo
    #def get_saldo(self):
    #    return self.__saldo                 substituido por propriedade
    @property
    def saldo(self):
        return self.__saldo

    # função Get para retornar o titular
    #def get_titular(self):
    #    return self.__titular               substituido por propriedade
    @property
    def titular(self):
        return self.__titular

    # função Get para retornar o limite
    # def get_limite(self):
    #    return self.__limite                substituido por propriedade
    @property
    def limite(self):
        return self.__limite

    # função Set para alterar o limite
    #def set_limite(self, limite):
    #    self.__limite = limite             substituido por setter
    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
