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

function RequestButton({text} : {text:string}) {
    //console.log(encodeURI("remaster track Doxy artist Miles Davis"));
    const MakeRequest = () => axios.get('http://localhost:5000/playback/pump_up_the_jam')
                                .then(function (response) {
                                    console.log(response);
                                })
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

export {RequestButton, RouteButton};