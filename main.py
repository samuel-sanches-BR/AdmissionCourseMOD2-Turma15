from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()
    game.execute()

#Quando o player morrer: (no "else" do "show_menu()" linha 108 do game.py)
#	- mostrar uma mensagem de restart (por exemplo "Press any key to restart")
#	- mostrar pontuação atingida
#	- mostrar o contador de mortes

#> Resetar a contagem de pontuação e a velocidade, cada vez que o jogo é "restartado"


#> Remover a repetição de código pra formatação de texto em "draw_score()" e "show_menu()"
