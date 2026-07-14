# =====================================================================
# Academia de Engenharia de Dados
# Inicializa a estrutura completa do Vault Obsidian
#
# Autor: Marcello Felipelli / ChatGPT
# =====================================================================

$Root = "C:\dev\dataeng-data\Livro\Engenharia de Dados"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Inicializando estrutura da Academia"
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

#-----------------------------------------------------------------------
# Função
#-----------------------------------------------------------------------

function New-Folder {

    param([string]$Path)

    if (!(Test-Path $Path)) {

        New-Item -ItemType Directory -Force -Path $Path | Out-Null

        Write-Host "[CRIADO] Pasta: $Path" -ForegroundColor Green

    }
}

function New-File {

    param([string]$Path)

    if (!(Test-Path $Path)) {

        New-Item -ItemType File -Force -Path $Path | Out-Null

        Write-Host "[CRIADO] Arquivo: $Path" -ForegroundColor Yellow

    }
}

#-----------------------------------------------------------------------
# Pastas principais
#-----------------------------------------------------------------------

$Folders = @(

"000-Atlas",

"001-Dashboard",

"010-Biblioteca",

"020-Laboratorios",

"030-Projetos",

"040-Certificacoes",

"050-Templates",

"060-Assets",

"060-Assets\diagramas",

"060-Assets\datasets",

"060-Assets\icones",

"060-Assets\imagens",

"060-Assets\svg",

"070-Notas",

"080-Inbox",

"090-Archive",

"100-Volumes",

"999-Arquivos-Temporarios"

)

foreach($Folder in $Folders){

    New-Folder "$Root\$Folder"

}

#-----------------------------------------------------------------------
# Atlas
#-----------------------------------------------------------------------

$AtlasFolders = @(

"Glossario",

"Tecnologias",

"Arquiteturas",

"Pessoas",

"Empresas",

"Casos"

)

foreach($Folder in $AtlasFolders){

    New-Folder "$Root\000-Atlas\$Folder"

}

#-----------------------------------------------------------------------
# Biblioteca
#-----------------------------------------------------------------------

$Biblioteca = @(

"Livros",

"Papers",

"RFCs",

"Documentacao Oficial",

"Cheat Sheets",

"Casos Reais",

"Empresas",

"Videos"

)

foreach($Folder in $Biblioteca){

    New-Folder "$Root\010-Biblioteca\$Folder"

}

#-----------------------------------------------------------------------
# Volumes
#-----------------------------------------------------------------------

$Volumes = @(

"00-Introducao",

"01-Fundamentos",

"02-Linux",

"03-Git-e-GitHub",

"04-SQL",

"05-Modelagem-de-Dados",

"06-Python",

"07-Apache-Spark",

"08-PostgreSQL",

"09-Lakehouse",

"10-Trino",

"11-Apache-Airflow",

"12-Qualidade-de-Dados",

"13-Observabilidade",

"14-Streaming",

"15-Cloud",

"16-DataOps-e-DevOps",

"17-Arquiteturas-Avancadas",

"18-Projeto-Integrador"

)

foreach($Volume in $Volumes){

    New-Folder "$Root\100-Volumes\$Volume"

    New-File "$Root\100-Volumes\$Volume\README.md"

}

#-----------------------------------------------------------------------
# Projeto Oficial
#-----------------------------------------------------------------------

New-Folder "$Root\030-Projetos\DataRetail Platform"

$Projeto = @(

"docs",

"datasets",

"docker",

"infra",

"pipelines",

"sql",

"spark",

"python",

"airflow",

"tests",

"monitoring",

"notebooks",

"scripts"

)

foreach($Pasta in $Projeto){

    New-Folder "$Root\030-Projetos\DataRetail Platform\$Pasta"

}

New-File "$Root\030-Projetos\DataRetail Platform\README.md"

#-----------------------------------------------------------------------
# Dashboard
#-----------------------------------------------------------------------

New-File "$Root\001-Dashboard\README.md"

#-----------------------------------------------------------------------
# Biblioteca
#-----------------------------------------------------------------------

New-File "$Root\010-Biblioteca\README.md"

#-----------------------------------------------------------------------
# Atlas
#-----------------------------------------------------------------------

$Atlas = @(

"MOC.md",

"Guia Editorial.md",

"Roadmap.md",

"Timeline.md",

"Arquiteturas.md",

"Tecnologias.md",

"Carreira.md",

"Como Usar a Academia.md"

)

foreach($Arquivo in $Atlas){

    New-File "$Root\000-Atlas\$Arquivo"

}

#-----------------------------------------------------------------------
# Templates
#-----------------------------------------------------------------------

$Templates = @(

"Template-Capitulo.md",

"Template-Laboratorio.md",

"Template-Tecnologia.md",

"Template-Glossario.md",

"Template-Projeto.md",

"Template-Estudo-de-Caso.md"

)

foreach($Arquivo in $Templates){

    New-File "$Root\050-Templates\$Arquivo"

}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Estrutura criada com sucesso!"
Write-Host "==========================================" -ForegroundColor Cyan