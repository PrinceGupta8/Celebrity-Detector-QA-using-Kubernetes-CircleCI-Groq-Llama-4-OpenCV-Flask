import os
from flask import request,render_template,Blueprint
from src.celebrity_detector import CelebrityDetector
from src.image_handler import process_image
from src.qa_engine import QAEngine
import base64

detecter=CelebrityDetector()
engine=QAEngine()

main=Blueprint("main" , __name__)
@main.route("/",methods=["GET","POST"])
def index():
    player_info=""
    result_img_data=""
    user_question=""
    answer=""

    if request.method=="POST":
        if "image" in request.files:
            img=request.files["image"]
            
            img_bytes,face_box=process_image(img)
            player_info, player_name=detecter.identify(img_bytes)

            if face_box is not None:
                result_img_data=base64.b64encode(img_bytes).decode()
            else:
                player_info="No face detected please try different image"

        elif "question" in request.form:
            user_question = request.form["question"]
            player_name=request.form["player_name"]
            player_info=request.form["player_info"]
            result_img_data=request.form["result_img_data"]
            answer=engine.ask_about_celebrity(name=player_name,question=user_question)
    return render_template(
        "index.html",
        player_info=player_info,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
        )
