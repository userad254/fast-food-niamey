# 🍽️ Fast Food Niamey - Commande de Repas via Stripe

Une application web de commande de repas moderne et sécurisée, permettant aux utilisateurs de découvrir des spécialités locales et de payer directement en ligne via l'interface sécurisée de Stripe.

## 🚀 Fonctionnalités
- 🍱 Catalogue de produits dynamique (spécialités algériennes et africaines).
- 🛒 Processus d'achat simplifié.
- 💳 Paiement sécurisé avec Stripe Checkout.
- 📱 Interface responsive et soignée.

## 📖 Utilisation
1. Accéder à `http://localhost:5000`
2. Sélectionner un plat parmi la sélection proposée.
3. Cliquer sur "Ajouter au panier" pour être redirigé vers Stripe.
4. Tester le paiement avec la carte Stripe test : `4242 4242 4242 4242`

## 🛠 Installation

```bash
# Cloner le dépôt
git clone <url-du-repo>
cd fast-food-niamey

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos propres clés Stripe
```

## 🧠 Compétences démontrées
- **Intégration d'API tierces** : Mise en place d'un tunnel de paiement complet et asynchrone avec Stripe.
- **Sécurité** : Gestion rigoureuse des clés API et des secrets via des variables d'environnement (.env).
- **Sessions Flask** : Gestion de la persistance et des états de redirection utilisateur.
- **Architecture Web** : Séparation claire entre la logique métier (`produits.py`), les routes (`app.py`) et les templates (`templates/`).
- **Typage Python** : Utilisation intensive des *Type Hints* pour garantir la robustesse et la maintenabilité du code.

## 📄 License
Ce projet est sous licence **MIT** - Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📧 Contact
**Adamou Soumana**
- 📧 adam00soumana@gmail.com
- 🔗 [LinkedIn](www.linkedin.com/in/adamou-soumana-a6537a346)
- 🌐 [Portfolio](https://adamou-portfolio.onrender.com/)
