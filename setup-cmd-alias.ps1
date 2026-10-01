$projectDirectory = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$pathEntries = @(
    $userPath -split ';' | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
)
$normalizedProjectDirectory = $projectDirectory.TrimEnd([char[]]@('\', '/'))
$alreadyOnPath = $false

foreach ($entry in $pathEntries) {
    $normalizedEntry = [Environment]::ExpandEnvironmentVariables($entry.Trim().Trim('"'))
    $normalizedEntry = $normalizedEntry.TrimEnd([char[]]@('\', '/'))
    if ($normalizedEntry -ieq $normalizedProjectDirectory) {
        $alreadyOnPath = $true
        break
    }
}

if (-not $alreadyOnPath) {
    $updatedUserPath = (@($pathEntries) + $projectDirectory) -join ';'
    [Environment]::SetEnvironmentVariable('Path', $updatedUserPath, 'User')
    Write-Host "Added '$projectDirectory' to your user PATH."
} else {
    Write-Host 'The Hangman project folder is already in your user PATH.'
}

Write-Host 'Open a new Command Prompt window and run: hangman'