# Deploy Script
$sourceDir = "dist"
$deployDir = "deployment"

Write-Host "Starting deployment..."

# Check if build artifact exists
if (-not (Test-Path $sourceDir)) {
    Write-Error "Build artifacts not found in '$sourceDir'. Run build.ps1 first."
    exit 1
}

# Clean up old deployment
if (Test-Path $deployDir) {
    Remove-Item -Path $deployDir -Recurse -Force
}

# Create deployment directory
New-Item -ItemType Directory -Path $deployDir | Out-Null

# Deploy files
Copy-Item "$sourceDir\*" -Destination $deployDir -Recurse

Write-Host "Application deployed to '$deployDir'."
Write-Host "Simulating restart..."
Write-Host "Deployment successful!"
