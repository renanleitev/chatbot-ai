import customtkinter as ctk
import requests
from bs4 import BeautifulSoup

class Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Artemis")
        master.geometry("800x600")

        # Configuração da janela
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=0)
        master.grid_rowconfigure(2, weight=0)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Área de texto
        self.text_area = ctk.CTkTextbox(master, width=700, height=400, wrap="word")
        self.text_area.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.text_area.insert(ctk.END, "Olá! Me informe o protocolo ou a data, hora que você deseja consultar.\n")
        self.text_area.configure(state="disabled")

        # Campo de entrada
        self.entry = ctk.CTkEntry(master, width=500, placeholder_text="Digite o protocolo ou a data, hora...")
        self.entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry.bind("<Return>", self.process_input)

        # Botão de envio
        self.send_button = ctk.CTkButton(master, text="Enviar", fg_color="blue", command=self.process_input)
        self.send_button.grid(row=2, column=0, padx=20, pady=10)

    def process_input(self, event=None):
        user_input = self.entry.get()
        if not user_input:
            return

        self.text_area.configure(state="normal")
        self.text_area.insert(ctk.END, "Você: " + user_input + "\n")
        self.text_area.configure(state="disabled")

        response = self.get_response(user_input)

        self.text_area.configure(state="normal")
        self.text_area.insert(ctk.END, "Artemis: " + response + "\n")
        self.text_area.configure(state="disabled")

        self.entry.delete(0, ctk.END)

    def format_response(self, cells):
        protocolo = cells[0].get_text().strip()
        data_ocorrencia = cells[1].get_text().strip()
        hora_ocorrencia = cells[2].get_text().strip()
        natureza = cells[3].get_text().strip()
        tipo = cells[13].get_text().strip()
        situacao = cells[4].get_text().strip()
        bairro = cells[5].get_text().strip()
        endereco = cells[6].get_text().strip()
        return "\n".join([
            f"Protocolo: {protocolo}",
            f"Data: {data_ocorrencia}",
            f"Hora: {hora_ocorrencia}",
            f"Natureza: {natureza}",
            f"Tipo: {tipo}",
            f"Situação: {situacao}",
            f"Bairro: {bairro}",
            f"Endereço: {endereco}",
        ])

    def get_response(self, user_input):
        try:
            response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRcWiuMO_XIUBLdF-11eT8Y-8aaI17b7SwwPvK90yfnMjdTna32DOkXCqlmqe-ODXyoo5LqY0gYlrQx/pubhtml")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                rows = soup.find_all('tr')

                # Verificar se o input contém uma data e hora no formato 'data, hora'
                if ',' in user_input:
                    data, hora = user_input.split(',')
                    data = data.strip()
                    hora = hora.strip()

                    for row in rows[1:]:
                        cells = row.find_all('td')
                        data_ocorrencia = cells[1].get_text().strip()
                        hora_ocorrencia = cells[2].get_text().strip()

                        if data == data_ocorrencia and hora == hora_ocorrencia:
                            return self.format_response(cells)
                
                # Caso o input seja apenas protocolo
                for row in rows[1:]:
                    cells = row.find_all('td')
                    protocolo = cells[0].get_text().strip()

                    if user_input.strip() == protocolo:
                        return self.format_response(cells)

                return "Dados não encontrados para o protocolo, data ou hora especificados."
            else:
                return "Erro ao acessar a planilha."
        except requests.exceptions.RequestException as e:
            return f"Erro ao conectar com a tabela: {e}"

if __name__ == "__main__":
    root = ctk.CTk()
    chatbot = Chatbot(root)
    root.mainloop()
