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

function PumpUpTheJam({text} : {text:string}) {
    const MakeRequest = () => axios({url:'http://localhost:5000/playback/add', 
                                params:{"uri":"spotify%3Atrack%3A21qnJAMtzC6S5SESuqQLEK"}})
                                .catch(function (error) {
                                    console.log(error);
                                });

    return(
        <>
        <div>
            <button 
                type="button" 
                className="btn btn-primary" 
                onClick={ MakeRequest }>{ text }
            </button>
        </div> 
        </>
    );
}

export {PumpUpTheJam, RouteButton};