# API-DSM-Prototipo
<br id="topo">

<h1 align="center"> FATEC, SJC - 1º Semestre DSM</h1>

> <p>Equipe:</p>
# :monkey::computer: Monkey Type 

<h2 align="center" >Sumário </h2>


 <p align="center"> |
    <a href="#sobre">Sobre</a> | 
    <a href="#sprints">Sprints</a> | 
    <a href="#backlog">Product Backlog</a> | 
    <a href="#user-stories">User Stories</a> | 
    <a href="#prototipo">Protótipo Navegável</a> | 
    <a href="#tecnologias">Tecnologias</a> | 
    <a href="#equipe">Equipe</a> |
    
</p>
   
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

<p align="justify">Em face de uma pandemia mundial instituições de ensino do mundo todo enfrentaram o grande desafio de adaptarem  as atividades acadêmicas para o ensino remoto em um curto espaço de tempo. Com isso o aumento do uso de ferramentas de correios eletrônicos para comunicação dentro das instituições cresceu de forma exponencial levando a diversos problemas de perda de informações. Com o intuito de resolver esse problema, a <strong>FATEC São José dos Campos</strong> propôs aos alunos do 1° semestre do curso de <strong>Desenvolvimento de Software Multiplataforma (DSM)</strong>, o desenvolvimento de um portal de informações para o Corpo Docente, Discente e Administrativo da Fatec SJC capaz de exibir e gerar de forma seletiva e controlada os avisos gerais ou específicos de cada usuário, respeitando as respectivas hierarquias dentro da universidade com o intuíto de melhorar a comunicação interna da instituição.</p>

>### Status do Projeto: Em Andamento :warning:
<br>


