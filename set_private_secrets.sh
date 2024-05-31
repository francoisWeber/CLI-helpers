#!/bin/bash

/opt/homebrew/bin/enpass-cli -vault=$HOME/Documents/Enpass/Vaults/primary/ -pin show ENV_PERSO 2>&1 | while IFS= read -r line; do

    cleaned_line=$(echo "$line" | sed 's/"$//')

    # Extraction de la valeur de la clef "password"
    LOGIN=$(echo $cleaned_line | perl -nle 'print $1 if /login:\s*(\S+)/')
    PASSWD=$(echo $cleaned_line | perl -nle 'print $1 if /password:\s*(\S+)/')

    # Affichage des valeurs extraites
    echo "export $LOGIN=$PASSWD" >> ./.secrets
done

