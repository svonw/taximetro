def main():
    print("=== Calculadora de Tarifas ===")
    print("1. Modo CLI")
    print("2. Modo Web (Streamlit)")

    opcion = input("Elige opción (1/2): ")

    while opcion not in ("1", "2"):
        print("Opción inválida")
        opcion = input("Elige opción (1/2): ")
    if opcion == "1":
        import cli
        cli.main()
    elif opcion == "2":
        import subprocess
        subprocess.run(["streamlit", "run", "streamlit_app.py"])




if __name__ == "__main__":
    main()