Clear-Host

git pull
git status
Start-Sleep -Seconds 2

# Fecha moderna ISO 8601
$fecha = Get-Date -Format "yyyy-MM-dd HH:mm"

# Evitar commit si no hay cambios
if (-not (git status --porcelain)) {
    Write-Host "No hay cambios para commitear."
    Pause
    exit
}

git add .
git commit -m "Auto $fecha"
git push
echo ""
Pause
Clear-Host

# ps c:\> powershell -ExecutionPolicy Bypass -File git-auto.ps1
# ps c:\> .\git-auto.ps1