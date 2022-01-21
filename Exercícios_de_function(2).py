"""
Exercício

1-Function para Análise de indicadores
    A maioria das empresas tem suas próprias regras para cálculos de indicadores
        ° Algumas empresas definem que um cliente é considerado um cliente inadimplete quando ele está
        devendo acima de x reais e por mais de x dias.
        ° Algumas empresas definem que um vendedor bateu a meta quando ele vendeu acima de x reais (outras
        ainda analisam não só as vendas desse vendedor, mas também da loja ou unidade de negócios que ele faz
        parte, ou ainda uma avalição qualitativa)
        °Algumas empresas definem que o Produto está em 'falta' no estoque quando ele está abaixo de um
        nível mínimo quando um cliente insere um novo pedido daquele produto
        ° E assim vai para dezenas de indicadores.

O ponto importante é, cada empresa tem alguma adaptadação do cáculo de indicadores. E normalmente se formas 
formos analisar esses indicadores é interessante ter funções que façam todo o trabalho de análise deles.
Por isso, Vamos construir 2 exemplos aqui:

Item 1 : crie uma função que calcula o percentual de Stockout de uma empresa
   ° O % de stockout é dado por (Vendas Perdidas por Estoque) / (Vendas Concluídas + Vendas Perdidas
    por Estoque) -> essas vendas são dadas em valor total (dinheiro) e não em quantidade de vendas
   ° Seu programa recebe um dicionário com todas as vendas da empresa, o status dela (se foi Concluída 
    ou Cancelada) e, caso tenha sido Cancelada, o motivo de Cancelamento. O formato é o seguinte:
"""
"""
vendas = {
    'VE0001': (15000, 'Concluído', ''),
    'VE0002': (13300, 'Cancelado', 'Cancelado pelo Cliente'),
    'VE0003': (12000, 'Concluído', ''),
    ...
}
"""

#Para reforçar : As vendas Canceladas por qualquer outro motivo que não seja de ESTOQUE não dever ser 
# consideradas para a conta do STOCKOUT.

