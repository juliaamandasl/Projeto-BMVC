// RELÓGIO//
const contador = document.getElementById("contador");

function atualizarRelogio() {
    const agora = new Date();
    contador.textContent = agora.toLocaleTimeString("pt-BR");
}

setInterval(atualizarRelogio, 1000);
atualizarRelogio();

// SAUDAÇÃO
const nomeUsuario = localStorage.getItem("usuario") || "Admin"; 

function gerarSaudacao(nome) {
    const hora = new Date().getHours();
    let saudacao;

    if (hora >= 5 && hora < 12) {
        saudacao = "Bom dia";
    } else if (hora >= 12 && hora < 18) {
        saudacao = "Boa tarde";
    } else {
        saudacao = "Boa noite";
    }

    return `${saudacao}, ${nome} `;
}

document.getElementById("saudacao").textContent = gerarSaudacao(nomeUsuario);


lucide.createIcons();

document.addEventListener("DOMContentLoaded", () => {
    const elementos = document.querySelectorAll(
        ".saudacao-container, .relogio, .menu button"
    );

    
    elementos.forEach(el => el.classList.add("fade-in-up"));

    
    elementos.forEach((el, i) => {
        setTimeout(() => {
            el.classList.add("visible");
        }, 200 * i);
    });
});

