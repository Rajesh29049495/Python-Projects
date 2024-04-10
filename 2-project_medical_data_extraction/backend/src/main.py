from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(                          # to extract we will use `extract` function that we created, which will need file path and file format, so this is something that should come with the request,
        file_format: str = Form(...),
        file: UploadFile = File(...),
):
    contents = file.file.read()                    # first read the content of the uploaded file

    file_path = "../uploads/" + str(uuid.uuid4())  + ".pdf"

    with open(file_path, "wb") as f:      # the mode that we use is "wb", because uploaded dats is in bytes
        f.write(contents)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }


    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)