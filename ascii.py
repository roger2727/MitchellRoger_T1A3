from rich.console import Console
console=Console()
def starwars():
    console.rule("")
    console.rule("")
    console.print(r""" [yellow]              _________________      ____         __________
 .       .    /                 |    /    \    .  |          \
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/             .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \
   .      \            /  /   /__\   \    |         _/.   \    \
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/ ADVENTURE By M ROGER[/] """, style= "yellow")
    console.rule("")
    console.rule("")
def yoda():
    
    console.print(r""" [green]
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
        [/]  """, style= "green")  
def vadar():
    console.print(r"""[red]
          _________
          III| |III
        IIIII| |IIIII
       IIIIII| |IIIIII
       IIIIII| |IIIIII
      IIIIIII| |IIIIIII
      IIIIIII\ /IIIIIII
     II (___)| |(___) II
    II  \    /D\    /  II
   II  \ \  /| |\  / /  II
  II    \_\/|| ||\/_/    II
 II     / O-------O \     II
II_____/   \|||||/   \_____II 

[/]""", style ="red")    