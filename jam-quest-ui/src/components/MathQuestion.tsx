import { useState } from 'react';

function MathQuestion() {
    const games = [
        ["2 + 2", "4"],
        ["2 + 3", "5"],
        ["2 + 4", "6"],
        ["2 + 5", "7"]
    ]
    var [Answer, SetAnswer] = useState("");
    var Index = useState(Math.floor(games.length * Math.random()))[0];

    const HandleAnswer = () => {
        if (Answer===games[Index][1]) {window.location.href = "http://localhost:5173/queue"}
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
  
export default MathQuestion;