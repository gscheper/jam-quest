import axios from "axios";

function RedirToQuest() {
    var MakeRequest = () => {
        axios({url:'http://localhost:5000/quest/king', 
               method: 'get'})
                .then(function (response) {
                    if (response.data['king'] != 1) {
                        window.location.href = "/quest";
                    }
                    })
                .catch(function (error) {console.log(error);});
    };

    MakeRequest();
}
  
export default RedirToQuest;