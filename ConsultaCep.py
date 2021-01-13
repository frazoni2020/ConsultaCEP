import requests
def main():
  print("Consulta Cep")
 
  cep = input("Digite o cep para a consulta (APENAS OS NUMEROS): ")
 
  if len(cep)!= 8:
    print("Cep invalido")
    exit()
 
  request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
  data = request.json()
  if "erro" not in data:
    print("====>CEP ENCONTRADO<====")
    print(f'CEP:{cep}')
    print('RUA : {}'.format(data['logradouro']))
    print('COMPLEMENTO: {}'.format(data['complemento']))
    print('LOCALIDADE: {}'.format(data['localidade']))
    print('UF: {}'.format(data['uf']))
  
  else:
    print("CEP INEXISTENTE")
 
  opção = str(input('DESEJA REALIZAR NOVA CONSULTA [SIM/NÃO]')).upper().strip()
  if opção == "SIM":
    main()
  else:
    print("Saindo")
 
 
if __name__ == '__main__':
  main()