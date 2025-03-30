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

