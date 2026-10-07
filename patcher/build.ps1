param(
    [Parameter(Mandatory = $true)][string]$AssetDirectory,
    [Parameter(Mandatory = $true)][string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'
$assetPath = (Resolve-Path -LiteralPath $AssetDirectory).Path
$outputPath = [System.IO.Path]::GetFullPath($OutputDirectory)
$sourcePath = Join-Path $PSScriptRoot 'patcher.py'
$names = @(
    'PCE-Langrisser-Kr-v0.707-patch.bps',
    'LANGRISSER_LIVE_FONT_DIAGNOSTIC_V378.cue'
)
foreach ($name in $names) {
    $filePath = Join-Path $assetPath $name
    if (-not (Test-Path -LiteralPath $filePath -PathType Leaf)) {
        throw "Missing patch asset: $filePath"
    }
}

$buildRoot = Join-Path $outputPath '_build'
$arguments = @(
    '-m', 'PyInstaller', '--noconfirm', '--clean', '--onefile', '--windowed',
    '--name', 'PCE-Langrisser-Kr-v0.707-Patcher',
    '--distpath', $outputPath,
    '--workpath', (Join-Path $buildRoot 'work'),
    '--specpath', (Join-Path $buildRoot 'spec')
)
foreach ($name in $names) {
    $arguments += @('--add-data', ((Join-Path $assetPath $name) + ';assets'))
}
$arguments += $sourcePath
& python @arguments
if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed: $LASTEXITCODE" }
