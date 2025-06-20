import axios from "axios";


function PumpUpTheJam() {
    var MakeRequest = () => {
        axios({url:'http://' + import.meta.env.VITE_BACKEND_ENDPOINT + '/playback/add', 
            params: {"uri":'spotify:track:21qnJAMtzC6S5SESuqQLEK'}, 
            method: 'post',
            withCredentials: false})
                .catch(function (error) {console.log(error);});
    };

    return(
        <>
        <button 
        type="button" 
                className="btn btn-primary button queue-button" 
                onClick={ () => MakeRequest() }> 
                    Pump Up The Jam
                    </button>
        </>
    );
}

export default PumpUpTheJam;