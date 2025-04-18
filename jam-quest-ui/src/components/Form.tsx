import { useState } from 'react';
import axios from "axios";

function SongForm() {
    var [TopSong, SetTopSong] = useState("spotify%3Atrack%3A21qnJAMtzC6S5SESuqQLEK");

    const UpdateList = (input:string) => {
        if (input === "") {
            return;
        }
        axios({url: 'http://localhost:5000/search', params: {"q":encodeURI(input)}})
                                .then(function (response) {
                                    SetTopSong(response.data['items'][0]['uri']);
                                })
                                .catch(function (error) {
                                    console.log(error);
                                });
    };

    const AddSong = () => {
        axios({url: 'http://localhost:5000/add', 
               params: {"uri":TopSong},
               method: 'post'})
                .catch(function (error) {console.log(error);});//window.location.href="/quest"
    };
    
    return(
        <>
            <form>
                <label>
                    <input type="text" name="UserInput" onChange={ e => UpdateList(e.target.value) }/>
                </label>
            </form>
            <button 
                type="button" 
                className="btn btn-primary" 
                onClick={ () => AddSong() }>Add to Queue
            </button>
        </>
    );
}

export default SongForm;