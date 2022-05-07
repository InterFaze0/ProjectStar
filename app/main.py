from discord.ext import commands
from flask import Flask,jsonify
import multiprocessing as mlps
import json



app = Flask(__name__)
flow = commands.Bot("!f ")

@flow.event
async def on_ready():
    print("Flow started!")


@flow.command()
async def up(message,*args):
    data = {
        "valueOne":args[0],
        "valueTwo":args[1],
        "valueThree":args[2]
    }
    with open("json_data.json","w") as myJsonFileW:
        json.dump(data,myJsonFileW)
    await message.send("Api update edildi!")

@app.route("/")
def index():
    with open("json_data.json","r") as myJsonFileR:
        data =json.load(myJsonFileR)
    return jsonify(data)


token ="ODkxNjkxNzQ3OTI1Njg4NDMx.YVCCpw.iCBTSZzbuLkr4b4DJ36aVwnmG-U"
def processOne():
    flow.run(token)
    
def processTwo():
    app.run(debug=False)

p1 = mlps.Process(target=processOne)
p2 = mlps.Process(target=processTwo)



if __name__ == "__main__":
    p1.start()
    p2.start()




