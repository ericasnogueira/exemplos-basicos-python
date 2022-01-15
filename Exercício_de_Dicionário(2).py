"""
## 2. Case da Hashtag

Recentemente tivemos que fazer backup dos vídeos que temos hospedados no Vimeo. Acontece que não existe um botão de Download de todos os 
vídeos ao mesmo tempo, precisamos entrar em 1 por 1 e fazer o download manualmente.

A alternativa é gerar um código em Python que converse com a API do Vimeo (API é uma integração que as ferramentas 
abrem para programadores poderem fazer integrações dos seus próprios programas/scripts com a ferramenta).

Para resolver isso, a gente fez a integração e fizemos uma "requisição" de todos os vídeos para a Vimeo.
 Essa requisição dá como resposta para o nosso código isso:

"""


video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}
print(video)

"""
Repare que é um código completamente confuso, mas que no fim do dia é um dicionário.
Dentro dele queremos printar o link de download do vídeo para depois simplesmente clicar em todos os links e fazer o download de todos os vídeos.
No nosso caso, tínhamos uma lista com os mais de 2.000 vídeos (sendo cada vídeo um dicionário exatamente como esse aí em cima), 
e por isso fizemos exatamente esse mesmo procedimento que você vai construir aqui abaixo, só que dentro de um "for" para percorrer todos os vídeos. Não podemos disponibilizar a lista inteira por questões de segurança e proteção de dados mesmo, mas o dicionário acima já vale o exemplo. 
"""

for item in video:
    print(item)
print(video['download'][0]['link'])



