#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
# do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Digite o tamnho do arquvio em MB: '))
velocidade_internet = int(input('Digite a velocidade da internet em MBPS: '))

segundos_para_baixar = tamanho_arquivo / velocidade_internet
segundos_para_minutos = (segundos_para_baixar / 60)
print(f'Você ira demorar {segundos_para_minutos:.1f} minutos para baixar o arquivo no tamanho de {tamanho_arquivo:.0f} MB com internet'
      f'de {velocidade_internet} MBPS' )