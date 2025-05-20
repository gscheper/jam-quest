import { useState } from 'react';
import axios from "axios";
axios.defaults.withCredentials=true;
axios.defaults.headers.get['Content-Type'] ='application/x-www-form-urlencoded';
axios.defaults.headers.get['Access-Control-Allow-Credentials'] ='include';

function MathQuestion() {
    const GetQuestion = () => {
        axios({url:'http://localhost:5000/quest', method:"get"})
        .then(function (response) {SetQuestion(response.data['Quest']);})
        .catch(function () {SetQuestion("");})
    }
    
    const HandleAnswer = (answer:String) => {
            axios({url:'http://localhost:5000/quest',
                method:'post',
                params:{'Quest':Question,'Answer':String(answer)}
            }).then(function () {window.location.href = 'http://localhost:5173/queue';})
            .catch(function (err) {console.log(err)})
    }
    
    var [Answer, SetAnswer] = useState("");
    var [Question, SetQuestion] = useState("");
    
    GetQuestion();

    return (
    <div className="mb-3 grid-container">
        <label className="form-label quest-text"> { Question } </label>
        <input type="text" name="UserInput quest-form" className="form-control" onChange={e => SetAnswer(e.target.value)}/>
        <button className="btn btn-primary quest-button" type="submit" onClick={ () => HandleAnswer(Answer) } >Submit</button>
    </div>
    );
  }
  
export default MathQuestion;