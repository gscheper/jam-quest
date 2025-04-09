import axios from 'axios';
import { useState } from 'react';

function Quest() {
    const games = [
        ["2 + 2", "4"],
        ["2 + 3", "5"],
        ["2 + 4", "6"],
        ["2 + 5", "7"]
    ]
    var [Answer, SetAnswer] = useState("");
    var [Index, SetIndex] = useState(Math.floor(games.length * Math.random()));

    const HandleAnswer = () => {
        if (Answer===games[Index][1]) {
            axios({url:'http://localhost:5000/user/king'})
                    .then(function () {})//window.location.href = "http://localhost:5173/queue";
                    .catch(function (error) {console.log(error);});
        }
    }

    return (
        <>
            <div className="mb-3">
                <label className="form-label">{games[Index][0]}</label>
                <input type="text" name="UserInput" className="form-control" onChange={e => SetAnswer(e.target.value)}/>
                <button className="btn btn-primary" type="submit" onClick={() => HandleAnswer()} >Submit</button>
            </div>
        </>
    );
  }
  
export default Quest;