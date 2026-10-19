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
    $taskDocument = $taskWord.Documents.Open($DocumentPath, $false, $false)
    $taskDocument.Fields.Update() | Out-Null
    foreach ($taskToc in $taskDocument.TablesOfContents) {
        $taskToc.Update()
        $taskToc.Range.Font.Name = 'Times New Roman'
        $taskToc.Range.Font.Size = 10.5
        $taskToc.Range.Font.Color = 0
        $taskToc.Range.ParagraphFormat.SpaceBefore = 0
        $taskToc.Range.ParagraphFormat.SpaceAfter = 0
        $taskToc.Range.ParagraphFormat.LineSpacingRule = 4
        $taskToc.Range.ParagraphFormat.LineSpacing = 12
    }
    $taskDocument.Repaginate()
    foreach ($taskToc in $taskDocument.TablesOfContents) {
        $taskToc.UpdatePageNumbers()
    }
    $taskDocument.Save()
    $taskDocument.ExportAsFixedFormat($PdfPath, 17)
    $taskPages = $taskDocument.ComputeStatistics(2)
    Write-Output "Word exported $taskPages pages with updated TOC."
} finally {
    if ($null -ne $taskDocument) {
        $taskDocument.Close()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($taskDocument)
    }
    if ($null -ne $taskWord) {
        $taskWord.Quit()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($taskWord)
    }
}
