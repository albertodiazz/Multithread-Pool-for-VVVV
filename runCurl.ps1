Start-Sleep 5
(Invoke-WebRequest -Uri "http://10.90.125.20:5000/data" -Method Put -UseBasicParsing).Content
