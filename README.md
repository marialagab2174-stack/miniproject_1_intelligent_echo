# 🔊 Robot Écho Intelligent - Spécification Maximum

Ce projet implémente un interpréteur de langage naturel simplifié (NLP) pour la commande de robots mobiles sous **ROS 2 Jazzy**.

## 📋 Spécifications Techniques

### 1. Analyseur de Commandes (cmd_parser)
- **Parsing par Expressions Régulières (Regex)** : Garantit une extraction précise des valeurs numériques même avec des espaces superflus.
- **Conversion Géométrique** : Traduit les commandes texte directement en messages `geometry_msgs/Twist`.
- **Validation** : Filtrage automatique des commandes malformées pour éviter les comportements robotiques erratiques.

### 2. Services & Persistance
- **Service /get_history** : Retourne les 10 dernières commandes valides stockées en mémoire vive.
- **Logger Persistant** : Chaque commande est horodatée et enregistrée dans `robot_commands.log` pour analyse post-mission.

### 3. Commandes Supportées
| Commande | Action | Exemple |
|----------|--------|---------|
| `avance N` | Vitesse linéaire positive | `avance 0.5` |
| `recule N` | Vitesse linéaire négative | `recule 0.2` |
| `tourne_gauche A` | Vitesse angulaire positive | `tourne_gauche 1.0` |
| `tourne_droite A` | Vitesse angulaire négative | `tourne_droite 1.0` |
| `stop` | Arrêt complet du robot | `stop` |

## 🚀 Utilisation Avancée

### Compilation & Tests
```bash
cd ~/ros2_ws
colcon build --packages-select miniproject_1_intelligent_echo
colcon test --packages-select miniproject_1_intelligent_echo # Exécution des tests unitaires
source install/setup.bash
```

### Lancement avec Logger
```bash
ros2 launch miniproject_1_intelligent_echo echo_robot.launch.py
```

### Vérification du Service
```bash
ros2 service call /get_history miniproject_1_intelligent_echo/srv/GetHistory
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Laboratoire :** TP ROS 2 (Alger) | Dell Latitude 7400
