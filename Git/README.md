# git init . / git remote add origin main
Aqui armazeno todos os comandos principais que utilizo no dia a dia para versionamento de código.

## 📚 Documentação Python 
- [Documentação Official Git](https://git-scm.com/docs/git)

## ▶️ Canais e Pyalists do Youtube Que Me Ajudaram
- [Teo Me Why](https://www.youtube.com/watch?v=84FhNXNWoig&list=PLvlkVRRKOYFQyKmdrassLNxkzSMM6tcSL)

## **COMANDOS GIT**

- git remote add origin (link do repositorio) → Você cria um repositorio local apartir de um link do github
- git clone (url) → Clona um repositorio
- git status → Mostra o status do diretorio
- git add . → Adiciona todos os arquivos pro commit
- git commit -m “nome do commit” -→ Adiciona um commit
- git commit --amend -m "renomeia mensagem" → atualiza a ultima mensagem de commit
- git push origin (nome da branch)  → manda as alterações da branch local pro remoto
- git pull origin (nome da branch) → puxa as alterações do repositorio remoto para o repositiorio local
- git log →ve todos os saves do git
- git diff (nome do arquivo) → mostra as alterações do arquivo anterior pro atual
- git reset (nome do arquivo) → volta o arquivo para que ele nao seja commitado
- HEAD → É o ultimo commit da branch
- git restore (nome do arquivo) → volta a versão anterior do arquivo
- git rm (nome do arquivo) → deleta arquivo

**ATUALIZA REPOSITORIO LOCAL PUXANDO INFO DO REMOTO:**

- git pull origin main
- git fetch --all → puxa todas as novas branchs
- git branch -a → agora vai puxar as branch que o comando acima trouxe do repositorio remoto
- git checkout (nome da branch) → altera de uma branch pra outra

**COMANDOS ENVOLVENDO AÇÕES NA BRANCH:**

- git checkout -b secundaria → cria uma nova branch
- git branch -D secundaria → Para deletar uma branch
- git checkout main → volta para a branch main
- git checkout (nome do arquivo) → deleta oque tem dentro para trazer do repositorio oque ta escrito no remoto
- git merge (nome da branch: secundaria) → junta as duas branch
- git checkout (nome da branch) → altera de uma branch pra outra

- git reset --soft
- git reset --hard → ele desfaz todas as alterações do arquivo

## EXTRA:

**COMANDOS DE TERMINAL**
- ls → lista todos os direitorios
- cd → entra na pasta
- pwd → mostra o caminho completo
- touch nome_do_arquivo.(extensão) → cria arquivo
- ls -a → mostra todos os arquivos ocultos
- mkdir → cria uma pasta
- rm → r “nome da pasta” → deleta a pasta
- ctrl + L → clear no console
- nano nome_do_arquivo.txt → abre o editor de texto onde você consegue digitar e salvar
- cat (nome do arquivo) →  mostra oque tem dentro do arquivo
- rm -rf .git/ → caso eu adicione a pasta git errada, esse comando deleta ela

