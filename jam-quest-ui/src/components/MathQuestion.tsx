import { useState } from 'react';
import axios from "axios";
axios.defaults.withCredentials=true;
axios.defaults.headers.get['Content-Type'] ='application/x-www-form-urlencoded';
axios.defaults.headers.get['Access-Control-Allow-Credentials'] ='include';

function MathQuestion() {
    axios({url:'http://localhost:5000/quest', 
           method:"get"})
            .then(function (response) {console.log(response);})
    const games = [
        ["2 + 2", "4"],
        ["2 + 3", "5"],
        ["2 + 4", "6"],
        ["2 + 5", "7"]
    ]
    var [Answer, SetAnswer] = useState("");
    var Index = useState(Math.floor(games.length * Math.random()))[0];

    const HandleAnswer = () => {
        if (Answer===games[Index][1]) {
            axios({url:'http://localhost:5000/quest/king',
                method:'post'
            }).then(function () {window.location.href = "http://localhost:5173/queue"})
        }
    }

    return (
    <div className="mb-3 grid-container">
        <label className="form-label quest-text">{games[Index][0]}</label>
        <input type="text" name="UserInput quest-form" className="form-control" onChange={e => SetAnswer(e.target.value)}/>
        <button className="btn btn-primary quest-button" type="submit" onClick={() => HandleAnswer()} >Submit</button>
    </div>
    );
  }
  
export default MathQuestion;