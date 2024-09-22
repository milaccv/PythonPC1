archivo = input("Introduce el nombre del archivo: ").lower()
extensiones = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

extension = archivo[archivo.rfind("."):]
tipo_mime = extensiones.get(extension, "application/octet-stream")
print(f"El tipo MIME es: {tipo_mime}")