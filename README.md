# 🔊 Intelligent Echo - ROS 2 Communication Pro

Ce projet est une implémentation avancée d'un système d'écho capable de traiter des flux de données textuelles avec une logique métier dynamique.

## 📋 Spécifications Techniques
- **Traitement Dynamique** : Transformation de chaînes de caractères via 3 modes (UPPERCASE, REVERSE, CYBER).
- **Service-Oriented Stats** : Fournit une analyse de performance (latence, volume) via le service `/get_echo_stats`.
- **Paramétrage à Chaud** : Possibilité de modifier le mode de traitement via `ros2 param set` sans interruption de service.

## 🛠 Interfaces
- **Topic Input** : `/input_topic` (std_msgs/String)
- **Topic Output** : `/output_topic` (std_msgs/String)
- **Service** : `/get_echo_stats` (Custom SRV)

## 🚀 Utilisation
```bash
# Build
colcon build --packages-select miniproject_1_intelligent_echo
source install/setup.bash

# Lancer le noeud
ros2 run miniproject_1_intelligent_echo intelligent_echo.py

# Changer le mode dynamiquement
ros2 param set /intelligent_echo echo_mode "REVERSE"

# Consulter les stats
ros2 service call /get_echo_stats miniproject_1_intelligent_echo/srv/GetEchoStats
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Machine :** Dell Latitude 7400
