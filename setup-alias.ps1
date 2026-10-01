$launcherPath = (Join-Path $PSScriptRoot 'hangman.bat').Replace("'", "''")
$profilePath = $PROFILE.CurrentUserCurrentHost
$marker = '# Hangman project alias'

if (-not (Test-Path -LiteralPath $profilePath)) {
    $profileDirectory = Split-Path -Parent $profilePath
    New-Item -ItemType Directory -Path $profileDirectory -Force | Out-Null
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
}

$profileContent = Get-Content -LiteralPath $profilePath -Raw
if ($profileContent -notmatch [regex]::Escape($marker)) {
    if (Get-Command hangman -ErrorAction SilentlyContinue) {
        throw "A command named 'hangman' already exists. Remove it before installing this alias."
    }

    $aliasDefinition = @"

$marker
function hangman {
    & '$launcherPath' @args
}
"@
    Add-Content -LiteralPath $profilePath -Value $aliasDefinition
}

. $profilePath
Write-Host "PowerShell command 'hangman' is ready."