import tkinter as tk
from tkinter import messagebox
import webbrowser
import ctypes
import subprocess

PASSWORD_LENGTH = 14

def acessar_portal_office():
    url_portal_office = "https://account.activedirectory.windowsazure.com/ChangePassword.aspx"
    webbrowser.open(url_portal_office)

def conectar_vpn():
    # Caminho para o executável do WatchGuard Mobile VPN
    caminho_executavel = r"C:\Program Files (x86)\WatchGuard\WatchGuard Mobile VPN with SSL\wgsslvpnc.exe"

    try:
        # Executa o programa externo
        subprocess.run([caminho_executavel])
        print("VPN conectada com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar à VPN: {e}")
        messagebox.showwarning("Erro", "Não foi possível abrir o aplicativo VPN.\nPossíveis causas:\nO aplicativo Mobile VPN with SSL client não está instalado.\nSe você utiliza a VPN nativa do Windows, tente conectar-se manualmente.")

def bloquear_tela():
    # Chama a função LockWorkStation para bloquear a tela
    ctypes.windll.user32.LockWorkStation()

# Criar a janela principal
root = tk.Tk()
root.title("Assistente de Troca de Senha")

# Cor de fundo
root.configure(bg="#343541")

# Tamanho da janela
root.geometry("1100x700")

# Fonte
fonte_titulo = ("Helvetica", 16, "bold")
fonte_texto = ("Helvetica", 12)

# Título
label_titulo = tk.Label(root, text="Assistente de Troca de Senha", font=fonte_titulo, bg="#343541", fg="white")
label_titulo.pack(pady=10)

# Descrição
label_descricao = tk.Label(root, text="Clique no botão abaixo para acessar o Portal do Office e realizar a atualização de senha.", font=fonte_texto, bg="#343541", fg="white")
label_descricao.pack(pady=10)

label_descricao = tk.Label(root, text="Obs. Talvez seja necessário realizar login no portal, após o login, será redirecionado para a página para efetuar a troca da senha.", font=fonte_texto, bg="#343541", fg="white")
label_descricao.pack(pady=10)

# Botão para acessar o Portal do Office
btn_acessar_portal = tk.Button(root, text="Acessar o Portal do Office", command=acessar_portal_office, font=fonte_texto, bg="#0C2D57", fg="white", relief="flat")
btn_acessar_portal.pack(pady=10)

# Requisitos de senha
label_requisitos = tk.Label(root, text=f"Sua nova senha deve conter no mínimo {PASSWORD_LENGTH} caracteres, incluindo:", font=fonte_texto, bg="#343541", fg="white")
label_requisitos.pack(pady=10, anchor="w")

# Lista de requisitos
requisitos = ["letras minúsculas", "letras maiúsculas", "números", "caracteres especiais"]

for requisito in requisitos:
    label_requisito = tk.Label(root, text=f"\u2022 {requisito}", font=fonte_texto, bg="#343541", fg="white")
    label_requisito.pack(anchor="w")

label_requisitos = tk.Label(root, text="Após a troca da senha, clique no botão abaixo para abrir o aplicativo da VPN:", font=fonte_texto, bg="#343541", fg="white")
label_requisitos.pack(pady=10, anchor="w")

label_requisitos = tk.Label(root, text="Conecte-se na vpn com a senha nova:", font=fonte_texto, bg="#343541", fg="white")
label_requisitos.pack(pady=10, anchor="w")

# Botão para conectar à VPN
btn_conectar_vpn = tk.Button(root, text="Abrir aplicativo de VPN", command=conectar_vpn, font=fonte_texto, bg="#0C2D57", fg="white", relief="flat")
btn_conectar_vpn.pack(pady=10)

label_requisitos = tk.Label(root, text="Após conectar na VPN com a senha nova, clique no botão abaixo para bloquear a tela, em seguida, desbloqueie com a sua nova senha:", font=fonte_texto, bg="#343541", fg="white")
label_requisitos.pack(pady=10, anchor="w")

# Botão para bloquear/desbloquear a tela
btn_bloquear_desbloquear_tela = tk.Button(root, text="Bloquear a Tela", command=bloquear_tela, font=fonte_texto, bg="#0C2D57", fg="white", relief="flat")
btn_bloquear_desbloquear_tela.pack(pady=10)

label_requisitos = tk.Label(root, text="Se já conseguiu logar com sua nova senha e acessar os diretórios e sistemas da empresa pode clicar no botão abaixo para fechar essa janela:", font=fonte_texto, bg="#343541", fg="white")
label_requisitos.pack(pady=10, anchor="w")

# Botão para fechar a janela
btn_fechar_janela = tk.Button(root, text="Fechar Janela", command=root.destroy, font=fonte_texto, bg="#e74c3c", fg="white", relief="flat")
btn_fechar_janela.pack(pady=10)

root.mainloop()
