# Système de Gestion Hospitalière - Architecture N-Tiers

## Architecture du projet

Le projet suit une architecture N-Tiers avec les couches suivantes :

1. **Couche Présentation** : API REST (Django REST Framework)
2. **Couche Métier** : Services et DTOs
3. **Couche Données** : Modèles et Repositories

### Diagramme UML

```plantuml

package "Présentation" {
  [API Views] --> [Serializers]
}

package "Métier" {
  [Services] --> [DTOs]
  [Services] --> [Exceptions]
}

package "Données" {
  [Repositories] --> [Models]
}

[API Views] --> [Services]
[Services] --> [Repositories]

## 📖 Guide d'Utilisation

### 🔐 Authentification
1. **Obtenir un token d'accès** :
   ```http
   POST /api-token-auth/
   Content-Type: application/json

   {
     "username": "votre_identifiant",
     "password": "votre_mot_de_passe"
   }
**Réponse réussie :**
   {"token":"votre_token_secure_12345"}
**a ajouter aux entetes**
   Authorization: Token votre_token_secure_12345

   #👨⚕️ Gestion des Patients
##Créer un patient

POST /api/patients/
Headers:
  Authorization: Token votre_token
  Content-Type: application/json

{
  "first_name": "Marie",
  "last_name": "Curie",
  "date_of_birth": "1867-11-07",
  "gender": "F",
  "address": "1 Rue Pierre Curie, Paris",
  "phone_number": "0123456789",
  "blood_type": "A+"
}

#Rechercher des patients

GET /api/patients/search/?q=Curie
Headers:
  Authorization: Token votre_token

  