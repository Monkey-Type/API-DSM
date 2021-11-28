<br id="topo">

<h1 align="center"> FATEC, SJC - 1º Semestre DSM</h1>

> <p>Equipe:</p>
# :monkey::computer: Monkey Type 

<h2 align="center" >Sumário </h2>


 <p align="center"> |
    <a href="#sobre">Sobre</a> | 
    <a href="#sprints">Sprints</a> | 
    <a href="#qs"><b>Quick Start</b></a> | 
    <a href="#backlog">Product Backlog</a> | 
    <a href="#user-stories">User Stories</a> | 
    <a href="#preview">Preview</a> | 
    <a href="#tecnologias">Tecnologias</a> | 
    <a href="#equipe">Equipe</a> |
    
</p>
   
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

<p align="justify">Em face de uma pandemia mundial instituições de ensino do mundo todo enfrentaram o grande desafio de adaptarem  as atividades acadêmicas para o ensino remoto em um curto espaço de tempo. Com isso o aumento do uso de ferramentas de correios eletrônicos para comunicação dentro das instituições cresceu de forma exponencial levando a diversos problemas por perda de informações. Com o intuito de resolver esse problema, a <strong>FATEC São José dos Campos</strong> propôs aos alunos do 1° semestre do curso de <strong>Desenvolvimento de Software Multiplataforma (DSM)</strong>, o desenvolvimento de um portal de informações para o Corpo Docente, Discente e Administrativo da Fatec SJC capaz de exibir e gerar de forma seletiva e controlada os avisos gerais ou específicos de cada usuário, respeitando as respectivas hierarquias dentro da universidade com o intuíto de melhorar a comunicação interna da instituição.</p>

>### Status do Projeto: Finalizado ✔
<br>


