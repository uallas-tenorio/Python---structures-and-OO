from Conta import Conta

conta1 = Conta(123,"Uallas",200.0,1000.0)

conta2 = Conta(321, "Driele", 300.0, 1000.0)

conta3 = Conta(222,"Raul", 400.0, 1000.0)


conta1.saca(10.0)
conta1.extrato()

conta1.transfere(5.0,conta2)
conta1.extrato()
conta2.extrato()

print("Conta com propriedade: " + str(conta1.saldo))

conta1.saca(10000.0)

print(Conta.codigos_bancos())