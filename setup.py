from cx_Freeze import setup, Executable

# Defina o script que você quer transformar em executável
executables = [Executable("chatbot.py", icon="icone.ico")]

# Configura a construção
setup(
    name="ChatBot",
    version="1.0",
    description="ChatBot com Python",
    executables=executables
)