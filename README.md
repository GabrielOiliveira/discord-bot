# Discord Bot de Registro de Membros

Bot em Python que dá boas-vindas a novos membros de um servidor Discord e libera o acesso quando eles se registram pelo comando `/registrar`.

## Funcionalidades
- Mensagem de boas-vindas automática no canal `registro` quando alguém entra no servidor
- Comando `/registrar Nick#123456`, que valida o formato, altera o apelido do membro e atribui o cargo `Membro`
- Respostas visíveis só para quem usou o comando
- Tratamento de erros (formato inválido, falta de permissão, cargo inexistente)

## Tecnologias
Python, discord.py (slash commands) e python-dotenv

## Como rodar
1. Instale as dependências: `pip install discord.py python-dotenv`
2. Crie um arquivo `.env` na pasta do projeto:
```
   DISCORD_TOKEN=seu_token
   GUILD_ID=id_do_servidor
```
3. No Developer Portal, ative o *Server Members Intent* do bot.
4. No servidor, crie o canal `registro` e o cargo `Membro`. O cargo do bot precisa ficar acima do cargo `Membro`, com permissão para gerenciar apelidos e cargos.
5. Execute: `python nome_do_arquivo.py`

## Possíveis melhorias
- Mensagens e nomes de canal/cargo configuráveis
- Registro (log) de quem se registrou
