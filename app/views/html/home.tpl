<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../static/css/home.css">
    <title>cjSolutions</title>
</head>

<body>
    
    <header>
        <div class="cabecalho">
            <div class="logo"><img id="img-logo" src="../../static/img/logocj.jpg" alt=""></div>
            <h2 id="h2-cab">Portal do Funcionário</h2>
            <button class="btn-logout">Logout</button>
        </div>
    </header>

    
    <nav class="menu">
        <h2 id="h2-menu">Ponto</h2>
        <button type="button"><i data-lucide="clock"></i> Registrar Ponto</button>
        <button type="button"><i data-lucide="list"></i> Meus Registros</button>
        <button type="button"><i data-lucide="bar-chart-2"></i> Relatórios</button>
    </nav>

    <main class="ponto">
    
        <div class="saudacao-container">
            <span id="saudacao"></span>
        </div>

        <section class="relogio">
            <h2>Relógio de Ponto</h2>
            <div class="contador" id="contador"></div>
            <p>Clique em um botão abaixo para registrar sua entrada ou saída:</p>
            <button type="button" id="entrada">Registrar Entrada</button>
            <button type="button" id="saida">Registrar Saída</button>
        </section>
    </main>

    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="../../static/js/home.js"></script>
</body>
</html>
