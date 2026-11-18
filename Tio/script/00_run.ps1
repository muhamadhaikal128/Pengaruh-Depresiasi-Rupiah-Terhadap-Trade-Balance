param(
 [string]$ProjectRoot=(Split-Path -Parent $PSScriptRoot),
 [string]$PythonExe='C:\Users\Administrator\AppData\Local\uv\cache\archive-v0\8S4zSmTV3TTty8yy\Scripts\python.exe',
 [string]$StataExe='C:\Program Files\StataNow19\StataMP-64.exe',
 [string]$PythonPackages='F:\temp\trade_macro_packages',
 [switch]$SkipBuild,
 [switch]$SkipEstimation
)
$ErrorActionPreference='Stop'
$ProjectRoot=(Resolve-Path -LiteralPath $ProjectRoot).Path
$runTemp=Join-Path $ProjectRoot 'intermediate\oskooee\temp'
New-Item -ItemType Directory -Path $runTemp -Force | Out-Null
$env:STATATMP=$runTemp; $env:TEMP=$runTemp; $env:TMP=$runTemp
$env:PYTHONPATH=$PythonPackages; $env:PYTHONIOENCODING='utf-8'
$env:MPLCONFIGDIR=Join-Path $runTemp 'mplcache'
if (-not $SkipBuild) {
 & $PythonExe (Join-Path $PSScriptRoot '01_build_panel.py')
 if ($LASTEXITCODE -ne 0) { throw 'HS6 preparation failed' }
}
if (-not $SkipEstimation) {
 $stataArgs=@('/e','do',('"'+(Join-Path $PSScriptRoot '00_master.do')+'"'),('"'+$ProjectRoot.Replace([char]92,[char]47)+'"'))
 $job=Start-Process -FilePath $StataExe -ArgumentList $stataArgs -WorkingDirectory $runTemp -WindowStyle Hidden -PassThru
 $job.WaitForExit()
}
$log=Join-Path $ProjectRoot 'output\diagnostics\oskooee\estimation.log'
if (-not (Select-String -LiteralPath $log -Pattern '^OSKOOEE_ESTIMATION_COMPLETED$' -Quiet)) { throw 'Stata estimation incomplete; see estimation.log' }
$stataArgs=@('/e','do',('"'+(Join-Path $PSScriptRoot '06_cusum_paths.do')+'"'),('"'+$ProjectRoot.Replace([char]92,[char]47)+'"'))
$job=Start-Process -FilePath $StataExe -ArgumentList $stataArgs -WorkingDirectory $runTemp -WindowStyle Hidden -PassThru
$job.WaitForExit()
$cusumLog=Join-Path $ProjectRoot 'output\diagnostics\oskooee\cusum_paths.log'
if (-not (Select-String -LiteralPath $cusumLog -Pattern '^STATA_CUSUM_PATHS_COMPLETED$' -Quiet)) { throw 'Official Stata CUSUM path export incomplete' }
& $PythonExe (Join-Path $PSScriptRoot '08_report_results.py')
if ($LASTEXITCODE -ne 0) { throw 'Model diagnostics or report validation failed' }
$stataArgs=@('/e','do',('"'+(Join-Path $PSScriptRoot '07_export.do')+'"'),'graphs',('"'+$ProjectRoot.Replace([char]92,[char]47)+'"'))
$job=Start-Process -FilePath $StataExe -ArgumentList $stataArgs -WorkingDirectory $runTemp -WindowStyle Hidden -PassThru
$job.WaitForExit()
$graphLog=Join-Path $ProjectRoot 'output\diagnostics\oskooee\native_graphs.log'
if (-not (Select-String -LiteralPath $graphLog -Pattern '^OSKOOEE_NATIVE_GRAPHS_COMPLETED$' -Quiet)) { throw 'Native graph export incomplete' }
& $PythonExe (Join-Path $PSScriptRoot '09_validate_results.py')
if ($LASTEXITCODE -ne 0) { throw 'Final delivery validation failed' }
Write-Output 'HS6 pipeline complete. Read notes/hasil_ardl_nardl_hs6.md.'
