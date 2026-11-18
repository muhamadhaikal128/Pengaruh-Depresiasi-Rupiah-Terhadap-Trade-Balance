param(
    [string]$ProjectRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$PythonExe = 'C:\Users\Administrator\AppData\Local\uv\cache\archive-v0\8S4zSmTV3TTty8yy\Scripts\python.exe',
    [string]$StataExe = 'C:\Program Files\StataNow19\StataMP-64.exe',
    [string]$PythonPackages = 'F:\temp\trade_macro_packages'
)
$ErrorActionPreference = 'Stop'
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
$analysisTemp = Join-Path $ProjectRoot 'intermediate\oskooee\temp'
New-Item -ItemType Directory -Path $analysisTemp -Force | Out-Null
$env:STATATMP = $analysisTemp
$env:TEMP = $analysisTemp
$env:TMP = $analysisTemp
$env:PYTHONIOENCODING = 'utf-8'
$env:MPLCONFIGDIR = Join-Path $analysisTemp 'mplcache'
if (Test-Path -LiteralPath $PythonPackages) { $env:PYTHONPATH = $PythonPackages }
& $PythonExe (Join-Path $PSScriptRoot '12_prepare_oskooee_models.py')
if ($LASTEXITCODE -ne 0) { throw 'Data preparation failed.' }
$stataRoot = $ProjectRoot.Replace([char]92,[char]47)
$stataEstimate = Join-Path $PSScriptRoot '13_run_oskooee_models.do'
$stataArguments = @('/e','do',('"' + $stataEstimate + '"'),('"' + $stataRoot + '"'))
$stataJob = Start-Process -FilePath $StataExe -ArgumentList $stataArguments -WorkingDirectory $analysisTemp -WindowStyle Hidden -PassThru
$stataJob.WaitForExit()
$estimateLog = Join-Path $ProjectRoot 'output\diagnostics\oskooee\estimation.log'
if (-not (Select-String -LiteralPath $estimateLog -Pattern '^OSKOOEE_ESTIMATION_COMPLETED$' -Quiet)) { throw 'Stata estimation did not complete. See estimation.log.' }
& $PythonExe (Join-Path $PSScriptRoot '14_report_oskooee_results.py')
if ($LASTEXITCODE -ne 0) { throw 'Result validation/reporting failed.' }
$stataGraphics = Join-Path $PSScriptRoot '15_export_oskooee_graphs.do'
$stataArguments = @('/e','do',('"' + $stataGraphics + '"'),('"' + $stataRoot + '"'))
$stataJob = Start-Process -FilePath $StataExe -ArgumentList $stataArguments -WorkingDirectory $analysisTemp -WindowStyle Hidden -PassThru
$stataJob.WaitForExit()
$graphLog = Join-Path $ProjectRoot 'output\diagnostics\oskooee\native_graphs.log'
if (-not (Select-String -LiteralPath $graphLog -Pattern '^OSKOOEE_NATIVE_GRAPHS_COMPLETED$' -Quiet)) { throw 'Native graph export did not complete.' }
& $PythonExe (Join-Path $PSScriptRoot '16_finalize_oskooee_report.py')
if ($LASTEXITCODE -ne 0) { throw 'Delivery validation failed.' }
Write-Output 'Analysis, diagnostics, table images and graphs completed. Read notes/hasil_ardl_nardl_oskooee.md.'
