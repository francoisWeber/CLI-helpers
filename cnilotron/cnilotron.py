import click
from datetime import datetime

ME = "François Weber"

GENERIC_DEMAND = """Par ailleurs, je profite de ce mail pour vous demander :
- de supprimer toutes mes informations de contact de vos bases de données
- de me communiquer la liste des tiers à qui vous auriez pu communiquer mes coordonnées
- exiger de ces tiers qu'ils suppriment également mes coordonnées de leurs bases de données
- de me tenir au courant de toutes ces procédures
Je vous rappelle que vous bénéficiez d'un délai d'1 mois pour effectuer ces actions (https://www.cnil.fr/fr/le-droit-leffacement-supprimer-vos-donnees-en-ligne)."""


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand not in ["menace", "plainte"]:
        print("Option non reconnue 🤷")


@cli.command()
@click.argument("previous_claims", required=True, default=None, type=str, nargs=-1)
def avertissement(previous_claims):
    message = f"""Bonjour,
 
Je n'ai *jamais* demandé à recevoir votre newsletter ; j'ai même déjà demandé à ne *plus* la recevoir {len(previous_claims) - 1} fois (les {n_clics}). Cet action qui vous oblige légalement à me sortir de vos mailings. 
Vous n'avez manifestement pris aucune action pour vous mettre en confirmité avec mes souhaits et avec le RGPD (puisque je reçois toujours vos mails) : je vous indique donc que je saisirai la CNIL au prochain mail commercial.
 
{GENERIC_DEMAND}
Cordialement.
{ME}"""
    print(message)


@cli.command()
@click.argument("entity", type=str)
@click.argument("previous_claims", type=str, nargs=-1)
def plainte(entity, previous_claims):
    message_cnil = f"""Bonjour
J'ai reçu plusieurs mails commerciaux non sollicités de la part de {entity} aux dates suivantes : {', '.join(previous_claims)}. J'ai systématiquement suivi la procédure de désinscription et ai obtenu validation à chaque fois. Aujourd'hui, ces sollicitations continuent malgré ces demandes (dernier mail reçu aujourd'hui) et je souhaite donc porter plainte auprès de la CNIL contre {entity} pour non respect de mon consentement (et accessoirement absence de demande de consentement).

Ces pratiques, doivent être dénoncées et punies pour éviter que des lois comme le RGPD tombent aux oubliettes, fautes de réaction de la part des consommateurs et du régulateur.

Merci d'avance pour la considération que vous porterez à ma demande.
Bien cordialement.
{ME}"""
    message_entity = f"""Bonjour
Malgré mes {len(previous_claims)} dernières demandes de désinscription à vos newsletter (dates : {', '.join(previous_claims)}) vous persistez à ne pas respecter mon droit à la désinscription, violant ainsi le GDPR. Je vous informe que je saisis donc la CNIL contre {entity}.

{GENERIC_DEMAND}
Cordialement.
{ME}"""
    print("~~~ Pour la CNIL ~~~\n")
    print(message_cnil)
    print(f"\n\n~~~ Pour {entity} ~~~\n ")
    print(message_entity)


if __name__ == "__main__":
    cli()
