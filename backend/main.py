from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
from data.prediction import *
from fastapi.responses import FileResponse
import io
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/index")
def hello_world(name: str):
    return f"hello {name}!"


@app.post("/api/predict")
async def predict_image(style_path: str,file: UploadFile = File(...)):
    image = read_image(await file.read())

    #image = preprocess(image)
    styleImage = predict(image, style_path)
    print(styleImage)
    #print(predictions)
    #styleImage.save("thumbnail.png")
    header = {
        "w":str(styleImage.size[0]),
        "h":str(styleImage.size[1]),
    }
    return StreamingResponse(io.BytesIO(styleImage.tobytes()), media_type="image/png", headers=header)


    

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")