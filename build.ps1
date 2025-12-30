# Build Script
$buildDir = "dist"

Write-Host "Starting build process..."

# Clean up old build
if (Test-Path $buildDir) {
    Remove-Item -Path $buildDir -Recurse -Force
}

# Create build directory
New-Item -ItemType Directory -Path $buildDir | Out-Null

# Copy artifacts
Copy-Item "app.py" -Destination $buildDir
Copy-Item "requirements.txt" -Destination $buildDir

Write-Host "Build complete. Artifacts ready in '$buildDir'."