vendas = {'VE0001': (9868,'Concluído',''),'VE0002': (9642,'Concluído',''),
'VE0003': (6007,'Concluído',''),'VE0004': (15562,'Concluído',''),
'VE0005': (18752,'Cancelado','Estoque em Falta'),'VE0006':
 (16358,'Cancelado','Estoque em Falta'),'VE0007':
  (17045,'Concluído',''),'VE0008': (12230,'Concluído',''),
  'VE0009': (6747,'Concluído',''),'VE0010': (15114,'Concluído',''),
  'VE0011': (12497,'Concluído',''),'VE0012': (6001,'Concluído',''),
  'VE0013': (16227,'Cancelado','Cancelada pelo Cliente'),'VE0014': (16150,'Concluído',''),
  'VE0015': (17705,'Concluído',''),'VE0016': (9978,'Concluído',''),'VE0017': (4266,'Concluído',''),
  'VE0018': (11531,'Concluído',''),'VE0019': (10352,'Cancelado','Cancelada pelo Cliente'),
  'VE0020': (16544,'Concluído',''),'VE0021': (15488,'Concluído',''),
  'VE0022': (15828,'Concluído',''),'VE0023': (1218,'Concluído',''),
  'VE0024': (11560,'Concluído',''),'VE0025': (14220,'Concluído',''),
  'VE0026': (17839,'Concluído',''),'VE0027': (4050,'Concluído',''),
  'VE0028': (7594,'Cancelado','Estoque em Falta'),'VE0029': (19586,'Concluído',''),
  'VE0030': (8453,'Concluído',''),'VE0031': (3589,'Concluído',''),
  'VE0032': (13472,'Cancelado','Cancelada pelo Cliente'),
  'VE0033': (16994,'Concluído',''),'VE0034': (2139,'Concluído',''),
  'VE0035': (10173,'Concluído',''),'VE0036': (17784,'Cancelado','Estoque em Falta'),
  'VE0037': (12214,'Concluído',''),'VE0038': (5878,'Concluído',''),'VE0039': (2622,'Concluído',''),
  'VE0040': (9765,'Concluído',''),'VE0041': (8872,'Concluído',''),'VE0042': (16543,'Concluído',''),
  'VE0043': (8994,'Concluído',''),'VE0044': (4332,'Concluído',''),'VE0045': (19679,'Concluído',''),
  'VE0046': (14968,'Concluído',''),'VE0047': (6352,'Concluído',''),'VE0048': (11461,'Concluído',''),
  'VE0049': (5285,'Concluído',''),'VE0050': (11639,'Concluído',''),'VE0051': (6023,'Concluído',''),
  'VE0052': (4943,'Concluído',''),'VE0053': (5654,'Concluído',''),'VE0054': (11734,'Concluído',''),
  'VE0055': (2742,'Concluído',''),'VE0056': (5380,'Cancelado','Estoque em Falta'),
  'VE0057': (5578,'Concluído',''),'VE0058': (1897,'Concluído',''),'VE0059': (7857,'Concluído',''),
  'VE0060': (4472,'Concluído',''),'VE0061': (19874,'Concluído',''),
  'VE0062': (13323,'Cancelado','Cancelada pelo Cliente'),'VE0063': (5821,'Concluído',''),
  'VE0064': (4410,'Concluído',''),'VE0065': (16676,'Concluído',''),'VE0066': (10577,'Concluído',''),
  'VE0067': (10627,'Concluído',''),'VE0068': (1987,'Concluído',''),'VE0069': (13197,'Concluído',''),
  'VE0070': (15063,'Concluído',''),'VE0071': (14363,'Concluído',''),'VE0072': (10452,'Concluído',''),
  'VE0073': (15376,'Concluído',''),'VE0074': (4661,'Concluído',''),'VE0075': (13287,'Concluído',''),
  'VE0076': (8278,'Concluído',''),'VE0077': (7134,'Concluído',''),'VE0078': (16568,'Concluído',''),
  'VE0079': (17732,'Concluído',''),'VE0080': (5127,'Concluído',''),'VE0081': (4582,'Concluído',''),
  'VE0082': (14804,'Cancelado','Cancelada pelo Cliente'),'VE0083': (12362,'Concluído',''),
  'VE0084': (1148,'Concluído',''),'VE0085': (14018,'Concluído',''),'VE0086': (15891,'Concluído',''),
  'VE0087': (4517,'Concluído',''),'VE0088': (1770,'Concluído',''),'VE0089': (14926,'Concluído',''),
  'VE0090': (13627,'Concluído',''),'VE0091': (3047,'Concluído',''),'VE0092': (13924,'Concluído',''),
  'VE0093': (7158,'Concluído',''),'VE0094': (5942,'Concluído',''),'VE0095': (13480,'Concluído',''),
  'VE0096': (17686,'Concluído',''),'VE0097': (5722,'Cancelado','Cancelada pelo Cliente'),
  'VE0098': (16963,'Concluído',''),'VE0099': (14225,'Concluído',''),'VE0100': (12553,'Concluído',''),
  'VE0101': (18047,'Concluído',''),'VE0102': (11420,'Concluído',''),'VE0103': (6191,'Concluído',''),
  'VE0104': (8388,'Concluído',''),'VE0105': (17210,'Concluído',''),'VE0106': (12217,'Concluído',''),
  'VE0107': (8984,'Concluído',''),'VE0108': (7638,'Cancelado','Cancelada pelo Cliente'),
  'VE0109': (8462,'Concluído',''),'VE0110': (14081,'Concluído',''),'VE0111': (10842,'Concluído',''),
  'VE0112': (13261,'Concluído',''),'VE0113': (16953,'Cancelado','Estoque em Falta'),
  'VE0114': (5343,'Concluído',''),'VE0115': (4734,'Concluído',''),
  'VE0116': (13606,'Cancelado','Cancelada pelo Cliente'),'VE0117': (17106,'Cancelado','Estoque em Falta'),
  'VE0118': (17704,'Concluído',''),'VE0119': (12242,'Concluído',''),
  'VE0120': (7476,'Cancelado','Estoque em Falta'),'VE0121': (18408,'Concluído',''),
  'VE0122': (13612,'Concluído',''),'VE0123': (18198,'Concluído',''),'VE0124': (4844,'Concluído',''),
  'VE0125': (12750,'Concluído',''),'VE0126': (11969,'Concluído',''),'VE0127': (15337,'Concluído',''),
  'VE0128': (1100,'Concluído',''),'VE0129': (18893,'Concluído',''),'VE0130': (15850,'Concluído',''),
  'VE0131': (2097,'Concluído',''),'VE0132': (11636,'Cancelado','Estoque em Falta'),
  'VE0133': (12603,'Concluído',''),'VE0134': (10769,'Concluído',''),'VE0135': (11016,'Concluído',''),
  'VE0136': (14556,'Concluído',''),'VE0137': (1389,'Concluído',''),'VE0138': (11681,'Concluído',''),
  'VE0139': (16759,'Cancelado','Cancelada pelo Cliente'),'VE0140': (16317,'Concluído',''),
  'VE0141': (5965,'Concluído',''),'VE0142': (4493,'Concluído',''),'VE0143': (5398,'Concluído',''),
  'VE0144': (9875,'Concluído',''),'VE0145': (17492,'Concluído',''),'VE0146': (7473,'Concluído',''),
  'VE0147': (10284,'Concluído',''),'VE0148': (10778,'Concluído',''),'VE0149': (2227,'Concluído',''),
  'VE0150': (14157,'Concluído',''),'VE0151': (9516,'Concluído',''),'VE0152': (9824,'Concluído',''),
  'VE0153': (5118,'Concluído',''),'VE0154': (5123,'Concluído',''),'VE0155': (2697,'Concluído',''),
  'VE0156': (19024,'Concluído',''),'VE0157': (5128,'Concluído',''),
  'VE0158': (8293,'Cancelado','Estoque em Falta'),'VE0159': (18782,'Concluído',''),
  'VE0160': (12182,'Concluído',''),'VE0161': (9063,'Concluído',''),'VE0162': (17608,'Concluído',''),
  'VE0163': (8456,'Cancelado','Cancelada pelo Cliente'),'VE0164': (1291,'Concluído',''),
  'VE0165': (14018,'Concluído',''),'VE0166': (2791,'Concluído',''),'VE0167': (17953,'Concluído',''),
  'VE0168': (14627,'Concluído',''),'VE0169': (3296,'Concluído',''),'VE0170': (1863,'Concluído',''),
  'VE0171': (4719,'Concluído',''),'VE0172': (15060,'Concluído',''),
  'VE0173': (2596,'Cancelado','Cancelada pelo Cliente'),'VE0174': (4919,'Concluído',''),
  'VE0175': (13770,'Concluído',''),'VE0176': (15041,'Cancelado','Estoque em Falta'),
  'VE0177': (6702,'Concluído',''),'VE0178': (9989,'Concluído',''),'VE0179': (5135,'Concluído',''),
  'VE0180': (13337,'Concluído',''),'VE0181': (13457,'Concluído',''),'VE0182': (17218,'Concluído',''),
  'VE0183': (6424,'Concluído',''),'VE0184': (5478,'Concluído',''),
  'VE0185': (10478,'Cancelado','Cancelada pelo Cliente'),'VE0186': (3240,'Concluído',''),
  'VE0187': (16503,'Concluído',''),'VE0188': (12762,'Concluído',''),
  'VE0189': (6985,'Cancelado','Cancelada pelo Cliente'),'VE0190': (13013,'Concluído',''),
  'VE0191': (5706,'Concluído',''),'VE0192': (6521,'Cancelado','Estoque em Falta'),
  'VE0193': (12904,'Concluído',''),'VE0194': (14691,'Concluído',''),'VE0195': (19338,'Concluído',''),
  'VE0196': (4556,'Cancelado','Cancelada pelo Cliente'),'VE0197': (9653,'Concluído',''),
  'VE0198': (4617,'Concluído',''),'VE0199': (4717,'Concluído',''),'VE0200': (8366,'Concluído','')}


# função aqui
def calculo_stockout(dicionario_vendas):
    numerador = 0
    denominador = 0
    #percorrendo o dicionario
    for venda in dicionario_vendas:
        valor, status, motivo = dicionario_vendas[venda]
        if status == "Concluído" : 
            denominador += valor  # adicionando o valor no denominador
        elif status == "Cancelado" and motivo == "Estoque em Falta" :      
            denominador += valor     #adicionando  numerador e o denominador
            numerador += valor          
    return numerador / denominador 

#rodando a função no dicionário para ver se está funcionando

print(f'{calculo_stockout(vendas):.2%}')
