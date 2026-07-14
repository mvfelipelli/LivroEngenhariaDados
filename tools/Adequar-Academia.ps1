param(
    [string]$Vault = "C:\dev\dataeng-data\Livro\Engenharia de Dados",
    [switch]$Apply,
    [switch]$SkipBackup
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Host "[CRIAR PASTA] $Path" -ForegroundColor Green
        if ($Apply) {
            New-Item -ItemType Directory -Path $Path -Force | Out-Null
        }
    }
}

function Ensure-File {
    param(
        [string]$Path,
        [string]$Content = ""
    )
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Host "[CRIAR ARQUIVO] $Path" -ForegroundColor Green
        if ($Apply) {
            $parent = Split-Path -Parent $Path
            Ensure-Directory $parent
            Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
        }
    }
}

function Merge-Directory {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (-not (Test-Path -LiteralPath $Source)) { return }

    Ensure-Directory $Destination
    Write-Host "[MESCLAR] $Source -> $Destination" -ForegroundColor Yellow
    if (-not $Apply) { return }

    Get-ChildItem -LiteralPath $Source -Force | ForEach-Object {
        $target = Join-Path $Destination $_.Name

        if ($_.PSIsContainer) {
            Merge-Directory -Source $_.FullName -Destination $target
        }
        elseif (-not (Test-Path -LiteralPath $target)) {
            Move-Item -LiteralPath $_.FullName -Destination $target
        }
        else {
            $sourceHash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
            $targetHash = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash

            if ($sourceHash -eq $targetHash) {
                Remove-Item -LiteralPath $_.FullName -Force
            }
            else {
                $base = [IO.Path]::GetFileNameWithoutExtension($_.Name)
                $ext = [IO.Path]::GetExtension($_.Name)
                $conflict = Join-Path $Destination "$base-migrado$ext"
                $counter = 1
                while (Test-Path -LiteralPath $conflict) {
                    $conflict = Join-Path $Destination "$base-migrado-$counter$ext"
                    $counter++
                }
                Move-Item -LiteralPath $_.FullName -Destination $conflict
                Write-Host "  [CONFLITO PRESERVADO] $conflict" -ForegroundColor Magenta
            }
        }
    }

    if ((Get-ChildItem -LiteralPath $Source -Force | Measure-Object).Count -eq 0) {
        Remove-Item -LiteralPath $Source -Force
    }
}

function Rename-Or-MergeDirectory {
    param(
        [string]$OldPath,
        [string]$NewPath
    )

    if (-not (Test-Path -LiteralPath $OldPath)) { return }

    if (Test-Path -LiteralPath $NewPath) {
        Merge-Directory -Source $OldPath -Destination $NewPath
    }
    else {
        Write-Host "[RENOMEAR] $OldPath -> $NewPath" -ForegroundColor Yellow
        if ($Apply) {
            Move-Item -LiteralPath $OldPath -Destination $NewPath
        }
    }
}

function Update-MarkdownLinks {
    param(
        [string]$Root,
        [hashtable]$Replacements
    )

    Get-ChildItem -LiteralPath $Root -Recurse -File -Filter "*.md" | ForEach-Object {
        $content = Get-Content -LiteralPath $_.FullName -Raw -Encoding utf8
        if ($null -eq $content) { $content = "" }

        $updated = $content
        foreach ($old in $Replacements.Keys) {
            $updated = $updated.Replace([string]$old, [string]$Replacements[$old])
        }

        if ($updated -ne $content) {
            Write-Host "[ATUALIZAR LINKS] $($_.FullName)" -ForegroundColor DarkCyan
            if ($Apply) {
                Set-Content -LiteralPath $_.FullName -Value $updated -Encoding utf8
            }
        }
    }
}

if (-not (Test-Path -LiteralPath $Vault)) {
    throw "Vault não encontrado: $Vault"
}

if (-not $Apply) {
    Write-Host ""
    Write-Host "MODO DE SIMULAÇÃO: nenhuma alteração será feita." -ForegroundColor Yellow
}

if ($Apply -and -not $SkipBackup) {
    Write-Step "Criando backup"
    $backupRoot = Join-Path (Split-Path -Parent $Vault) "_backups"
    Ensure-Directory $backupRoot
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupFile = Join-Path $backupRoot "Engenharia-de-Dados-$timestamp.zip"
    Compress-Archive -Path (Join-Path $Vault "*") -DestinationPath $backupFile -CompressionLevel Optimal
    Write-Host "[BACKUP] $backupFile" -ForegroundColor Green
}

Write-Step "Criando estrutura"

