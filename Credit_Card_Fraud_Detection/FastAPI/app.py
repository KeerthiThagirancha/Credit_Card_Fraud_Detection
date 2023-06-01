# 1. Install uvicorn and fastapi
#pip install
# 1. Imports Libraries
import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import pickle

# 2. Create the  app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#3.load the model
rgModel = pickle.load(open("card.pkl", "rb"))

# 4. Index route, opens automatically on http://127.0.0.1:80
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')

#----------------------

@app.get("/predictOutcome")
def getPredictOutcome(AverageAmountTransaction: float, TransactionAmount: float, IsDeclined: int, TotalNumberOfDeclines: int):
 #rgModel = pickle.load(open("card.pkl", "rb"))
 prediction = rgModel.predict([[AverageAmountTransaction, TransactionAmount, IsDeclined, TotalNumberOfDeclines]])
 #return [{'Outcome': prediction[0]}]
 val = prediction[0];
 print(val);
 return [{'message': str(val)}]


# uvicorn app:app --host 0.0.0.0 --port 80
# http://127.0.0.1:80/predictOutcome?AverageAmountTransaction=185.5&TransactionAmount=4823&IsDeclined=1&TotalNumberOfDeclines=5
