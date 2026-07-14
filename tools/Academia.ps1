param(
    [Parameter(Position = 0)]
    [ValidateSet("preview", "init", "help")]
    [string]$Command = "help"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$adequar = Join-Path $PSScriptRoot "Adequar-Academia.ps1"

if (-not (Test-Path -LiteralPath $adequar)) {
    throw "Script não encontrado: $adequar"
}

switch ($Command) {
    "preview" {
        Write-Host "Executando simulação..." -ForegroundColor Cyan
        & $adequar
    }
    "init" {
        Write-Host "Aplicando adequação..." -ForegroundColor Cyan
        & $adequar -Apply
    }
    "help" {
        Write-Host ""
        Write-Host "Academia de Engenharia de Dados" -ForegroundColor Cyan
        Write-Host "  .\Academia.ps1 preview"
        Write-Host "  .\Academia.ps1 init"
        Write-Host "  .\Academia.ps1 help"
        Write-Host ""
    }
}
