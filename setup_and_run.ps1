# Verifica si pip está instalado
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "Pip no está instalado. Instalando pip..."
    Invoke-Expression "& { $(Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -UseBasicParsing).Content }"
}

# Instala las dependencias del proyecto
Write-Host "Instalando dependencias del proyecto..."
pip install -r requirements.txt

# Ejecuta el proyecto Python
Write-Host "Ejecutando el proyecto..."
python main.py
