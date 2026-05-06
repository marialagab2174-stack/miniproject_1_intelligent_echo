# 🔊 Robot Écho Intelligent - Interpréteur de Commandes

Ce robot écoute des commandes textuelles et les traduit instantanément en vecteurs de mouvement pour une base mobile.

## 📋 Spécifications Techniques
- **Parser de Commandes** : Traduit 'avance N' en `geometry_msgs/Twist`.
- **Historique de Session** : Service `/get_history` retournant les 10 dernières actions.
- **Multi-Node Launch** : Démarrage coordonné du parser et du logger.

## 🚀 Commandes Supportées
- `avance [vitesse]`
- `recule [vitesse]`
- `tourne_gauche [angle]`
- `tourne_droite [angle]`
- `stop`

## 🛠 Utilisation
```bash
ros2 launch miniproject_1_intelligent_echo echo_robot.launch.py
ros2 topic pub /cmd_text std_msgs/String "data: 'avance 0.5'"
ros2 service call /get_history miniproject_1_intelligent_echo/srv/GetHistory
```

---
**Maria Lagab** - *Spécialité Robotique*