> [Voltar ao Topo](#topo) ☝️

<span id="sprints">
<br>

## :running: Sprints

| Sprint | Link | Início | Entrega | Status |
|--- |--- |--- |--- |:---:
| 01 | [Sprint 01](#sprint1) | 08/09/2021 | 19/09/2021 | ✔ |
| 02 | Sprint 02 | 20/09/2021 | 10/10/2021 | Em Aberto |
| 03 | Sprint 03 | 18/10/2021 | 07/11/2021 | Em Aberto |
| 04 | Sprint 04 | 08/11/2021 | 28/11/2021 | Em Aberto |

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
        <td>#01</td>
    </tr>
    <tr>
        <td>RF - 2</td>
        <td>#02</td>
        <td>  A Identidade Visual do sistema deve levar em consideração a identidade visual da Fatec SJC</td>
        <td>#01</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td>#03</td>
        <td>  Interface com navegação intuitiva</td>
        <td>#01</td>
    </tr>
    <tr>
        <td>RF - 4</td>
        <td>#05 #14 #15 #16</td>
        <td>  Envio de informações para divulgação via sistema (Administrador)</td>
        <td>#02</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td>#07 #11 #13</td>
        <td> Visualização de informações de divulgação via sistema de modo seletivo (filtro por data, interessados, curso, etc.)</td>
        <td>#02</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td>#08</td>
        <td>  Acesso às informações do sistema através de perfis de usuário/papeis (adm,usuário comum, coordenador de curso, etc.)</td>
        <td>#02</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td>#09 #17</td>
        <td>  Cada Usuário deve ter um poder de enviar informes/anúncios a determinados grupos de usuários e receber mensagens de determinado grupos de usuários numa hierarquia de USERS</td>
        <td>#03 #04</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td>#22</td>
        <td>   Nas categoria de usuário onde há uma hierarquia  (ex.: chefe da secretaria e assistente da secretaria), deverá haver a opção de habilitar quem pode mandar mensagem dentro desse grupo de usuário</td>
        <td>#03 #04</td>
    </tr>
    <tr>
        <td>RF - 9</td>
        <td>#18 #20</td>
        <td>  O usuário deve ter a automia de marcar a mensagem como lida e não lida. Será importante manter um histórico de mensagem.</td>
        <td>#02 #03 #04</td>
    </tr>
    <tr>
        <td>RF - 10</td>
        <td>#06 #10 #12</td>
        <td>  Possibilidade de anexar documentos (e.g.: PDFs, Docs, etc)</td>
        <td>#03 #04</td>
    </tr>
    <tr>
        <td>RF - 11</td>
        <td>#21</td>
        <td>  Quem recebe a mensagem não poderá excluí-la, porém poderá arquivá-la</td>
        <td>#03 #04</td>
    </tr>
    <tr>
        <td>RF - 12</td>
        <td>#21</td>
        <td>  Quem criou a mensagem é o único com poder de exclusão da mesma</td>
        <td>#03 #04</td>
    </tr>
    <tr>
        <td>RF - 13</td>
        <td>#22</td>
        <td>  O Usuário dever ter a opção de receber ou não notificações por e-mail, cada vez que receber uma mensagem no sistema</td>
        <td>#04</td>
    </tr>
    <tr>
        <td>RF - 14</td>
        <td>#11</td>
        <td>   Filtro de mensagens: numa ferramenta de busca, por data, por categorias de remetente</td>
        <td>#04</td>
    </tr>
    <tr>
        <td>RF - 15</td>
        <td>#19</td>
        <td>   Informes e mensagens que não sejam mais úteis devem ser arquivadas automaticamente</td>
        <td>#03 #04</td>
    </tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>RNF - 1</td>
        <td></td>
        <td>   Utilizar HTML5 para arquitetura da informação da aplicação</td>
        <td>#01</td>
    </tr>
    <tr>
        <td>RNF - 2</td>
        <td></td>
        <td>  Utilizar CSS 3 para especificação do layout e demais características de renderização da interface com o usuário</td>
        <td>#01</td>
    </tr>
    <tr>
        <td>RNF - 3</td>
        <td></td>
        <td> Utilizar JavaScript no front end (obs.: pode fazer uso de frameworks)</td>
        <td>#01</td>
    </tr>
    <tr>
        <td>RNF - 4</td>
        <td></td>
        <td> Desenvolver o back end com a linguagem Python 3+ e o 
microframework Flask</td>
        <td>#02</td>
    </tr>
    <tr>
        <td>RNF - 5</td>
        <td></td>
        <td> Utilizar o sistema gerenciador de banco de dados 
MariaDB/MySQL/PostGresSQL</td>
        <td>#02 #03</td>
    </tr>
    <tr>
        <td>RNF - 6</td>
        <td></td>
        <td>  Sistema responsivo</td>
        <td>#03 #04</td>
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
        <td align="center">#10</td>
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
        <td align="center">#07</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder enviar anúncios</td>
        <td>Para que alunos, outros professores ou secretaria que uma conta fatec consigam visualizar essas informações</td>
    </tr>
    <tr>
        <td align="center">US-10</td>
        <td align="center">#10</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder anexar arquivos, documentos, etc</td>
        <td>Para que alunos consigam acessar e fazer o download desses arquivos, documentos, etc</td>
    </tr>
    <tr>
        <td align="center">US-11</td>
        <td align="center">#05 #14</td>
        <td>Professor</td>
        <td>Como professor, eu quero poder filtrar as informações que recebo por data de modo seletivo (curso, interessados, etc)</td>
        <td>Para que não exista conflito de informações e para que eu consiga ver apenas o necessário</td>
    </tr>
    <tr>
        <td align="center">US-12</td>
        <td align="center">#10</td>
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
        <td>Para que os Professores do curso possam vê-los</td>
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
        <td align="center">#07</td>
        <td>Secretaria Acadêmica</td>
        <td> Como Usuário da Secretaria Acadêmica quero poder divulgar informes</td>
        <td>Para que qualquer usuário que seja Aluno ou Professor possa ve-los</td>
    </tr>
    <tr>
        <td align="center">US-18</td>
        <td align="center">#09</td>
        <td>Usuário Geral</td>
        <td> Como Usuário quero poder marcar as mensagens como lidas</td>
        <td>Para que  as mensagens lidas saiam da minha lista de mensagens</td>
    </tr>
    <tr>
        <td align="center">US-19</td>
        <td align="center">#15</td>
        <td>Administrador</td>
        <td> Como Administrador quero que as menssagens que não são mais úteis sejam arquivadas automaticamente</td>
        <td>Para que o Usuário Geral não tenha a sua caixa de mensagens poluída</td>
    </tr>
    <tr>
        <td align="center">US-20</td>
        <td align="center">#09</td>
        <td>Administrador</td>
        <td> Como Administrador quero que seja mantido um histórico de mensagens (arquivadas)</td>
        <td>Para que seja possível revê-las</td>
    </tr>
    <tr>
        <td align="center">US-21</td>
        <td align="center">#11 #12</td>
        <td>Usuário Geral</td>
        <td> Como Usuário que pode enviar anúncios e mensagens quero que apenas eu possa excluí-las.</td>
        <td>Para que eu possua um histórico acessível do que eu gerei</td>
    </tr>
    <tr>
        <td align="center">US-22</td>
        <td align="center">#08</td>
        <td>Secretaria</td>
        <td> Como Usuário que possuí hierarquia interna quero poder habilitar quais Usuários podem ou não enviar mensagens dentro do meu grupo</td>
        <td>Para que eu possa manter o controle dos Usuários dentro da hierarquia da minha categoria</td>
    </tr>
    <tr>
        <td align="center">US-23</td>
        <td align="center">#13</td>
        <td>Usuário Geral</td>
        <td> Como Usuário quero poder optar por receber mensagens e anúncios também por e-mail</td>
        <td>Para que eu possa manter o controle que já possuo ou manter minha preferência</td>
    </tr>
</table>


<br>

> [Voltar ao Topo](#topo) ☝️

<span id="prototipo">

## :movie_camera: Protótipo Navegável
<br>

- ### Registro de Conta > Mudança de Senha 

![LoginCadastroEsqueciSenha1](https://user-images.githubusercontent.com/58151594/133909179-9d5d40db-50fc-41d4-9226-c6506f8ff823.gif)
<br>

- ### Entrar (login) > Tela "Informativos" (tela principal)

![LoginTelaPrincipal2](https://user-images.githubusercontent.com/58151594/133909275-d41debd0-8f50-4e67-a517-58925f385567.gif)
<br>

- ### Tela "Informativos" > Filtros > Opções de Notificações

![TelePrincipalFiltros3](https://user-images.githubusercontent.com/58151594/133909325-b8b94228-18c3-404c-bb40-25f274a700b4.gif)
<br>

- ### Menu Lateral > Arquivos > Editar (Novo Informe)

![MenuLateralAquivadosEditarNovaMsgm4](https://user-images.githubusercontent.com/58151594/133909381-3281a543-8e0f-4d27-a953-756902c4a06a.gif)
<br>

- ### Configurações > Sair (logout)

![ConfiguracoesSair5](https://user-images.githubusercontent.com/58151594/133909598-1a021f01-e7bf-4026-8f41-91ec9565d27e.gif)
<br>

> [Voltar ao Topo](#topo) ☝️

<span id="tecnologias">

## :computer: Tecnologias

![Ferramentas_API](https://user-images.githubusercontent.com/58151594/133682494-9cefd846-e3cc-4e38-9f3f-87d58ceb31aa.jpg)


<br>

> Tecnologias links Úteis:
- [HTML5](https://pt.wikipedia.org/wiki/HTML5)
- [CSS3](https://pt.wikipedia.org/wiki/CSS3)
- [JavaScript](https://pt.wikipedia.org/wiki/JavaScript)
- [Adobe XD](https://www.adobe.com/br/products/xd.html)
- [GitHub](https://github.com)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- [Whimsical](https://whimsical.com/)

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
        <td>Contato</td>
    </tr>
    <tr>
        <td>Rafael da Silva Peres</td>
        <td>Product Owner</td>
        <td><a href="https://github.com/Rafaeldasilvaperes">GitHub</td>
    </tr>
    <tr>
        <td>Gabriel Souza Bicho Nunes</td>
        <td>Scrum Master</td>
        <td><a href="https://github.com/ZeroPirata">GitHub</td>
    </tr>
    <tr>
        <td>Gustavo Pereira</td>
        <td>DEV</td>
        <td><a href="https://github.com/Foot-G">GitHub</td>
    </tr>
    <tr>
        <td>Leonardo Queiróz Machado</td>
        <td>DEV</td>
        <td><a href="https://github.com/Lrd-M">GitHub</td>
    </tr>
    <tr>
        <td>Lucas Ferreira da Costa</td>
        <td>DEV</td>
        <td><a href="https://github.com/orgs/Monkey-Type/people/ddaiwon">GitHub</td>
    </tr>
    <tr>
        <td>Rafael Leonardo Lopes</td>
        <td>DEV</td>
        <td><a href="https://github.com/Rafael-leonardo">GitHub</td>
    </tr>
    <tr>
        <td>Vinícius Andrade B.</td>
        <td>DEV</td>
        <td><a href="https://github.com/orgs/Monkey-Type/people/ViniciusAndBar">GitHub</td>
    </tr>
</table>
<br>

#### :pray: Agradecimentos especiais ao [Wellington Felipe](https://github.com/orgs/Monkey-Type/people/WellFelipe411) (ex P.O.) por ajudar a equipe no início do projeto.

<br>

> [Voltar ao Topo](#topo) ☝️

<br>

<span id="sprint1">

## Sprint 01 :running:
<br>

<p align="justify">Na primeira <b>Sprint</b> fizemos o levantamento dos <b>Requisitos</b> junto ao cliente através do Product Owner do nosso grupo. Assim tivemos uma melhor idéia do que consistiriam os <b>Requisitos Funcionais (RF)</b> e os <b>Requisitos Não Funcionais (RNF)</b> do produto, possibilitando a criação da nossa <B>Backlog do Produto</b>.
 Aqui se fez necessária a criação do <b>Repositório GitHub</b> para criar e manter um histórico das alterações feitas no projeto visando também a sua organização.  
 Usando o recurso das <b>Histórias dos Usuários</b> junto aos requisitos levantados, conseguimos explicitar melhor qual era a necessidade do cliente e o foco principal do nosso produto. Com as <b>Histórias dos Usuários</b> prontas, criamos o <b>Backlog da Sprint 01</b>.
 Para o <b>Esboço (Sketch)</b> da nossa aplicação, utilizamos o espaço de trabalho visual colaborativo <b>Whimsical</b>. Então geramos as <b>Tarefas</b> que cada um dos membros da equipe iriam executar. A partir da criação das Tarefas foi possível estimar o tempo de entrega de cada tarefa e assim a criação da nossa ferramenta visual do Scrum, o gráfico <b>Burndown</b>. Criado então o <b>Readme.MD</b> para apresentação do nosso projeto.
 Usando a linguagem de marcação <b>HTML5</b> e a ferramenta de estilização "Folha de Estilo em Cascatas" <b>CSS3</b> criamos nosso <b>Protótipo Navegável</b>.</p>

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