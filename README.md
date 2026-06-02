# DIR MAP WEB v0.3.6

**DIR MAP WEB** é um mapeador local de diretórios que roda no navegador, usando um pequeno servidor Python.  
Ele foi feito para analisar pastas grandes, visualizar a estrutura de diretórios e gerar estatísticas úteis sem enviar nada para a internet.

Nada é enviado para fora da sua máquina. O processamento acontece localmente.

---

## Visão geral

O app permite selecionar uma pasta do computador e gerar rapidamente:

- árvore visual do diretório;
- tamanho total real da pasta;
- tamanho realmente mapeado após filtros;
- quantidade de arquivos;
- quantidade de pastas;
- profundidade máxima;
- média de tamanho por arquivo;
- itens ignorados pelos filtros;
- pastas mais pesadas;
- extensões que mais ocupam espaço;
- exportação do mapa;
- exportação separada das estatísticas.

A ideia é simples: dar uma visão clara de “onde está o peso” dentro de uma pasta, sem depender de ferramentas pesadas, Electron, Node, React, internet ou serviços externos.

---

## Recursos principais

### Dashboard do diretório

O dashboard mostra as estatísticas principais da pasta analisada:

| Métrica | Descrição |
|---|---|
| Tamanho total real | Soma real do tamanho da pasta, incluindo itens ignorados no mapa |
| Tamanho mapeado | Soma apenas do que entrou no resultado filtrado |
| Arquivos | Total de arquivos encontrados |
| Pastas | Total de pastas encontradas |
| Profundidade | Maior nível de profundidade encontrado |
| Média por arquivo | Tamanho médio dos arquivos analisados |
| Ignorados | Itens pulados pelos filtros configurados |
| Sem permissão | Itens que não puderam ser lidos |

Os tamanhos são exibidos em formato legível, como `B`, `KB`, `MB`, `GB` e `TB`.

---

### Mapa do diretório

O app gera uma árvore do diretório selecionado no estilo:

```txt
my_projects/ [401.01 MB]
├── project_a/ [73.46 MB]
│   ├── dist/ [36.65 MB]
│   └── main.py [7.78 KB]
└── README.md [3.82 KB]
```

Isso facilita ver rapidamente o que existe dentro de uma pasta e quanto cada parte pesa.

---

### Filtros

Você pode configurar filtros antes de mapear.

#### Ocultar Pasta(s)

Ignora pastas específicas no resultado do mapa.

Exemplos comuns:

```txt
node_modules, .git, __pycache__, .venv, venv, dist, build
```

Esse filtro é útil para evitar que pastas gigantes e repetitivas poluam a árvore.

#### Ocultar Extensão(ões)

Permite ignorar arquivos por extensão.

Exemplo:

```txt
.log, .tmp, .cache
```

#### Ocultar Todos os Arquivos

Quando ativado, o mapa mostra principalmente a estrutura de pastas, sem listar cada arquivo individual.

#### Controlar Recursividade

Permite limitar a profundidade da varredura, útil em diretórios grandes demais.

#### Limite de itens

Define o número máximo de itens que o app deve renderizar no resultado.  
Isso ajuda a evitar travamentos quando a pasta possui dezenas de milhares de arquivos.

---

## Exportação

O app possui dois blocos de exportação separados.

### Exportar estatísticas

Exporta somente o dashboard e os dados estatísticos.

Formatos disponíveis:

- `.MD`
- `.JSON`
- `.TXT`
- copiar estatísticas para a área de transferência

Ideal para relatórios, auditorias rápidas ou documentação técnica.

### Exportar mapa/tree

Exporta somente o resultado da árvore de diretórios.

Formatos disponíveis:

- `.MD`
- `.JSON`
- `.TXT`
- copiar mapa para a área de transferência

Ideal para documentar a estrutura de um projeto ou pasta.

---

## Como rodar

### Requisitos

Você precisa ter o Python instalado no Windows.

Recomendado:

```txt
Python 3.10+
```

Para verificar se o Python está instalado:

```bat
python --version
```

ou:

```bat
py --version
```

---

### Rodando pelo `.bat`

Na pasta do projeto, dê duplo clique em:

```txt
start.bat
```

Depois abra no navegador:

```txt
http://localhost:8765
```

Em muitos casos o navegador abrirá automaticamente.

---

### Rodando pelo terminal

Também é possível rodar manualmente:

```bat
cd C:\caminho\para\DIR_MAP_WEB
python serve.py
```

Depois acesse:

```txt
http://localhost:8765
```

Para parar o servidor, volte ao terminal e pressione:

