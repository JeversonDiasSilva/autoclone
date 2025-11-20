# 🎮 Clonador de Sistemas para Batocera

Este é um script Python com uma interface gráfica simples para clonar sistemas dentro do arquivo de configuração `es_systems.cfg` do Batocera.

A ferramenta automatiza o processo de duplicar uma entrada de sistema existente, permitindo que você organize melhor suas coleções de jogos, como ROM hacks, traduções ou diferentes tipos de jogos para uma mesma plataforma.

## ✨ Funcionalidades Principais

*   **Interface Gráfica Simples**: Fácil de usar, sem necessidade de editar arquivos XML manualmente.
*   **Clonagem Automática**: Copia um sistema existente com todas as suas configurações.
*   **Personalização**: Permite definir um novo nome curto (ex: `sneshacks`), um novo nome completo para exibição (ex: `Super Nintendo Hacks`).
*   **Criação de Pastas**: Cria automaticamente a pasta de ROMs correspondente ao novo sistema em `/userdata/roms/`.
*   **Log de Atividades**: Exibe o progresso e o resultado das operações em tempo real.

## 🤔 Por que usar? (Caso de Uso)

Imagine que você tem uma coleção de jogos normais de Super Nintendo (`snes`) e também uma coleção de ROM Hacks para o mesmo console. Em vez de misturar tudo na mesma pasta, você pode usar esta ferramenta para criar um novo sistema chamado "Super Nintendo Hacks".

1.  **Sistema Base**: `snes`
2.  **Novo Sistema**: `sneshacks`
3.  **Nome Completo**: `Super Nintendo Hacks`

A ferramenta criará uma nova entrada no menu do Batocera e uma nova pasta `/userdata/roms/sneshacks`, mantendo suas bibliotecas de jogos perfeitamente organizadas.


1.  A janela do aplicativo será aberta. Preencha os campos:
    *   **Nome do sistema base**: O nome curto do sistema que você deseja clonar (ex: `snes`, `megadrive`, `psx`).
    *   **Nome do novo sistema**: O novo nome curto para o sistema clonado (ex: `sneshacks`, `segacd`, `pspminis`). Deve ser uma única palavra, sem espaços.
    *   **Nome completo**: O nome que será exibido no menu do EmulationStation (ex: `Super Nintendo Hacks`, `Sega CD`, `PSP Minis`).

2.  Clique no botão **"🚀 Clonar Sistema"**.

3.  Acompanhe o progresso na caixa de texto na parte inferior. Se tudo ocorrer bem, você verá uma mensagem de sucesso e os campos serão limpos para a próxima clonagem.

4.  Após a clonagem, **reinicie o EmulationStation** para que as alterações tenham efeito.

## ⚠️ Atenção!

*   **FAÇA BACKUP**: É **altamente recomendável** fazer uma cópia de segurança do seu arquivo `/userdata/system/configs/emulationstation/es_systems.cfg` antes de usar esta ferramenta. Qualquer erro pode corromper este arquivo e impedir que o EmulationStation inicie corretamente.
*   **ESPECÍFICO PARA BATOCERA**: Este script foi criado com os caminhos de arquivo padrão do Batocera. Ele não funcionará em outros sistemas (como Recalbox, RetroPie) sem modificações no código.

<img src="https://github.com/JeversonDiasSilva/autoclone/blob/main/img/autoclone.jpeg" />

# Instalação (Em Breve...)
```bash
curl -sL bit.ly/JCGAMES-AUTOCLONE | bash
```


<br><br>
