# Chatbot WhatsApp com Flask e Twilio

Este projeto utiliza Flask em conjunto com o serviço Twilio para criar um chatbot funcional e interativo no WhatsApp.

## Passo a Passo para Configuração:

### 1. Crie uma conta gratuita na Twilio

Comece criando uma conta gratuita na Twilio:
[https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio)

### 2. Conexão com o WhatsApp através da Twilio

Para se conectar ao WhatsApp através da Twilio pela primeira vez, envie a mensagem indicada para o número fornecido na seção "Sandbox Participants":
[https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1)

## 3. Instalação e Configuração:
Antes de começar, é recomendado criar um ambiente virtual (venv) para o projeto. Isso irá isolar as dependências do projeto e evitar conflitos com outros projetos ou pacotes instalados globalmente em sua máquina.

```shell
python3 -m venv nome-do-venv
```

Em seguida, ative o venv com o seguinte comando:

```shell
source nome-do-venv/bin/activate
```

Instalar dependências.

```shell
pip install -r requirements.txt
```

Criar um arquivo `.env` e altere as variaveis de ambiente

```shell
cp .env.sample .env
```

### 4. Inicialização da Aplicação Flask

Após configurar o ambiente, inicie a aplicação em Flask executando o comando:
```flask run```

### 5. Configurando o Webhook na Twilio

Para que a Twilio possa comunicar-se com a sua aplicação Flask, é necessário fornecer uma URL pública. Uma maneira fácil de fazer isso é utilizando a ferramenta [ngrok](https://ngrok.com/). Após iniciar sua aplicação Flask, execute o ngrok para obter uma URL pública que direcione para sua aplicação local.

Na seção de sandbox da Twilio para o WhatsApp, preencha o campo "When a message comes in" com a URL fornecida pelo ngrok e adicione `/bot` ao final.

Exemplo:

<https://c046-2804-d4b-9a4d-9a00-9830-f5de-a0c-95e5.ngrok-free.app/bot>




