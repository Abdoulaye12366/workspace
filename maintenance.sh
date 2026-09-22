#!/bin/bash
echo "=== LANCEMENT DE LA MAINTENANCE DE LA CONSOLE ==="

echo -e "\n[1/2] Nettoyage et mise a jour des paquets..."
pkg update -y && pkg upgrade -y

echo -e "\n[2/2] Verification de l'espace disque de l'appareil..."
df -h | grep "/data"

echo -e "\n✅ Maintenance terminee avec succes, Habi !"
#!/bin/bash
echo "=== Début de la maintenance Termux ==="
pkg clean
pkg autoremove -y
echo "=== Nettoyage terminé ==="
echo "Espace disque restant :"
df -h /data
