import { useState } from 'react';
import axios from "axios";
import PumpUpTheJam from './PumpUpTheJam';

function SongForm() {
    var [TopSong, SetTopSong] = useState("spotify:track:21qnJAMtzC6S5SESuqQLEK");

    const UpdateList = (input:string) => {
        if (input === "") {
            return;
        }
        axios({url: 'http://' + import.meta.env.VITE_BACKEND_ENDPOINT + '/playback/search', 
            params: {"q":encodeURI(input)},
            method:'GET'})
                                .then(function (response) {
                                    SetTopSong(response.data.data.items[0].uri);
                                })
                                .catch(function (error) {
                                    console.log(error);
                                });
    };

    const AddSong = () => {
        axios({url: 'http://' + import.meta.env.VITE_BACKEND_ENDPOINT + '/playback/add', 
               params: {"uri":TopSong},
               method: 'POST'})
                .catch(function (error) {console.log(error);});//window.location.href="/quest"
    };
    
    return(
        <>
            <form>
                <label>
                    <input 
                        type="text" 
                        name="UserInput" 
                        onChange={ e => UpdateList(e.target.value) }
                        className='form'/>
                </label>
            </form>
            <div>
                <button 
                    type="button" 
                    className="btn btn-primary queue-button" 
                    onClick={ () => AddSong() }> Add to Queue
                </button>
                <PumpUpTheJam/>
            </div>
        </>
    );
}

export default SongForm;