> [Voltar ao Topo](#topo) ☝️

<span id="sprints">
<br>

## :running: Sprints

| Sprint | Link | Início | Entrega | Status |
|--- |--- |--- |--- |:---:
| 01 | [Sprint 01](#sprint1) | 08/09/2021 | 19/09/2021 | ✔ |
| 02 | [Sprint 02](#sprint2) | 20/09/2021 | 10/10/2021 | ✔ |
| 03 | [Sprint 03](#sprint3) | 18/10/2021 | 07/11/2021 | ✔ |
| 04 | [Sprint 04](#sprint4) | 08/11/2021 | 28/11/2021 | ✔ |

<br>

> [Voltar ao Topo](#topo) ☝️

<span id="qs">

<br>

# Quick Start


Tendo a ferramenta Git e o Python instalados em seu computador:
- Abra o Prompt de Comando no caminho de um novo diretório e copie o seguinte comando para clonar o nosso repositório:

```
git clone https://github.com/Monkey-Type/API-DSM.git
```
- Dentro da pasta root do projeto, crie um Ambiente Virtual com o seguite comando:
```
python3 -m venv venv
```
ou caso tenha o python3 já instalado
```
python -m venv venv
```
(Obs.: caso você utilize um sistema operacional diferente do Windows, verifique comandos alternativos neste [Link](https://docs.python.org/pt-br/3/library/venv.html) .)
- Isso criará o diretório  ```venv```. Agora ative o Ambiente Virtual com o comando:
```
venv\Scripts\activate
```
- Você deverá ver o ambiente virtual ativado antes do caminho do seu diretório, assim:
``` (venv) C:\...```
- Agora instale as dependências do projeto:
``` 
pip install -r requirements.txt
```
- Agora certifique-se que está no diretório ```src``` e para executar a aplicação, execute o comando:
```
flask run
```
- A aplicação estará rodando por padrão na porta :5000, caso já tenha uma aplicação rodando nesta porta, certifique-se de selecionar uma porta livre na hora de rodar a aplicação:
``` 
flask run -p 9000
```
- Vá até o caminho indicado http://127.0.0.1:5000/ ou http://127.0.0.1:9000/ e navegue na aplicação.

<br>

> [Voltar ao Topo](#topo) ☝️

<span id="backlog">

<br>

## :page_with_curl: Product Backlog 

> - RF - Requisito Funcional

> - RNF - Requisito Não Funcional

<table>
    <tr>
        <td>REQUISITO FUNCIONAL_ID</td>
        <td>USER STORIES_ID</td>
        <td align="center">REQUISITOS</td>
        <td>SPRINTS</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td>#01</td>
        <td> Criação de um protótipo navegável</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RF - 2</td>
        <td>#02</td>
        <td> A Identidade Visual do sistema deve levar em consideração a identidade visual da Fatec SJC</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td>#03</td>
        <td> Interface com navegação intuitiva</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RF - 4</td>
        <td>#05 #14 #15 #16</td>
        <td>  Envio de informações para divulgação via sistema (Administrador)</td>
        <td>#02 ✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>#07 #11 #13</td>
        <td> Visualização de informações de divulgação via sistema de modo seletivo (filtro por data, interessados, curso, etc.)</td>
        <td>#02 #03 ✔</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td>#08</td>
        <td>  Acesso às informações do sistema através de perfis de usuário/papeis (adm,usuário comum, coordenador de curso, etc.)</td>
        <td>#02 #03 ✔</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td>#21</td>
        <td>  Quem criou a mensagem é o único com poder de exclusão da mesma</td>
        <td>#02 #03 ✔</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td>#09 #17</td>
        <td>  Cada Usuário deve ter o poder de enviar informes/anúncios a determinados grupos de usuários e receber mensagens de determinado grupos de usuários numa hierarquia de USERS</td>
        <td>#02 #03 ✔</td>
    </tr>
    <tr>
        <td>RF - 9</td>
        <td>#22</td>
        <td>   Nas categoria de usuário onde há uma hierarquia  (ex.: chefe da secretaria e assistente da secretaria), deverá haver a opção de habilitar quem pode mandar mensagem dentro desse grupo de usuário</td>
        <td>#03 #04 ✔</td>
    </tr>
    <tr>
        <td>RF - 10</td>
        <td>#18 #20</td>
        <td>  O usuário deve ter a automia de marcar a mensagem como lida e não lida (arquivar). Será importante manter um histórico de mensagem.</td>
        <td>#03 #04 ✔</td>
    </tr>
    <tr>
        <td>RF - 11</td>
        <td>#06 #10 #12</td>
        <td>  Possibilidade de anexar documentos (e.g.: PDFs, Docs, etc)</td>
        <td>#03 #04 ✔</td>
    </tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>RNF - 1</td>
        <td></td>
        <td>   Utilizar HTML5 para arquitetura da informação da aplicação</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RNF - 2</td>
        <td></td>
        <td>  Utilizar CSS 3 para especificação do layout e demais características de renderização da interface com o usuário</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RNF - 3</td>
        <td></td>
        <td> Utilizar JavaScript no front end (obs.: pode fazer uso de frameworks)</td>
        <td>#01 ✔</td>
    </tr>
    <tr>
        <td>RNF - 4</td>
        <td></td>
        <td> Desenvolver o back end com a linguagem Python 3+ e o 
microframework Flask</td>
        <td>#02 ✔</td>
    </tr>
    <tr>
        <td>RNF - 5</td>
        <td></td>
        <td> Utilizar o sistema gerenciador de banco de dados 
MariaDB/MySQL/PostGresSQL</td>
        <td>#02 ✔</td>
    </tr>
    <tr>
        <td>RNF - 6</td>
        <td></td>
        <td>  Sistema responsivo</td>
        <td>#02 #03 ✔</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️

<span id="user-stories">
<br>

## :page_with_curl: User Stories 
<br>


<table>
    <tr>
        <td align="center">US__ID</td>
        <td align="center">RF_ID</td>
        <td align="center">REMETENTE</td>
        <td align="center">INSTRUÇÃO</td>
        <td align="center">FINALIDADE</td>
    </tr>
    <tr>
        <td align="center">US-1</td>
        <td align="center">#01</td>
        <td>Cliente</td>
        <td>Como Cliente, eu quero poder testar a aplicação antes de usa-la</td>
        <td>Para que eu simule a experiência que meus usuários terão na minha aplicação</td>
    </tr>
    <tr>
        <td align="center">US-2</td>
        <td align="center">#02</td>
        <td>Cliente</td>
        <td>Como Cliente, eu quero que o design siga a identidade visual da Fatec São Jose dos Campos</td>
        <td>Para que os usuários saibam que estão em um site da Fatec de São Jose dos Campos</td>
    </tr>
    <tr>
        <td align="center">US-3</td>
        <td align="center">#03</td>
        <td>Cliente</td>
        <td>Como Cliente, eu quero que a interface seja intuitiva</td>
        <td>Para que os usuários consigam aprender a usar a aplicação facilmente</td>
    </tr>
    <tr>
        <td align="center">US-4</td>
        <td align="center">RNF-6</td>
        <td>Cliente</td>
        <td>Como cliente, eu quero que interface seja responsiva</td>
        <td>Para que os usuários consigam ter facidade de acesso em qualquer dispositívo</td>
    </tr>
    <tr>
        <td align="center">US-5</td>
        <td align="center">#04</td>
        <td>Administrador/
        Secretaria</td>
        <td>Como usuário administrador, eu quero enviar as informações</td>
        <td>Para que qualquer pessoa que possuam uma conta fatec consiga visualizar essas informações</td>
    </tr>
    <tr>
        <td align="center">US-6</td>
        <td align="center">#11</td>
        <td>Administrador/
        Secretaria</td>
        <td>Como usuário administrador, eu quero poder anexar arquivos e documentos</td>
        <td>Para que alunos, professores e a comunidade da fatec possa vizualizar e fazer download desses arquivos/documentos</td>
    </tr>
    <tr>
        <td align="center">US-7</td>
        <td align="center">#05</td>
        <td>Administrador/
        Secretaria</td>
        <td>Como usuária administrador, eu quero poder filtrar as informações de modo seletivo (data, cursos, etc)</td>
        <td>Para gerenciar o que cada cargo envia na plataforma</td>
    </tr>
    <tr>
        <td align="center">US-8</td>
        <td align="center">#06</td>
        <td>Administrador/
        Secretaria</td>
        <td>Como usuário administrador, eu quero que a plataforma possua cargos (adm, aluno, professor)</td>
        <td>Para que cada cargo apenas veja o que é de seu interesse/autoridade</td>
    </tr>
    <tr>
        <td align="center">US-9</td>
        <td align="center">#08</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder enviar anúncios</td>
        <td>Para que alunos, outros professores ou secretaria que uma conta fatec consigam visualizar essas informações</td>
    </tr>
    <tr>
        <td align="center">US-10</td>
        <td align="center">#11</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder anexar arquivos, documentos, etc</td>
        <td>Para que alunos consigam acessar e fazer o download desses arquivos, documentos, etc</td>
    </tr>
    <tr>
        <td align="center">US-11</td>
        <td align="center">#05</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder filtrar as informações que recebo por data de modo seletivo (curso, interessados, etc)</td>
        <td>Para que não exista conflito de informações e para que eu consiga ver apenas o necessário</td>
    </tr>
    <tr>
        <td align="center">US-12</td>
        <td align="center">#11</td>
        <td>Aluno</td>
        <td>Como aluno, eu quero poder enviar trabalhos, provas, arquivos em geral</td>
        <td>Para que meu professor possa visualizar e baixar esses arquivos</td>
    </tr>
    <tr>
        <td align="center">US-13</td>
        <td align="center">#05</td>
        <td>Aluno</td>
        <td>Como aluno, eu quero poder filtrar as informações do sistema de maneira seletiva (materia, interessados, etc)</td>
        <td>Para que eu consigo ver apenas o necessário e me organizar melhor pela plataforma</td>
    </tr>
    <tr>
        <td align="center">US-14</td>
        <td align="center">#04</td>
        <td>Coordenador</td>
        <td>Como Coordenador, quero poder criar informes</td>
        <td>Para que todos os Usuários da FATEC possam vê-los</td>
    </tr>
    <tr>
        <td align="center">US-15</td>
        <td align="center">#04</td>
        <td>Diretor</td>
        <td> Como Diretor, quero poder criar informes</td>
        <td>Para que todos os Usuários da FATEC possam vê-los</td>
    </tr>
    <tr>
        <td align="center">US-16</td>
        <td align="center">#04</td>
        <td>Secretaria Administrativa</td>
        <td> Como Usuário da Secretaria Administrativa quero poder criar informes</td>
        <td>Para que todo o corpo docente da FATEC possa ve-los</td>
    </tr>
    <tr>
        <td align="center">US-17</td>
        <td align="center">#08</td>
        <td>Secretaria Acadêmica</td>
        <td> Como Usuário da Secretaria Acadêmica quero poder divulgar informes</td>
        <td>Para que qualquer usuário que seja Aluno ou Professor possa ve-los</td>
    </tr>
    <tr>
        <td align="center">US-18</td>
        <td align="center">#10</td>
        <td>Usuário Geral</td>
        <td> Como Usuário quero poder marcar as mensagens como lidas</td>
        <td>Para que  as mensagens lidas saiam da minha lista de mensagens</td>
    </tr>
    <tr>
        <td align="center">US-20</td>
        <td align="center">#10</td>
        <td>Administrador</td>
        <td> Como Administrador quero que seja mantido um histórico de mensagens (arquivadas)</td>
        <td>Para que seja possível revê-las</td>
    </tr>
    <tr>
        <td align="center">US-21</td>
        <td align="center">#07</td>
        <td>Usuário Geral</td>
        <td> Como Usuário que pode enviar anúncios e mensagens quero que apenas eu possa excluí-las.</td>
        <td>Para que eu possua um histórico acessível do que eu gerei</td>
    </tr>
    <tr>
        <td align="center">US-22</td>
        <td align="center">#09</td>
        <td>Secretaria</td>
        <td> Como Usuário que possuí hierarquia interna quero poder habilitar quais Usuários podem ou não enviar mensagens dentro do meu grupo</td>
        <td>Para que eu possa manter o controle dos Usuários dentro da hierarquia da minha categoria</td>
    </tr>
</table>


<br>

> [Voltar ao Topo](#topo) ☝️

<span id="preview">

## :movie_camera: Preview da Aplicação
<br>

[![PREVIEW DA APLICAÇÃO](https://img.youtube.com/vi/tgTBTtuiZNc/0.jpg)](https://www.youtube.com/watch?v=tgTBTtuiZNc)

<br>

> [Voltar ao Topo](#topo) ☝️

<span id="tecnologias">

## :computer: Tecnologias e Ferramentas Usadas
![](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)

![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![](https://img.shields.io/badge/Adobe%20XD-470137?style=for-the-badge&logo=Adobe%20XD&logoColor=#FF61F6)
![](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)


[](https://user-images.githubusercontent.com/58151594/136624912-b1371a56-89e8-4d4f-aa4f-331a7e683a32.jpg)


<br>

> Tecnologias links Úteis:
- [HTML5](https://pt.wikipedia.org/wiki/HTML5)
- [CSS3](https://pt.wikipedia.org/wiki/CSS3)
- [JavaScript](https://pt.wikipedia.org/wiki/JavaScript)
- [Adobe XD](https://www.adobe.com/br/products/xd.html)
- [GitHub](https://github.com)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [SQLite](https://www.sqlite.org/download.html)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask)
- [Python](https://python.org.br/instalacao-windows/)
- [Slack](https://slack.com/intl/pt-br/)
- [Discord](https://discord.com/download)

<br>

<br>

## Modelo Conceitual e Lógico do Banco de Dados

### Modelo Lógico

![BDLOGICO](https://github.com/Monkey-Type/API-DSM/blob/main/docs/Modelo_Conceitual_BD.jpeg)

### Modelo Conceitual

![BDCONCEITUAL](https://github.com/Monkey-Type/API-DSM/blob/main/docs/Modelo_Logico_BD.jpg)

<br>


> [Voltar ao Topo](#topo) ☝️

<br>

<span id="equipe">

## :monkey::computer: Equipe
<br>

<table>
<tr>
        <td>Nome</td>
        <td>Posição</td>
        <td>GitHub</td>
        <td>LinkedIn</td>
    </tr>
    <tr>
        <td>Rafael da Silva Peres</td>
        <td>Product Owner</td>
        <td><a href="https://github.com/Rafaeldasilvaperes"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/rafael-da-silva-peres-ba4228bb/"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
    <tr>
        <td>Gabriel Souza Bicho Nunes</td>
        <td>Scrum Master</td>
        <td><a href="https://github.com/ZeroPirata"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/gabriel-souza-bicho-nunes-429191185/"><span style="color:gold"><b>LinkedIn<b></span></td>
    </tr>
    <tr>
        <td>Gustavo Pereira</td>
        <td>DEV</td>
        <td><a href="https://github.com/Foot-G"><span style="color:gold"><b>GitHub<b></span></td>
        <td><a href="COLOCAR O SEU LINK PARA O LINKEDIN AQUI MEUBOMSENHOR"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
    <tr>
        <td>Leonardo Queiróz Machado</td>
        <td>DEV</td>
        <td><a href="https://github.com/Lrd-M"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/leonardo-queir%C3%B3z-machado-606321198/"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
    <tr>
        <td>Lucas Ferreira da Costa</td>
        <td>DEV</td>
        <td><a href="https://github.com/ddaiwon"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/lucas-costa-a49a01219/"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
    <tr>
        <td>Rafael Leonardo Lopes</td>
        <td>DEV</td>
        <td><a href="https://github.com/Rafael-leonardo"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/rafael-leonardo-lopes/"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
    <tr>
        <td>Vinícius Andrade B.</td>
        <td>DEV</td>
        <td><a href="https://github.com/ViniciusAndBar"><span style="color:gold"><b>GitHub</b></span></td>
        <td><a href="https://www.linkedin.com/in/vin%C3%ADcius-barbosa-78111a206/"><span style="color:gold"><b>LinkedIn</b></span></td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️

<br>

<span id="sprint1">

## Sprint 01 :running:
<br>

<p align="justify">Na <b>Primeira Sprint</b> fizemos o levantamento dos <b>Requisitos</b> junto ao cliente através do Product Owner do nosso grupo. Assim tivemos uma melhor idéia do que consistiriam os <b>Requisitos Funcionais (RF)</b> e os <b>Requisitos Não Funcionais (RNF)</b> do produto, possibilitando a criação da nossa <B>Backlog do Produto</b>.
 Aqui se fez necessária a criação do <b>Repositório GitHub</b> para criar e manter um histórico das alterações feitas no projeto visando também a sua organização.  
 Usando o recurso das <b>Histórias dos Usuários</b> junto aos requisitos levantados, conseguimos explicitar melhor qual era a necessidade do cliente e o foco principal do nosso produto. Com as <b>Histórias dos Usuários</b> prontas, criamos o <b>Backlog da Sprint 01</b>.
 Para o <b>Esboço (Sketch)</b> da nossa aplicação, utilizamos o espaço de trabalho visual colaborativo <b>Whimsical</b>. Então geramos as <b>Tarefas</b> que cada um dos membros da equipe iriam executar. A partir da criação das Tarefas foi possível estimar o tempo de entrega de cada tarefa e assim a criação da nossa ferramenta visual do Scrum, o gráfico <b>Burndown</b>. Criado então o <b>Readme.MD</b> para apresentação do nosso projeto.
 Usando a linguagem de marcação <b>HTML5</b>, a ferramenta de estilização "Folha de Estilo em Cascatas" <b>CSS3</b> e JavaScript para ajudar na experiência da navegação. Assim criamos nosso <b>Protótipo Navegável</b>.</p>

<br>

# Sprint Backlog

> ## Sprint 01

<br>

<table>
    <tr>
        <td align="center">REQUISITO FUNCIONAL_ID</td>
        <td align="center">REQUISITOS DA SPRINT</td>
        <td align="center">TAREFA INICIADA</td>
        <td align="center">STATUS</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td> Criação do Esboço referência para a aplicação considerando a representação de suas funcionalidades totais</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td>Construção do corpo da aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td>Disponibilização de botões funcionais que direcionem o usuário para os locais corretos dentro do site</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td>Possibilitar preenchimento de texto em campos chaves, para melhorar a experiência do usuário no protótipo</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 2</td>
        <td>Trazer representação visual suficiente da identidade visual da Fatec SJC tomando como referência o site oficial (ex.: cores, logotipos)</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td> Dividir layout da página em seções e as seções com cores facilitando a compreensão pelo usuário</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td> Cores seguem relação com suas seções mantendo a Identidade Visual do sistema</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td> Evitar a adição de elementos desnecessários na interface da aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td> Acesso a informação com poucos "cliques"</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>RNF - 1</td>
        <td>Utilizar um sistema de Navegação Global onde o usuário sempre tenha acesso as funcionalidades da aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RNF - 1</td>
        <td>Layout limpo e simples que facilite o acesso as diversas funcionalidades da aplicação sem confusão</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RNF - 1</td>
        <td>Utlização de incones para facilitar o agrupamento de informações e facilitar a navegação na aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RNF - 2</td>
        <td>Orientação da exibição de objetos, textos, logotipo na aplicação bem definidos e agradáveis ao usuário</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RNF - 3</td>
        <td> Criar a funcionalidade de interação com os menus pelo usuário</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️

<br>

<span id="sprint2">

## Sprint 02 :running:

<br>

<p align="justify">Na <b>Segunda Sprint</b> começamos com o uso do microframework <b>Flask</b> usando a linguagem <b>Python 3</b> para criar a nossa aplicação. Foi escolhido a base de dados relacional <b>SQLite</b> para construímos um pequeno banco de dados que organize e estruture as relações lógicas das informações na nossa aplicação. Dentro do Flask utilizamos o mecânismo de template para Python, <b>Jinja2</b> para conseguimos fazer toda a conversação entre back e front-end na nossa aplicação.</p>

<br>


# Sprint Backlog

> ## Sprint 02

<br>

<table>
    <tr>
        <td align="center">REQUISITO FUNCIONAL_ID</td>
        <td align="center">REQUISITOS DA SPRINT</td>
        <td align="center">TAREFA INICIADA</td>
        <td align="center">STATUS</td>
    </tr>
    <tr>
        <td>RF - 4</td>
        <td> Criação da funcionalidade que permite que Usuários consigam criar e enviar novos informativos na aplicação de forma funcional</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>Data e Hora das postagens sempre visíveis</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>Filtro por data</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td> Funcionalidade de registro e armazenamento de novos usuários na aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td>Criação de Hierarquias que identifiquem os usuários dentro da aplicação. (ex.: professor, diretor, aluno e etc)</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td> Criar limitação para usuários Alunos evitando que possam enviar anúncios/informativos na aplicação e que apenas visualizem os anúncios de outros usuários</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td> Quando um anúncio/informativo for criado esse deverá ser único e que outros usuários consigam visualiza-lo e não diversas cópias distribuidas entre usuários</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td> Apenas o usuário que criou o informativo, terá a liberdade de excluí-lo</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td> Criar lógica que permita que o direcionamento dos informativos criados pelo novo Usuário seja feito de acordo com as hierarquias</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td> Criar interação funcional entre três ou mais Usuários, sendo um deles usuário Aluno</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>RNF - 4</td>
        <td>Construção da API para conversação entre front e back end</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RNF - 5</td>
        <td>Utilização de SQLite para banco de dados da aplicação considerando possibilidade de troca para PostGresSQL devido facilidade com o Heroku</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️

<br>

<span id="sprint3">

## Sprint 03 :running:

<br>

<p align="justify">Na <b>Terceira Sprint</b>, já possuindo uma aplicação minimamente funcional, focamos em adicionar <b>novas funcionalidades essênciais</b> a aplicação. Implementamos um método de <b>autenticação por e-mail</b>, <b>filtragem</b> dos informativos <b>por dia</b> organizados por ordem de mais recente ao menos recente, <b>filtro por palavra chave</b> também em ordem e a funcionalidade de <b>arquivar informativos</b>. Foram feitas melhorias em alguns aspectos visuais da aplicação, principalmente na exibição dos informativos arquivados, e também feita uma <b>revisão no modelo lógico do banco de dados</b> conseguindo relacionar todos os papéis na nossa aplicação de forma efetiva. Implementamos o uso da ferramenta <b>Flask-Migrate</b> para facilitar o versionamento do esquema do nosso banco de dados caso necessário junto a ferramenta <b>Flask-Alembic</b> para prover as configurações e o ambiente para migração das atualizações feitas no banco de dados sem riscos as informações contidas neste. A nossa aplicação agora permite a <b>inserção (editar), ocultamento (arquivar) e remoção dos informativos.</b></p> 

<br>


# Sprint Backlog

> ## Sprint 03

<br>

<table>
    <tr>
        <td align="center">REQUISITO FUNCIONAL_ID</td>
        <td align="center">REQUISITOS DA SPRINT</td>
        <td align="center">TAREFA INICIADA</td>
        <td align="center">STATUS</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td>Criação da funcionalidade de autenticação do cadastro do novo usuário por e-mail</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td>Informativos poderão ser excluídos apenas pelos usuários que os criarão</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 10</td>
        <td>Possibilidade de arquivar informativos em um campo separado e em ordem cronológica para que seja mantido um histórico de informativos</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td>Informativos são enviados a destinatários específicos e apenas os usuários com os papéis selecionados poderam visualiza-los</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>Filtragem dos informativos por papéis (ex.: Diretor, Professor, Aluno e etc)</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>Criação de um mecanismo de filtro por palavras-chave em um campo de busca de fácil acesso para pesquisas rápidas</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>Criação dos mecanismos de filtragem por data, com exibição em ordem de mais recente para menos recente</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 9</td>
        <td>Funcionamento da seção adm. com acesso restrito para que seja feita a administração de papéis e funções dentro da aplicação</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️

<br>

<span id="sprint4">

## Sprint 04 :running:

<br>

<p align="justify">Na <b>Quarta Sprint</b> tinhamos como necessidade a entrega da <b>aplicação completa</b>, por se tratar da <b>Sprint de fechamento do projeto</b> desenvolvido por nossa equipe durante esse semestre. O <b>foco principal</b> da nossa equipe foi no desenvolvimento de todas as demais <b>funcionalidades necessárias</b> para a aplicação, com base nos requisitos funcionais, assim como em <b>testes práticos</b> dos recursos que ela dispõe <b>para a solução do problema de perda de informação</b> do nosso cliente. Dentro das <b>funcionalidades necessárias</b>, a nossa aplicação agora dispõe da possibilidade de <b>anexar arquivos</b> ao criar novos informativos. Na <b>área de cadastro</b>, agora conseguimos fazer uma <b>seleção inicial</b> entre <strong>funcionários</strong> e <strong>alunos</strong> da instituição, considerando o número de <b>Matrícula</b> ou número <b>RA</b> após a validação do novo cadastro. Além dos papeis, agora temos as <b>opções de Cursos</b> na nossa aplicação, que podem ser adicionados de acordo com os cursos existentes e devem ser relacionados aos entes de interesse na instituição para que a <b>organização da comunicação</b> entre o corpo docente, discente e administrativo seja efetiva. Além dos filtros de busca por data, papel e palavra-chave agora também existe a possibilidade de <b>filtrar informativos que possuem ou não arquivos anexados</b>. Dentro da aplicação, os <b>informativos</b> agora possuem a <b>opção "Ler mais"</b> funcional que permite ao usuário expandir todo o conteúdo dos informativos para que sejam exibidas todas as informações escritas do informativo assim como os seus arquivos anexados. Parte importante da nossa <b>aplicação</b> é que o seu layout agora é <b>responsivo</b>. Devido ao <b>uso</b> de um <b>MOR/ORM (Mapeamento objeto-relacional)</b> para gerar o nosso <b>banco de dados</b>, fizemos o uso do SQLite durante todo o nosso projeto, <b>aumentando a produtividade</b> de forma significativa e também adicionando a <b>possibilidade de rápida migração da aplicação para outros bancos de dados</b>. Escolhemos o banco de dados <b>PostGresSQL</b> como opção de uso para nossa aplicação considerando as opções dentro dos requisitos não-funcionais da nossa aplicação.</p>

<br>

# Sprint Backlog

> ## Sprint 04

<br>

<table>
    <tr>
        <td align="center">REQUISITO FUNCIONAL_ID</td>
        <td align="center">REQUISITOS DA SPRINT</td>
        <td align="center">TAREFA INICIADA</td>
        <td align="center">STATUS</td>
    </tr>
    <tr>
        <td>RF - 9</td>
        <td>Página de moderação (admin) funcional</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td>Página de moderação (admin) com layout responsivo</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 11</td>
        <td> Adicionar funcionalidade de anexar arquivos aos informativos</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td> Adicionar a opção de cursos dentro da aplicação de forma funcional</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
    <tr>
        <td>RF - 10</td>
        <td>Fazer funcional a opção de "Ler mais" para os informativos</td>
        <td align="center">✔</td>
        <td align="center">✔</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo) ☝️