$directories = @(
    "000-Atlas\Diagramas",
    "005-Wiki",
    "020-Laboratorios\Fundamentos",
    "020-Laboratorios\Linux",
    "020-Laboratorios\Git",
    "020-Laboratorios\SQL",
    "020-Laboratorios\Modelagem-de-Dados",
    "020-Laboratorios\Python",
    "020-Laboratorios\Apache-Spark",
    "020-Laboratorios\PostgreSQL",
    "020-Laboratorios\Lakehouse",
    "020-Laboratorios\Trino",
    "020-Laboratorios\Apache-Airflow",
    "020-Laboratorios\Qualidade-de-Dados",
    "020-Laboratorios\Observabilidade",
    "020-Laboratorios\Streaming",
    "020-Laboratorios\Cloud",
    "020-Laboratorios\DataOps-e-DevOps",
    "020-Laboratorios\Projeto-Integrador",
    "030-Projetos\DataRetail Platform\architecture",
    "030-Projetos\DataRetail Platform\decisions",
    "060-Assets\logos",
    "070-Anotacoes",
    "090-Arquivados",
    "tools\config",
    "tools\modules",
    "tools\templates",
    "tools\exports",
    "tools\logs"
)

foreach ($relative in $directories) {
    Ensure-Directory (Join-Path $Vault $relative)
}

Write-Step "Migrando estruturas antigas"

$migrations = @(
    @{ Old = "001-Labs"; New = "020-Laboratorios" },
    @{ Old = "002-Projetos"; New = "030-Projetos" },
    @{ Old = "003-Certificacoes"; New = "040-Certificacoes" },
    @{ Old = "999-Templates"; New = "050-Templates" },
    @{ Old = "070-Notas"; New = "070-Anotacoes" },
    @{ Old = "090-Archive"; New = "090-Arquivados" }
)

foreach ($m in $migrations) {
    Rename-Or-MergeDirectory `
        -OldPath (Join-Path $Vault $m.Old) `
        -NewPath (Join-Path $Vault $m.New)
}

Write-Step "Consolidando volumes duplicados"

$volumeRenames = @(
    @{ Old = "03-Git"; New = "03-Git-e-GitHub" },
    @{ Old = "07-PySpark"; New = "07-Apache-Spark" },
    @{ Old = "11-Airflow"; New = "11-Apache-Airflow" },
    @{ Old = "16-DevOps"; New = "16-DataOps-e-DevOps" },
    @{ Old = "17-Arquitetura"; New = "17-Arquiteturas-Avancadas" }
)

$volumesRoot = Join-Path $Vault "100-Volumes"
foreach ($m in $volumeRenames) {
    Rename-Or-MergeDirectory `
        -OldPath (Join-Path $volumesRoot $m.Old) `
        -NewPath (Join-Path $volumesRoot $m.New)
}

Write-Step "Criando arquivos institucionais"

$wikiFiles = @{
    "005-Wiki\Home.md" = "# Academia de Engenharia de Dados`r`n"
    "005-Wiki\Mapa Visual.md" = "# Mapa Visual`r`n"
    "005-Wiki\Perguntas Frequentes.md" = "# Perguntas Frequentes`r`n"
    "005-Wiki\Como Contribuir.md" = "# Como Contribuir`r`n"
    "005-Wiki\Como Pesquisar.md" = "# Como Pesquisar`r`n"
}

foreach ($entry in $wikiFiles.GetEnumerator()) {
    Ensure-File -Path (Join-Path $Vault $entry.Key) -Content $entry.Value
}

Write-Step "Criando arquivos auxiliares dos volumes"

Get-ChildItem -LiteralPath $volumesRoot -Directory |
    Where-Object { $_.Name -match '^\d{2}-' } |
    ForEach-Object {
        Ensure-File (Join-Path $_.FullName "README.md") "# $($_.Name)`r`n"
        Ensure-File (Join-Path $_.FullName "SUMMARY.md") "# Sumário — $($_.Name)`r`n"
        Ensure-File (Join-Path $_.FullName "CHANGELOG.md") "# Histórico de alterações — $($_.Name)`r`n"
    }

Write-Step "Atualizando caminhos antigos"

$replacements = @{
    "001-Labs/" = "020-Laboratorios/"
    "002-Projetos/" = "030-Projetos/"
    "003-Certificacoes/" = "040-Certificacoes/"
    "999-Templates/" = "050-Templates/"
    "070-Notas/" = "070-Anotacoes/"
    "090-Archive/" = "090-Arquivados/"
    "03-Git/" = "03-Git-e-GitHub/"
    "07-PySpark/" = "07-Apache-Spark/"
    "11-Airflow/" = "11-Apache-Airflow/"
    "16-DevOps/" = "16-DataOps-e-DevOps/"
    "17-Arquitetura/" = "17-Arquiteturas-Avancadas/"
}

Update-MarkdownLinks -Root $Vault -Replacements $replacements

Write-Host ""
if ($Apply) {
    Write-Host "ADEQUAÇÃO CONCLUÍDA COM SUCESSO." -ForegroundColor Green
}
else {
    Write-Host "SIMULAÇÃO CONCLUÍDA. Execute com -Apply para efetivar." -ForegroundColor Yellow
}
