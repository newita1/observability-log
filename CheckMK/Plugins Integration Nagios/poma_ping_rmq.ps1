Write-Host "<<<Ips_ping>>>"
$ips = "ip1", "ip2", "ip3"
#Se realiza por cada host dado en la variable IP un ping de 1 paquete, si este paquete no es entregado, se marca como erroneo y se printea en el output del agente
#un error con el nombre previo del host que falla, en caso de funcionar, printeamos el nombre del host y el texto "Have ping". 
foreach ($ip in $ips) {
    try {
        Test-Connection -ComputerName $ip -Count 1 -ErrorAction Stop > $null
        Write-Host "$ip - Have ping"
    } catch {
        Write-Host "$ip - Error"
    }
}