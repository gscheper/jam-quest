import axios from "axios";

function RouteButton({text, route} : {text:string, route:string}) {
    return(
        <>
        <div>
            <button 
                type="button" 
                className="btn btn-primary" 
                onClick={ () => window.location.href = route }>{ text }
            </button>
        </div> 
        </>
    );
}

function PumpUpTheJam() {
    var MakeRequest = () => {
        axios({url:'http://localhost:5000/playback/add', 
            params: {"uri":'spotify:track:21qnJAMtzC6S5SESuqQLEK'}, method: 'post'})
                .catch(function (error) {console.log(error);});
    };

    return(
        <>
        <div>
            <button 
                type="button" 
                className="btn btn-primary" 
                onClick={ () => MakeRequest() }> Pump Up The Jam
            </button>
        </div> 
        </>
    );
}

export {PumpUpTheJam, RouteButton};