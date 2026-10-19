param(
    [Parameter(Mandatory=$true)][string]$DocumentPath,
    [Parameter(Mandatory=$true)][string]$PdfPath
)
$ErrorActionPreference = 'Stop'
$taskWord = $null
$taskDocument = $null
try {
    $taskWord = New-Object -ComObject Word.Application
    $taskWord.Visible = $false
    $taskWord.DisplayAlerts = 0
    $taskWord.AutomationSecurity = 3
    $taskDocument = $taskWord.Documents.Open($DocumentPath, $false, $true)
    $taskDocument.Repaginate()
    $taskDocument.Fields.Update() | Out-Null
    $taskDocument.ExportAsFixedFormat($PdfPath, 17)
    $taskPages = $taskDocument.ComputeStatistics(2)
    Write-Output "Word exported $taskPages pages to $PdfPath"
} finally {
    if ($null -ne $taskDocument) {
        $taskDocument.Close(0)
        [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($taskDocument) | Out-Null
    }
    if ($null -ne $taskWord) {
        $taskWord.Quit(0)
        [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($taskWord) | Out-Null
    }
}
