# 🔊 Robot Écho Intelligent - Spécification Maximum

Ce package implémente un interpréteur de commandes vocales/textuelles vers Twist et un système de monitoring avancé.

## 🏆 Points Forts
- **Parsing REGEX** : Extraction robuste des commandes 'avance', 'recule', 'tourne', 'stop'.
- **Double Service** : 
    - `/get_history` : Historique des 10 dernières commandes.
    - `/get_echo_stats` : Statistiques de performance (messages, latence).
- **Challenge Résolu** : Client d'action `SecureNavClient` asynchrone (non-bloquant).
- **Persistence** : Journalisation automatique dans `robot_commands.log`.

## 🚀 Utilisation
```bash
# Compiler
colcon build --packages-select miniproject_1_intelligent_echo
source install/setup.bash

# Lancer le parser
ros2 run miniproject_1_intelligent_echo cmd_parser.py

# Tester une commande
ros2 topic pub /cmd_text std_msgs/String "data: 'avance 1.5'"
```

---
**Maria Lagab** | Spécialité Robotique & Systèmes Intelligents
