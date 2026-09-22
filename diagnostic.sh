#!/bin/bash
echo "=== DIAGNOSTIC SYSTEME DE HABI ==="
date
echo "-----------------------------------"
echo "[1] MEMOIRE VIVE (RAM) :"
free -m
echo "-----------------------------------"
echo "[2] ARCHITECTURE PROCESSEUR :"
uname -m
echo "-----------------------------------"
echo "✅ Diagnostic terminé avec succès !"
