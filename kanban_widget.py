import grist

# Ce fichier Python sert de point d'entrée pour votre widget personnalisé dans Grist.
# Il indique à Grist de charger le fichier 'kanban_view.html' comme contenu du widget.

grist.widget.set_content(
    "kanban_view.html",
    headers={
        # Cette politique de sécurité du contenu (CSP) est importante pour permettre au widget
        # de charger des ressources externes comme Tailwind CSS et l'API Grist.
        # 'self': Autorise les ressources de la même origine.
        # 'unsafe-inline': Autorise les scripts et styles en ligne (nécessaire pour Tailwind et le JS de base).
        # 'unsafe-eval': Autorise eval() (parfois nécessaire pour les bibliothèques, bien que généralement à éviter).
        # data:: Autorise les URIs de données (par exemple, pour les images).
        # connect-src *: Autorise les connexions à n'importe quelle origine (pour la communication de l'API Grist).
        # img-src *: Autorise les images de n'importe quelle origine.
        "Content-Security-Policy": "default-src 'self' 'unsafe-inline' 'unsafe-eval' data:; connect-src *; img-src * data:;"
    }
)
