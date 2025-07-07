#!/bin/bash
# Curitiba 07 de Julho de 2025.
# Editor: Jeverson D. Silva   ///@JCGAMESCLASSICOS...

# INSTALAÇÂO...




url="https://github.com/JeversonDiasSilva/autoclone/releases/download/v1.0/SYSTEMCLONE"
squash=$(basename "$url")
base_scripts="/userdata/system/.dev/apps"
dir_work="$base_scripts/systemclone"
local="/userdata/system/.local/share/applications"

mkdir -p "$base_scripts"
mkdir -p "$local"
wget "$url" -O "$base_dir"/"$squash" > /dev/null 2>&1
unsquashfs -d "$dir_work" "$squash" > /dev/null 2>&1
rm "$squash"
chmod -R 777 "/userdata/system/.dev/apps/systemclone"
mv /userdata/system/.dev/apps/systemclone/autoclone.desktop "$local"
echo "Instalação concluida"
