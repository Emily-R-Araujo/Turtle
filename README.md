# Turtle Game

Este é um jogo simples em Python feito com Pygame, onde você controla uma tartaruga que precisa comer maçãs para ganhar pontos. Inspirei-me no clássico Snake, com a tartaruga ficando mais rápida à medida que sua pontuação cresce.

## Como Jogar

1.  **Requisitos:** Certifique-se de ter o Python e o Pygame instalados no seu sistema. Você pode instalar o Pygame usando o pip:
    ```bash
    pip install pygame
    ```

    Note que o pip deve estar na versão mais recente para poder instalar o pygame. Caso seu pip esteja desatualizado, é possível atualizá-lo com o seguinte comando:
    ```bash
    pip install --upgrade pip
    ```

2.  **Baixe os Arquivos:** Baixe o arquivo `main.py` e a pasta `src` contendo as imagens (`background.jpeg`, `Graphics/turtle-*.png`, `Graphics/apple.png`) e os sons (`SFX/background-music.wav`, `SFX/snake-eating.wav`, `SFX/game-over.wav`) para o mesmo diretório.

3.  **Execute o Jogo:** Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou os arquivos e execute o seguinte comando:
    ```bash
    python main.py
    ```

4.  **Controles:**
    * **Teclas de Seta (Cima, Baixo, Esquerda, Direita):** Movem a tartaruga na direção correspondente. A imagem da tartaruga mudará de acordo com a direção.
    * **ESC:** Pressione a tecla `ESC` durante a tela de "GAME OVER" para reiniciar o jogo.

5.  **Objetivo:** Controle a tartaruga para comer as maçãs que aparecem aleatoriamente na tela. Cada maçã comida aumenta sua pontuação em 10 pontos.

6.  **Fim de Jogo:** O jogo termina se a tartaruga sair dos limites da área de jogo (as bordas visíveis com a grama). Quando o jogo termina, a tela exibirá "GAME OVER" e sua pontuação final.

7.  **Menu Inicial:** Ao iniciar o jogo, uma tela de menu será exibida. Pressione qualquer tecla de seta para começar a jogar.

## Funcionalidades

* **Controle da Tartaruga:** O jogador controla a tartaruga usando as teclas de seta.
* **Coleta de Maçãs:** Ao colidir com uma maçã, a pontuação do jogador aumenta e uma nova maçã aparece em um local aleatório.
* **Pontuação:** A pontuação é exibida no canto superior esquerdo da tela.
* **Velocidade Progressiva:** A velocidade da tartaruga aumenta ligeiramente a cada maçã comida.
* **Música de Fundo:** Uma música de fundo é reproduzida continuamente durante o jogo.
* **Efeitos Sonoros:** Efeitos sonoros são reproduzidos ao comer uma maçã e quando o jogo termina.
* **Tela de Game Over:** Quando a tartaruga sai da tela, o jogo termina e uma tela de "GAME OVER" é exibida com a pontuação final e a opção de reiniciar.
* **Menu Inicial:** Uma tela de boas-vindas é mostrada no início do jogo.

## Créditos

* Este jogo foi desenvolvido usando a biblioteca Pygame (https://www.pygame.org/).

## Notas

* Certifique-se de que todos os arquivos na pasta `src` estejam presentes no mesmo diretório que o script `main.py` para que o jogo funcione corretamente.
* A dificuldade do jogo aumenta gradualmente à medida que a tartaruga se torna mais rápida com o aumento da pontuação.
