kmviagem = float(input('Digite quantos KM vai dar sua viagem: '))

if kmviagem < 200:
   print(f'A sua viagem ira custar {kmviagem * 0.5}')
else:
    print(f'A sua viagem ira custar {kmviagem * 0.45}')