```txt
Ctrl + C
```

---

## Como usar

1. Abra o app no navegador.
2. Clique em **BROWSER**.
3. Selecione uma pasta.
4. Ajuste os filtros, se quiser.
5. Clique em **MAPEAR**.
6. Veja o dashboard e o resultado.
7. Exporte ou copie as estatísticas/mapa conforme necessário.

---

## Observações importantes sobre o navegador

Por segurança, navegadores modernos não permitem acesso livre ao disco inteiro.  
Por isso, o app só consegue analisar a pasta que você selecionar manualmente.

Além disso, o navegador pode exibir uma confirmação como:

```txt
Carregar milhares de arquivos para este site?
```

Isso é normal.  
Como o app roda localmente em `localhost`, os arquivos não são enviados para nenhum servidor externo.

---

## Privacidade

O DIR MAP WEB foi criado para funcionar localmente.

- Não envia arquivos para a internet.
- Não usa API externa.
- Não depende de login.
- Não coleta dados.
- Não faz upload da pasta selecionada.
- Não precisa de conexão depois de aberto localmente.

O navegador lê os metadados e o conteúdo estrutural da pasta apenas para montar o mapa e calcular estatísticas.

---

## Estrutura esperada do projeto

Uma estrutura típica da versão web standalone pode ser parecida com:

```txt
DIR_MAP_WEB/
├── index.html
├── serve.py
├── start.bat
└── README.md
```

Dependendo da distribuição, podem existir arquivos extras de build, ícones ou documentação.

---

## Empacotamento em `.exe`

Essa versão pode ser empacotada como executável usando PyInstaller.

### Instalar PyInstaller

```bat
pip install pyinstaller
```

### Gerar executável básico

```bat
pyinstaller --onefile --name DIR_MAP_WEB serve.py
```

Se o `serve.py` precisar incluir `index.html` dentro do executável, use um arquivo `.spec` ou `--add-data`.

Exemplo no Windows:

```bat
pyinstaller --onefile --name DIR_MAP_WEB --add-data "index.html;." serve.py
```

O executável será gerado em:

```txt
dist\DIR_MAP_WEB.exe
```

---

## Diferença entre versão web e desktop

| Versão | Como funciona | Melhor uso |
|---|---|---|
| Web | Roda no navegador via servidor local Python | Leve, simples, sem Electron |
| Desktop | App empacotado com interface própria | Uso como programa tradicional |

A versão web é mais leve e direta.  
A versão desktop é mais parecida com aplicativo instalado.

---

## Problemas comuns

### A página não abre

Verifique se o servidor está rodando:

```bat
python serve.py
```

Depois acesse manualmente:

```txt
http://localhost:8765
```

---

### O navegador não deixa selecionar a pasta

Use um navegador moderno, como:

- Microsoft Edge
- Google Chrome
- Brave

Alguns navegadores podem ter suporte limitado à seleção de diretórios.

---

### O app parece travar em pastas muito grandes

Reduza o **limite de itens** ou ative filtros como:

```txt
node_modules, .git, dist, build, .venv
```

Pastas com dezenas de milhares de arquivos podem pesar no navegador, principalmente se muitos itens forem renderizados na árvore.

---

### O tamanho total real é maior que o tamanho mapeado

Isso é esperado.

- **Tamanho total real** considera tudo dentro da pasta.
- **Tamanho mapeado** considera somente o que passou pelos filtros e apareceu no resultado.

Exemplo: se `node_modules` foi ignorado, ele ainda entra no tamanho real, mas não entra no tamanho mapeado.

---

## Recomendações de uso

Para projetos de programação, bons filtros iniciais são:

```txt
node_modules, .git, __pycache__, .venv, venv, dist, build, .next, .cache, target, .idea
```

Para análise mais completa, desative alguns filtros e aumente o limite de itens.

Para análise rápida, mantenha os filtros pesados ativados.

---

## Status

Versão atual:

```txt
v0.3.6
```

Tipo:

```txt
Web local standalone
```

Foco desta versão:

- estabilidade;
- dashboard responsivo;
- exportação separada de estatísticas;
- fluxo simples com botões `BROWSER` e `MAPEAR`;
- zero dependência de Node/npm/React/Electron.

---

## Licença

Defina aqui a licença do projeto, se desejar.

Exemplos comuns:

```txt
MIT
Apache-2.0
GPL-3.0
Proprietária
```

---

## Créditos

DIR MAP WEB foi criado para mapear diretórios locais com clareza, rapidez e privacidade.

Menos gambiarra, mais mapa.  
Menos chute, mais estatística.
