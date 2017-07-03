# Filename: RenamingScript.ps1
# Author : Mahmoud Naser
Write-Host 'Script to Rename Files'
$prename= "Mahmoud"
$targetDirectory = $MyInvocation.MyCommand.Path
$targetExtension = "JPG"
# Getting File names in Directory

Write-Host "Targeting files with Extension $targetExtension"
Write-Host "Targeting files with under $targetDirectory"

$fileList = Get-ChildItem  -Path "*.$targetExtension" -Name # |  Where-Object {$_.Extension -eq ".JPG"} 
Foreach ($file in $fileList) {
	$newFileName = $prename + "_" + $file
	Write-Host "Renaming $file to $newFileName"
	rename-Item $file $newFileName
}

Write-Host "Rename Successfull"

# end of script