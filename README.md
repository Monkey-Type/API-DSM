# API-DSM-Prototipo
<br id="topo">

<h1 align="center"> FATEC, SJC - 1º Semestre DSM</h1>

<h3>Equipe:</h3>
<h1>Monkey Type</h1>

<h3 align="center">🚧 Readme Em Construção 🚧</h3>


<p align="center" style="">
    <a href="#sobre">Sobre</a> | 
    <a href="#sprints">Sprints</a> | 
    <a href="#backlogs">Backlogs</a> | 
    <a href="#user-stories">User Stories</a> | 
    <a href="#prototipo">Protótipo Navegável</a> | 
    <a href="#tecnologias">Tecnologias</a> | 
    <a href="#equipe">Equipe</a> | 
    
</p>
   
<span id="sobre">

## :bookmark_tabs: Sobre o projeto

Tem por objetivo proporcionar um portal de informações para o Corpo Docente e Administrativo da <b>Fatec SJC</b> capaz de exibir e gerar de forma seletiva e controlada os avisos gerais ou específicos de cada usuário, respeitando as respectivas hierarquias dentro da universidade com o intuíto de melhorar a comunicação interna da instituição.
<br><br>

>### Status do Projeto: Em Andamento :warning:
<br><br>

<span id="sprints">

<table>
    <tr>
        <td>Sprint</td>
        <td>Tag</td>
        <td>Lançamento</td>
        <td>Status</td>
        <td>Histórico</td>
    </tr>
    <tr>
        <td>01</td>
        <td>Sprint#01</td>
        <td>dd/mm/aaaa</td>
        <td>Em Aberto</td>
        <td>inserir relatório</td>
    </tr>
</table>

