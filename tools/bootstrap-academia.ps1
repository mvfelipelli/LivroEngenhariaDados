# =====================================================================
# Academia de Engenharia de Dados
# Bootstrap do Vault Obsidian
# =====================================================================

$Root = "C:\dev\dataeng-data\Livro\Engenharia de Dados"

# ---------------------------------------------------------------------
# Funções
# ---------------------------------------------------------------------

function New-Folder {
    param([string]$Path)

    if (!(Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "DIR  $Path" -ForegroundColor Green
    }
}

function New-Markdown {
    param(
        [string]$Path,
        [string]$Title = ""
    )

    if (!(Test-Path $Path)) {

        $content = ""

        if ($Title -ne "") {
            $content = @"
---
title: $Title
status: rascunho
---

# $Title

"@
        }

        Set-Content `
            -Path $Path `
            -Value $content `
            -Encoding utf8

        Write-Host "FILE $Path" -ForegroundColor Cyan
    }
}

# =====================================================================
# Estrutura principal
# =====================================================================

$Folders = @(
".obsidian",

"000-Atlas",
"000-Atlas\Glossario",

"999-Templates",

"00-Introducao",

"01-Fundamentos",

"02-Linux",

"03-Git",

"04-SQL",

"05-Modelagem-de-Dados",

"06-Python",

"07-PySpark",

"08-PostgreSQL",

"09-Lakehouse",

"10-Trino",

"11-Airflow",

"12-Qualidade-de-Dados",

"13-Observabilidade",

"14-Streaming",

"15-Cloud",

"16-DevOps",

"17-Arquitetura",

"18-Projeto-Integrador"
)

foreach ($folder in $Folders) {

    New-Folder (Join-Path $Root $folder)

}

# =====================================================================
# Atlas
# =====================================================================

$Atlas = @(
"MOC",
"Roadmap",
"Timeline",
"Arquiteturas",
"Tecnologias",
"Carreira"
)

foreach ($doc in $Atlas) {

    New-Markdown `
        (Join-Path $Root "000-Atlas\$doc.md") `
        $doc

}

# =====================================================================
# Templates
# =====================================================================

$Templates = @(
"Template-Capitulo",
"Template-Laboratorio",
"Template-Tecnologia",
"Template-Glossario",
"Template-Estudo-de-Caso"
)

foreach ($template in $Templates){

    New-Markdown `
        (Join-Path $Root "999-Templates\$template.md") `
        $template

}

# =====================================================================
# Volumes
# =====================================================================

$Volumes = @{

"00-Introducao" = @(
"00-Apresentacao",
"01-O-que-e-Engenharia-de-Dados",
"02-Ecossistema-de-Dados",
"03-Arquiteturas-Modernas",
"04-Projeto-Integrador",
"05-Ambiente-da-Academia",
"06-Como-Estudar",
"07-Roadmap",
"08-Preparacao-do-Ambiente",
"09-Encerramento"
)

}

foreach($volume in $Volumes.Keys){

    New-Markdown `
        (Join-Path $Root "$volume\README.md") `
        $volume

    foreach($chapter in $Volumes[$volume]){

        $chapterPath = Join-Path $Root "$volume\$chapter"

        New-Folder $chapterPath

        New-Folder "$chapterPath\imagens"

        New-Folder "$chapterPath\laboratorios"

        New-Folder "$chapterPath\exercicios"

        New-Folder "$chapterPath\referencias"

        New-Folder "$chapterPath\anexos"

        New-Markdown `
            "$chapterPath\README.md" `
            $chapter

    }

}

# =====================================================================
# Glossário Inicial
# =====================================================================

$Glossario = @(
"Engenharia de Dados",
"Engenheiro de Dados",
"Big Data",
"Data Warehouse",
"Data Lake",
"Lakehouse",
"Pipeline de Dados",
"Apache Spark",
"Apache Iceberg",
"Trino",
"Apache Airflow",
"ETL",
"ELT",
"MapReduce",
"ERP",
"CRM",
"Qualidade de Dados"
)

foreach($item in $Glossario){

    New-Markdown `
        (Join-Path $Root "000-Atlas\Glossario\$item.md") `
        $item

}

Write-Host ""
Write-Host "=============================================" -ForegroundColor Yellow
Write-Host " Academia criada com sucesso." -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Yellow