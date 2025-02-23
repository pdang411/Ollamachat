Chat with Ollama docker application. Download code file and run in docker command prompt to your folder  contain Ollamachat. Use VScode or any other IDE open folder . 
Open CMD in Window or terminal  navigate your folder  

***Create virtual enviroment***

Create venv IOS Mac.
python3 -m venv venv
source ./venv/bin/activate
Create venv Window
python -m venv venv 
venv\Scripts\activate 

![Screenshot 2025-02-23 143624](https://github.com/user-attachments/assets/b066b1be-7fd7-44f7-97eb-5c3952c5ec13)

run $ pip install -r requirements.txt
open docker desktop in MAC or Window
run docker command terminal or cmd
docker build -t gradio-app .
docker run -d -p 7860:7860 gradio-app

![Screenshot 2025-02-23 143625](https://github.com/user-attachments/assets/82f2bfad-cd1d-4040-85b3-aff9f95cba9c)