> [Voltar ao Topo](#topo)
<br>


<span id="backlogs">

## :page_with_curl: Backlogs

> RF - Requisito Funcional

> RNF - Requisito Não Funcional
<br>
<table>
    <tr>
        <td>CÓDIGO</td>
        <td align="center">REQUISITOS</td>
    </tr>
    <tr>
        <td>RF - 1</td>
        <td> Envio de informações para divulgação via sistema (Administrador)</td>
    </tr>
    <tr>
        <td>RF - 2</td>
        <td> A Identidade Visual do sistema deve levar em consideração a identidade visual da Fatec de SJC</td>
    </tr>
    <tr>
        <td>RF - 3</td>
        <td> Cada Usuário deve ter um poder de enviar mensagens a determinados grupos de usuários e receber mensagens de determinado grupos de usuários numa hierarquia de USERS</td>
    </tr>
    <tr>
        <td>RF - 4</td>
        <td> O usuário deve ter a automia de marcar a mensagem como lida e não lida. Será importante manter um histórico de mensagem.</td>
    </tr>
    <tr>
        <td>RF - 5</td>
        <td> Quem recebe a mensagem não poderá excluí-la, porém poderá arquivá-la</td>
    </tr>
    <tr>
        <td>RF - 6</td>
        <td> Quem criou a mensagem é o único com poder de exclusão da mesma</td>
    </tr>
    <tr>
        <td>RF - 7</td>
        <td>  O Usuário dever ter a opção de receber ou não notificações por e-mail, cada vez que receber uma mensagem no sistema</td>
    </tr>
    <tr>
        <td>RF - 8</td>
        <td> Nas categoria de usuário onde há uma hierarquia, por exemplo, chefe da secretaria e assistente da secretaria, deve haver a opção de habilitar que pode mandar mensagem dentro desse grupod e usuário</td>
    </tr>
    <tr>
        <td>RF - 9</td>
        <td>  Filtro de mensagens: numa ferramenta de busca, por data, por categorias de remetente</td>
    </tr>
    <tr>
        <td>RF - 10</td>
        <td> Possibilidade de anexar documentos (e.g.: PDFs, Docs, etc)</td>
    </tr>
    <tr>
        <td>RF - 11</td>
        <td> Visualização de informações de divulgação via sistema de modo seletivo (filtro por data, interessados, curso, etc.)</td>
    </tr>
    <tr>
        <td>RF - 12</td>
        <td> Acesso às informações do sistema através de perfis de usuário/papeis (adm,usuário comum, coordenador de curso, etc.)</td>
    </tr>
    <tr>
        <td>RF - 13</td>
        <td> O Sistema deve ser responsivo</td>
    </tr>
    <tr>
        <td>RNF - 1</td>
        <td> Desenvolver o back end com a linguagem Python 3+ e o 
microframework Flask</td>
    </tr>
    <tr>
        <td>RNF - 2</td>
        <td> Utilizar o sistema gerenciador de banco de dados 
MariaDB/MySQL/PostGresSQL</td>
    </tr>
    <tr>
        <td>RNF - 3</td>
        <td> Utilizar HTML 5 para arquitetura da informação da aplicação</td>
    </tr>
    <tr>
        <td>RNF - 4</td>
        <td> Utilizar CSS 3 para especificação do layout e demais características de renderização da interface com o usuário</td>
    </tr>
    <tr>
        <td>RNF - 5</td>
        <td> Utilizar o GitHub para controle de versão dos artefatos de projeto</td>
    </tr>
    <tr>
        <td>RNF - 6</td>
        <td> Interface com navegação intuitiva (e.g. acesso à informação com poucos “cliques”)</td>
    </tr>
    <tr>
        <td>RNF - 7</td>
        <td> Sistema responsivo</td>
    </tr>
    <tr>
        <td>RNF - 8</td>
        <td> Utilizar JavaScript no front end (obs: pode fazer uso de frameworks)</td>
    </tr>
    <tr>
        <td>RNF - 9</td>
        <td> Deve  seguir a identidade visual da Fatec-SJC</td>
    </tr>
</table>

<br>

> [Voltar ao Topo](#topo)

<span id="user-stories">
<br><br>

## :page_with_curl: User Stories
> TEXTO
<br>
<table>
    <tr>
        <td>Requisito</td>
        <td>Remetente</td>
        <td>Instrução</td>
        <td>Finalidade</td>
    </tr>
    <tr>
        <td>#01</td>
        <td> "Administrador/Secretaria"</td>
        <td> Como usuário administrador, eu quero enviar as informações</td>
        <td>Para que qualquer pessoa que possuam uma conta fatec consiga visualizar essas informações</td>
    </tr>
    <tr>
        <td>#2</td>
        <td>"Administrador/Secretaria"</td>
        <td> Como usuário administrador, eu quero poder anexar arquivos e documentos</td>
        <td>Para que alunos, professores e a comunidade da fatec possa vizualizar e fazer download desses arquivos/documentos</td>
    </tr>
    <tr>
        <td>#3</td>
        <td> "Administrador/Secretaria"</td>
        <td> Como usuária administrador, eu quero poder filtrar as informações de modo seletivo (data, cursos, etc)</td>
        <td>Para gerenciar o que cada cargo envia na plataforma</td>
    </tr>
    <tr>
        <td>#4</td>
        <td>"Administrador/Secretaria"</td>
        <td> Como usuário administrador, eu quero que a plataforma possua cargos (adm, aluno, professor)</td>
        <td>Para que cada cargo apenas veja o que é de seu interesse/autoridade</td>
    </tr>
    <tr>
        <td>#5</td>
        <td>Professor</td>
        <td> Como professor, eu quero poder enviar anúncios</td>
        <td>Para que alunos, outros professores ou secretaria que uma conta fatec consigam visualizar essas informações</td>
    </tr>
</table>


<br>

> [Voltar ao Topo](#topo)

<span id="prototipo">

## :movie_camera: Protótipo Navegável
<br>

> Preview de Protótipo Navegável - Teste
<br><br>

![ezgif com-gif-maker](https://user-images.githubusercontent.com/58151594/132951486-b8fd293c-1afe-4b3f-a238-0f674d0a1b9c.gif)
<br>

> [Voltar ao Topo](#topo)

<span id="tecnologias">

## :computer: Tecnologias

> TEXTO

![TECNOLOGIAS](https://user-images.githubusercontent.com/58151594/132951991-1f14ca07-eb46-4001-848a-8fce66807639.png)

<br>

> Listando as Tecnologias com links

- HTML 5: 
- CSS3:
- Python 3.9*:
- VSCode: 
- etc
<br>

> [Voltar ao Topo](#topo)

<br>

## :monkey::computer: Equipe Monkey Type:
<br>
> Opção 1 - Tabela

<table>
    <tr>
        <td>FOTO PEQUENA</td>
        <td>NOME</td>
        <td>FUNCÃO</td>
        <td>LINKDIN</td>
        <td>GITHUB</td>
    </tr>
    <tr>
        <td>FOTO</td>
        <td>João</td>
        <td>P.O.</td>
        <td>LINK</td>
        <td>LINK</td>
    </tr>
    <tr>
        <td>FOTO</td>
        <td>José</td>
        <td>Scrum Master</td>
        <td>LINK</td>
        <td>LINK</td>
    </tr>
    <tr>
        <td>FOTO</td>
        <td>Matias</td>
        <td>DEV</td>
        <td>LINK</td>
        <td>LINK</td>
    </tr>
</table>
<br><br>
