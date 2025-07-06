import customtkinter as ctk
import xml.etree.ElementTree as ET
import copy
import re
import os

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


def extrair_sistema(xml_path, nome_sistema):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for system in root.findall('system'):
            name = system.find('name')
            if name is not None and name.text == nome_sistema:
                return copy.deepcopy(system)
    except Exception:
        return None
    return None


def modificar_clone(system, novo_nome, novo_fullname, nome_base):
    name_tag = system.find('name')
    if name_tag is not None:
        name_tag.text = novo_nome

    fullname_tag = system.find('fullname')
    if fullname_tag is not None:
        fullname_tag.text = novo_fullname

    path_tag = system.find('path')
    if path_tag is not None:
        path_tag.text = f"/userdata/roms/{novo_nome}"

    for elem in system.iter():
        if elem.text and '%SYSTEM%' in elem.text:
            elem.text = elem.text.replace('%SYSTEM%', nome_base)

    xml_str = ET.tostring(system, encoding='unicode')
    comentario = f'<!-- Clone gerado automaticamente a partir de "{nome_base}" -->'
    return f'{comentario}\n{xml_str}'


def inserir_clone_no_arquivo(xml_path, nome_base, clone_str):
    with open(xml_path, 'r', encoding='utf-8') as f:
        original = f.read()

    padrao = re.compile(r'(<system>.*?<name>' + re.escape(nome_base) + r'</name>.*?</system>)', re.DOTALL)
    resultado = padrao.search(original)

    if not resultado:
        return False, "Sistema base não encontrado no arquivo."

    trecho_base = resultado.group(1)
    novo_texto = original.replace(trecho_base, trecho_base + "\n" + clone_str)

    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(novo_texto)

    return True, "Clone inserido com sucesso!"


def criar_pasta_roms(nome_novo):
    pasta = f"/userdata/roms/{nome_novo}"
    try:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            return f"Pasta criada: {pasta}"
        else:
            return f"Pasta já existe: {pasta}"
    except Exception as e:
        return f"Erro ao criar pasta: {e}"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎮 Clonador de Sistemas - Batocera")
        self.geometry("550x480")
        self.resizable(False, False)

        self.xml_path = "es_systems.cfg"

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="Clonar Sistema do Batocera", font=("Roboto", 20, "bold")).pack(pady=(10, 15))

        self.entry_base = ctk.CTkEntry(self.frame, width=400, placeholder_text="Nome do sistema base (ex: snes)")
        self.entry_base.pack(pady=10)

        self.entry_novo = ctk.CTkEntry(self.frame, width=400, placeholder_text="Nome do novo sistema (ex: sneshack)")
        self.entry_novo.pack(pady=10)

        self.entry_fullname = ctk.CTkEntry(self.frame, width=400, placeholder_text="Nome completo (ex: Super Nintendo Hacks)")
        self.entry_fullname.pack(pady=10)

        self.botao = ctk.CTkButton(self.frame, text="🚀 Clonar Sistema", command=self.clonar, width=200)
        self.botao.pack(pady=(15, 10))

        self.resultado = ctk.CTkTextbox(self.frame, height=160, width=500, corner_radius=6)
        self.resultado.pack(pady=(5, 10))
        self.limpar_texto()
        self.inserir_linha("📂 Aguardando entrada...")

    def limpar_texto(self):
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", "end")
        self.resultado.configure(state="disabled")

    def inserir_linha(self, texto):
        self.resultado.configure(state="normal")
        self.resultado.insert("end", texto + "\n")
        self.resultado.see("end")
        self.resultado.configure(state="disabled")

    def clonar(self):
        base = self.entry_base.get().strip()
        novo = self.entry_novo.get().strip()
        fullname = self.entry_fullname.get().strip()

        self.limpar_texto()
        self.inserir_linha("📂 Aguardando entrada...")

        if not os.path.exists(self.xml_path):
            self.inserir_linha("❌ Arquivo es_systems.cfg não encontrado.")
            return

        if not base or not novo or not fullname:
            self.inserir_linha("⚠️ Por favor, preencha todos os campos.")
            return

        self.inserir_linha("⚙️ Processando sistema base...")
        system = extrair_sistema(self.xml_path, base)
        if system is None:
            self.inserir_linha(f"❌ Sistema base '{base}' não encontrado no arquivo.")
            return

        self.inserir_linha("⚙️ Criando clone...")
        clone_str = modificar_clone(system, novo, fullname, base)
        sucesso, mensagem = inserir_clone_no_arquivo(self.xml_path, base, clone_str)
        self.inserir_linha(f"📦 {mensagem}")

        if sucesso:
            pasta_msg = criar_pasta_roms(novo)
            self.inserir_linha(f"📁 {pasta_msg}")
            # Limpa campos
            self.entry_base.delete(0, 'end')
            self.entry_novo.delete(0, 'end')
            self.entry_fullname.delete(0, 'end')
            self.inserir_linha("✅ Clonagem concluída com sucesso!")
        else:
            self.inserir_linha("❌ Falha na clonagem.")

if __name__ == "__main__":
    app = App()
    app.mainloop()